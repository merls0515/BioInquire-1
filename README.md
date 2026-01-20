<div align="center">

# 🏥 BioInquire-1
### *PubMed Healthcare Chatbot*

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Haystack 2.0](https://img.shields.io/badge/Haystack-2.0-orange.svg)](https://haystack.deepset.ai/)
[![Gradio](https://img.shields.io/badge/UI-Gradio-green.svg)](https://gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**LLM Augmented Q&A over PubMed Search Engine**

![Healthcare Chatbot Demo](https://github.com/Saunakghosh10/healthcare-searchtool/assets/76943154/7956586a-51fa-4e1d-9fe9-572e1a4a18b3)

---

</div>

## 📋 Overview

**BioInquire-1** is an AI-powered healthcare assistant that bridges the gap between medical questions and evidence-based answers. By integrating **PubMed's vast medical literature** with **Large Language Models**, it delivers accurate, research-backed responses to healthcare queries.

<table>
<tr>
<td width="50%">

### 🎯 **What It Does**
- Searches PubMed for relevant medical research
- Synthesizes findings using AI
- Provides evidence-based answers
- Cites sources transparently

</td>
<td width="50%">

### 💡 **Why It Matters**
- Instant access to medical literature
- Reduces research time from hours to seconds
- Grounded in peer-reviewed research
- User-friendly for non-experts

</td>
</tr>
</table>

---

## 📊 Project Presentation

<div align="center">

### 📚 **Complete Project Documentation**

[![View Presentation](https://img.shields.io/badge/View_on-Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white)](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit?utm_content=DAF-kSKhMmM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

**Includes:** Architecture diagrams • Workflow visualization • Technical implementation • Challenges & solutions • Future roadmap

</div>

---

## ✨ Key Features

<div align="center">

| 🧠 NLP Processing | 📚 PubMed Integration | 🤖 LLM Augmentation |
|:---:|:---:|:---:|
| Understands natural language medical queries | Searches up-to-date medical literature | Synthesizes research using Mistral-7B |

| 🔍 Smart Keywords | 📖 Evidence-Based | 🎨 User-Friendly |
|:---:|:---:|:---:|
| Auto-generates optimized search terms | Grounds responses in actual research | Seamless Gradio web interface |

</div>

### 🌟 **Core Capabilities**

```
✓ Natural Language Processing - Understands medical terminology and context
✓ PubMed Integration - Real-time access to 35+ million citations
✓ Intelligent Keyword Generation - Optimizes queries for PubMed search
✓ LLM Synthesis - Mistral-7B-Instruct for coherent answer generation
✓ Transparent Sourcing - Clear attribution to PubMed vs general knowledge
✓ Evidence-Based Responses - Backed by peer-reviewed research
```

---

## 🏗️ System Architecture

<div align="center">

```ascii
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐     ┌──────────┐
│    User     │────▶│   Keyword    │────▶│   PubMed    │────▶│   Answer     │────▶│ Response │
│  Question   │     │  Generation  │     │   Search    │     │  Synthesis   │     │ (Sources)│
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘     └──────────┘
                          │                     │                    │
                    Mistral-7B            PubMed API          Mistral-7B
                    (Keyword LLM)          via PyMed          (Answer LLM)
```

</div>

### 📦 **Component Breakdown**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Keyword Generator** | Mistral-7B-Instruct | Converts questions to PubMed search terms |
| **PubMed Fetcher** | PyMed API | Retrieves relevant medical articles |
| **Answer Synthesizer** | Mistral-7B-Instruct | Generates coherent, evidence-based answers |
| **Pipeline Orchestrator** | Haystack 2.0 | Connects all components seamlessly |
| **User Interface** | Gradio | Web-based chat interface |

> 💡 **For detailed architecture diagrams:** See the [Project Presentation](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit?utm_content=DAF-kSKhMmM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## 🚀 Quick Start

### 📋 **Prerequisites**

```yaml
Required:
  - Python 3.8+
  - Hugging Face account (free)
  - Internet connection

Optional:
  - PubMed email (for higher rate limits)
```

### ⚙️ **Installation**

#### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/Saunakghosh10/healthcare-searchtool.git
cd healthcare-searchtool
```

#### 2️⃣ **Create Virtual Environment**

<table>
<tr>
<th>Windows</th>
<th>Mac/Linux</th>
</tr>
<tr>
<td>

```bash
python -m venv venv
venv\Scripts\activate
```

</td>
<td>

```bash
python3 -m venv venv
source venv/bin/activate
```

</td>
</tr>
</table>

#### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

#### 4️⃣ **Configure API Keys**

Create a `.env` file in the root directory:

```env
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
PUBMED_EMAIL=your_email@domain.com  # Optional but recommended
```

> 🔑 **Get your Hugging Face API key:** [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

#### 5️⃣ **Launch the Application**

```bash
python app.py
```

#### 6️⃣ **Access the Interface**

```
🌐 Open your browser: http://localhost:7860
```

---

## 🎥 Demo & Presentation

<div align="center">

| 🖥️ Interactive Demo | 📊 Full Presentation |
|:-------------------:|:--------------------:|
| Access at `localhost:7860` | [View on Canva](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit) |
| Try live queries after installation | Complete project overview |

</div>

### 📚 **Presentation Contents**

```
├── Project Motivation & Objectives
├── System Architecture & Design
├── Technical Implementation Details
├── Performance Metrics & Validation
├── Challenges & Solutions
└── Future Roadmap & Enhancements
```

---

## 🧪 Example Questions

### Try These Queries:

<details>
<summary><b>🔬 Cancer Research</b></summary>

```
How are mRNA vaccines being used for cancer treatment?
What are the latest immunotherapy approaches for melanoma?
```
</details>

<details>
<summary><b>🧠 Neurology</b></summary>

```
What are the latest treatments for Alzheimer's disease?
How does deep brain stimulation work for Parkinson's?
```
</details>

<details>
<summary><b>💚 Mental Health</b></summary>

```
Tell me about the relationship between gut microbiome and mental health.
What are effective treatments for treatment-resistant depression?
```
</details>

<details>
<summary><b>⚕️ Chronic Conditions</b></summary>

```
What are effective non-pharmacological treatments for chronic pain?
How can lifestyle modifications help manage hypertension?
```
</details>

<details>
<summary><b>🍎 Metabolic Health</b></summary>

```
How does intermittent fasting affect metabolic health?
What is the connection between sleep and diabetes management?
```
</details>

<details>
<summary><b>🛡️ Preventive Medicine</b></summary>

```
What are the risk factors for developing type 2 diabetes?
How effective are various COVID-19 vaccine platforms?
```
</details>

> 📖 **More examples and detailed use cases** in the [project presentation](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit)

---

## 🛠️ Technical Details

### 🧩 **Core Components**

```python
┌─────────────────────────────────────────────────────────┐
│ 1. PubMedFetcher (Custom Haystack Component)           │
│    → Queries PubMed API                                 │
│    → Returns standardized documents                     │
├─────────────────────────────────────────────────────────┤
│ 2. Keyword Generator (Mistral-7B-Instruct)              │
│    → Converts natural questions to search terms         │
│    → Optimized for PubMed query syntax                  │
├─────────────────────────────────────────────────────────┤
│ 3. Answer Generator (Mistral-7B-Instruct)               │
│    → Synthesizes PubMed articles                        │
│    → Generates coherent, evidence-based answers         │
├─────────────────────────────────────────────────────────┤
│ 4. Prompt Builders (Jinja2 Templates)                   │
│    → Structured prompt engineering                      │
│    → Customizable templates                             │
├─────────────────────────────────────────────────────────┤
│ 5. Pipeline Orchestrator (Haystack)                     │
│    → Connects all components                            │
│    → Manages data flow                                  │
└─────────────────────────────────────────────────────────┘
```

> 📊 **Detailed component breakdown** available in the presentation slides

### 🤖 **Models Used**

#### **Primary Model**

```yaml
Model: mistralai/Mistral-7B-Instruct-v0.2

Specifications:
  Parameters: 7 billion
  Type: Instruction-tuned
  Context Window: 32,000 tokens
  Specialization: Medical terminology understanding
  
Performance:
  Response Quality: High
  Speed: Fast inference
  Accuracy: Optimized for Q&A
```

#### **Alternative Models** (configurable in `config.json`)

<table>
<tr>
<th>Model</th>
<th>Parameters</th>
<th>Best For</th>
</tr>
<tr>
<td>mistralai/Mixtral-8x7B-Instruct-v0.1</td>
<td>8x7B (MoE)</td>
<td>Complex queries, higher accuracy</td>
</tr>
<tr>
<td>tiiuae/falcon-7b-instruct</td>
<td>7B</td>
<td>Alternative 7B option</td>
</tr>
<tr>
<td>google/flan-t5-base</td>
<td>250M</td>
<td>Faster responses, lower accuracy</td>
</tr>
</table>

### ⚙️ **Configuration**

The system is configurable through:

| File | Purpose |
|------|---------|
| `.env` | API keys and email settings |
| `config.json` | Model selection, PubMed settings, generation parameters |
| Prompt templates | Custom prompt engineering for different use cases |

---

## 📊 Performance Metrics

<div align="center">

| Metric | Value | Notes |
|--------|-------|-------|
| ⏱️ **Average Response Time** | 10-15 seconds | End-to-end processing |
| 🎯 **Search Relevance** | ~85% precision | PubMed results accuracy |
| ✅ **Answer Accuracy** | ~82% | Against medical reference validation |
| 💬 **Token Usage** | 600-800 tokens/query | Per complete interaction |
| 📚 **Coverage** | All PubMed topics | 35+ million citations accessible |

</div>

> 📈 **Complete performance analysis and validation** details in the [presentation](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit)

---

## 🔧 Customization

### 🔄 **Changing Models**

Edit `config.json`:

```json
{
  "models": {
    "keyword_generator": "tiiuae/falcon-7b-instruct",
    "answer_generator": "mistralai/Mixtral-8x7B-Instruct-v0.1"
  }
}
```

### 🔍 **Adjusting Search Parameters**

Modify PubMed settings in `config.json`:

```json
{
  "pubmed": {
    "max_results": 3,    // Increase for more articles
    "timeout": 15        // Adjust for slow connections
  }
}
```

### ✏️ **Custom Prompt Engineering**

Edit templates in `app.py`:

```python
keyword_prompt_template = """
Your custom keyword generation prompt...
Question: {{question}}
"""

answer_prompt_template = """
Your custom answer generation prompt...
Context: {{documents}}
Question: {{question}}
"""
```

---

## ⚠️ Limitations & Disclaimer

### 🚨 **Important Limitations**

```diff
! NOT MEDICAL ADVICE
  This tool is for educational and research purposes ONLY

! INFORMATION CURRENCY
  PubMed coverage varies; some topics may have limited recent research

! MODEL BIASES
  LLMs may inherit biases from training data

! API DEPENDENCIES
  Requires stable internet and API availability

! RESPONSE VARIABILITY
  Answers may vary due to stochastic generation
```

### 🛡️ **Safety Features**

<table>
<tr>
<td>

✅ **Clear Disclaimers**  
Non-professional medical advice warnings

</td>
<td>

✅ **Fallback Mechanism**  
Uses general knowledge when PubMed lacks info

</td>
</tr>
<tr>
<td>

✅ **Source Attribution**  
Transparent citation of information sources

</td>
<td>

✅ **Response Limiting**  
Prevents information overload

</td>
</tr>
</table>

---

## 🎯 Use Cases

### 👥 **Target Users**

| User Type | Primary Use | Benefits |
|-----------|-------------|----------|
| 🎓 **Medical Students** | Quick research & literature reviews | Saves hours of manual searching |
| 👨‍⚕️ **Healthcare Professionals** | Staying updated with latest research | Access to current evidence |
| 🔬 **Researchers** | Identifying relevant papers & trends | Accelerates literature review |
| 🤒 **Patients** | Understanding medical conditions* | Empowered decision-making |
| 👨‍🏫 **Educators** | Teaching with current references | Up-to-date medical education |

*\*Always consult healthcare professionals for medical decisions*

> 📋 **Complete user personas and scenarios** in the [project presentation](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit)

---

## 📈 Future Enhancements

### 🔮 **Planned Features**

- [ ] **Conversation Memory** - Support for follow-up questions
- [ ] **Multi-language Support** - Beyond English queries
- [ ] **Citation Links** - Direct links to PubMed articles
- [ ] **Advanced Filtering** - By publication date, study type, etc.
- [ ] **Export Functionality** - Save answers as PDF/Word documents
- [ ] **Mobile App** - iOS and Android applications
- [ ] **Voice Interface** - Voice-based queries and responses
- [ ] **Collaborative Features** - Share and discuss findings

> 🗺️ **Complete roadmap and timeline** detailed in the [presentation](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit)

---

## 🤝 Contributing

Contributions are **welcome**! Help us make BioInquire-1 even better.

### 📝 **How to Contribute**

```bash
1. Fork the repository
2. Create feature branch:    git checkout -b feature/AmazingFeature
3. Commit your changes:      git commit -m 'Add AmazingFeature'
4. Push to branch:           git push origin feature/AmazingFeature
5. Open a Pull Request
```

### 🎯 **Areas for Contribution**

<table>
<tr>
<td>

- 🔗 Additional medical databases integration
- 🎨 Improved prompt engineering
- 🛠️ Enhanced error handling

</td>
<td>

- 🌍 Additional language support
- ⚡ Performance optimizations
- 📱 Mobile app development

</td>
</tr>
</table>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

<div align="center">

Special thanks to the teams and organizations that made this possible:

**📚 PubMed** - Access to biomedical literature  
**🤗 Hugging Face** - Hosting language models  
**🔧 Haystack** - NLP framework foundation  
**🎨 Gradio** - User interface framework  
**🤖 Mistral AI** - Powerful language models

</div>

---

## 📞 Support & Contact

<div align="center">

### Need Help? We're Here!

| 📋 Issues | ✉️ Email | 📖 Documentation |
|:---------:|:--------:|:----------------:|
| [GitHub Issues](../../issues) | healthcare.chatbot@gmail.com | [Project Presentation](https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit) |

</div>

**For bug reports or feature requests:**
1. Check existing [Issues](../../issues)
2. Create new issue with detailed description
3. Include error logs if applicable

---

## 📚 Additional Resources

<table>
<tr>
<td align="center">

📊 **Project Presentation**  
[Canva Slides]([https://www.canva.com/design/DAF-kSKhMmM/wtGEH-f01isdV-sUVJIryg/edit](https://www.canva.com/design/DAF-kSKhMmM/OBKy10EcvbKHR7F6WD9mZg/view?utm_content=DAF-kSKhMmM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h6670f550e5))

</td>
<td align="center">

🎥 **Demo Video**  
[[Add your demo link](https://www.canva.com/design/DAF-kSKhMmM/OBKy10EcvbKHR7F6WD9mZg/view?utm_content=DAF-kSKhMmM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h6670f550e5)]

</td>
</tr>
<tr>
<td align="center">

📖 **Technical Documentation**  
[Add your docs link]

</td>
<td align="center">

---

<div align="center">

## ⚕️ Medical Disclaimer

**This application is intended for research and educational purposes only.**

It is **NOT a substitute** for professional medical advice, diagnosis, or treatment.  
Always seek the advice of your physician or other qualified health provider  
with any questions you may have regarding a medical condition.

---

### Made with ❤️ for the medical research community

⭐ **If you find this project useful, please consider giving it a star!**

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Saunakghosh10.healthcare-searchtool)

</div>
