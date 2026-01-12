"""
PubMed Healthcare Chatbot - Main Application
LLM Augmented Q&A over PubMed Search Engine
"""

from pymed import PubMed
from typing import List
from haystack import component
from haystack import Document
from haystack.components.generators import HuggingFaceTGIGenerator
from dotenv import load_dotenv
import os 
from haystack import Pipeline
from haystack.components.builders.prompt_builder import PromptBuilder
import gradio as gr
import json
import time

# Load environment variables
load_dotenv()

# Configuration
os.environ['HUGGINGFACE_API_KEY'] = os.getenv('HUGGINGFACE_API_KEY')

# Load config
with open('config.json', 'r') as f:
    config = json.load(f)

# Initialize PubMed
pubmed = PubMed(
    tool=config['pubmed']['tool'], 
    email=os.getenv('PUBMED_EMAIL', 'healthcare.chatbot@gmail.com')
)

def documentize(article):
    """Convert PubMed article to Haystack Document format."""
    return Document(
        content=article.abstract, 
        meta={
            'title': article.title, 
            'keywords': article.keywords,
            'publication_date': str(article.publication_date),
            'doi': article.doi,
            'authors': article.authors
        }
    )

@component
class PubMedFetcher():
    """Custom component to fetch articles from PubMed."""
    
    @component.output_types(articles=List[Document])
    def run(self, queries: list[str]):
        cleaned_queries = queries[0].strip().split('\n')
        
        articles = []
        try:
            for query in cleaned_queries:
                if query:  # Skip empty queries
                    response = pubmed.query(
                        query, 
                        max_results=config['pubmed']['max_results']
                    )
                    documents = [documentize(article) for article in response]
                    articles.extend(documents)
        except Exception as e:
            print(f"Error fetching PubMed articles: {e}")
            print(f"Failed queries: {queries}")
        
        results = {'articles': articles}
        return results

# Initialize Language Models
keyword_llm = HuggingFaceTGIGenerator(
    model=config['models']['keyword_generator'],
    generation_kwargs={
        "max_new_tokens": 100,
        "temperature": 0.3
    }
)
keyword_llm.warm_up()

llm = HuggingFaceTGIGenerator(
    model=config['models']['answer_generator'],
    generation_kwargs={
        "max_new_tokens": config['generation']['max_new_tokens'],
        "temperature": config['generation']['temperature'],
        "top_p": config['generation']['top_p']
    }
)
llm.warm_up()

# Prompt Templates
keyword_prompt_template = """
Your task is to convert the following question into 3 keywords that can be used to find relevant medical research papers on PubMed.

IMPORTANT RULES:
1. Use Medical Subject Headings (MeSH) terms when possible
2. Be specific and precise
3. Focus on medical/clinical terminology
4. Output exactly 3 keywords, one per line
5. No explanations, just keywords

Here is an example:
question: "What are the latest treatments for major depressive disorder?"
keywords:
Antidepressive Agents
Depressive Disorder, Major
Treatment-Resistant depression

---
question: {{ question }}
keywords:
"""

prompt_template = """
Answer the question truthfully based on the given documents.
If the documents don't contain enough information, use your existing knowledge but clearly indicate what comes from documents vs general knowledge.

CRITICAL INSTRUCTIONS:
1. Base your answer primarily on the provided documents
2. If using general knowledge, state it explicitly
3. Be accurate and concise
4. Use medical terminology appropriately
5. Format your answer with clear sections if helpful

Question: {{ question }}

Retrieved PubMed Articles:
{% for article in articles %}
---
Article {{ loop.index }}:
Title: {{article.meta['title']}}
Keywords: {{article.meta['keywords']}}
Publication Date: {{article.meta['publication_date']}}

Abstract:
{{article.content}}
{% endfor %}

Based on the above information, provide a comprehensive answer:
"""

# Initialize Components
keyword_prompt_builder = PromptBuilder(template=keyword_prompt_template)
prompt_builder = PromptBuilder(template=prompt_template)
fetcher = PubMedFetcher()

# Build Pipeline
pipe = Pipeline()

# Add components
pipe.add_component("keyword_prompt_builder", keyword_prompt_builder)
pipe.add_component("keyword_llm", keyword_llm)
pipe.add_component("pubmed_fetcher", fetcher)
pipe.add_component("prompt_builder", prompt_builder)
pipe.add_component("llm", llm)

# Connect components
pipe.connect("keyword_prompt_builder.prompt", "keyword_llm.prompt")
pipe.connect("keyword_llm.replies", "pubmed_fetcher.queries")
pipe.connect("pubmed_fetcher.articles", "prompt_builder.articles")
pipe.connect("prompt_builder.prompt", "llm.prompt")

def ask(question):
    """Process a question through the pipeline."""
    if not question or question.strip() == "":
        return "Please enter a valid medical question."
    
    print(f"\nProcessing question: {question}")
    start_time = time.time()
    
    try:
        output = pipe.run(data={
            "keyword_prompt_builder": {"question": question},
            "prompt_builder": {"question": question},
            "llm": {
                "generation_kwargs": {
                    "max_new_tokens": config['generation']['max_new_tokens'],
                    "temperature": config['generation']['temperature']
                }
            }
        })
        
        processing_time = time.time() - start_time
        print(f"Processing completed in {processing_time:.2f} seconds")
        
        if output['llm']['replies']:
            answer = output['llm']['replies'][0]
            
            # Add metadata footer
            answer_with_footer = f"""
{answer}

---
*Response generated in {processing_time:.1f}s using PubMed search and {config['models']['answer_generator']}.*  
*Disclaimer: This information is for educational purposes only. Consult healthcare professionals for medical advice.*
"""
            return answer_with_footer
        else:
            return "No response generated. Please try again with a different question."
            
    except Exception as e:
        print(f"Error processing question: {e}")
        return f"Error processing your question. Please try again or rephrase your question.\n\nError details: {str(e)[:200]}"

# Create Gradio Interface
iface = gr.Interface(
    fn=ask, 
    inputs=gr.Textbox(
        label="Medical Question",
        placeholder="Enter your biomedical question here...",
        value="How are mRNA vaccines being used for cancer treatment?",
        lines=3
    ), 
    outputs=gr.Markdown(
        label="AI Assistant Response"
    ),  
    title="PubMed Healthcare Chatbot - LLM Augmented Q&A over PubMed Search Engine",
    description="""
    ## 🤖 AI-Powered Medical Research Assistant
    
    This chatbot helps you find and understand medical research from PubMed. 
    It converts your questions into PubMed searches, retrieves relevant articles, 
    and synthesizes information using advanced language models.
    
    ### How it works:
    1. Enter a medical question in natural language
    2. System converts it to PubMed search terms
    3. Fetches relevant research articles
    4. Generates evidence-based answer
    
    ### Example questions to try:
    """,
    examples=[
        ["How are mRNA vaccines being used for cancer treatment?"], 
        ["What are the latest treatments for Alzheimer's disease?"],
        ["Tell me about the relationship between gut microbiome and mental health."],
        ["What are effective non-pharmacological treatments for chronic pain?"],
        ["How does intermittent fasting affect metabolic health?"],
        ["What are the risk factors for developing type 2 diabetes?"]
    ],
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="gray",
    ),
    allow_flagging="never",
    article="""
    ### About This Project
    This is an open-source healthcare chatbot that combines PubMed search with LLM capabilities. 
    It's designed for educational and research purposes only.
    
    **Key Features:**
    - Natural language medical question understanding
    - Real-time PubMed database search
    - Evidence-based answer generation
    - Clear source attribution
    
    **Important Notes:**
    - Not a substitute for professional medical advice
    - Always verify information with healthcare providers
    - Responses are based on available PubMed literature
    """
)

# Launch application
if __name__ == "__main__":
    print("🚀 Starting PubMed Healthcare Chatbot...")
    print(f"📊 Using model: {config['models']['answer_generator']}")
    print("🔍 PubMed tool configured:", config['pubmed']['tool'])
    print("🌐 Web interface starting on http://localhost:7860")
    print("⏳ Initializing models... (this may take a moment)")
    
    iface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        debug=False,
        show_error=True
    )
