
# 🧠 AI-Powered Code & Developer Agent

A local GenAI-powered code assistant that helps you **explain, debug, and optimize Python code** — with or without LLMs. Built using Mistral-7B (GGUF), LangChain, and Streamlit, it runs entirely offline with two modes:

### 🚀 Key Features

- **Explain Mode** – Understand logic line-by-line
- **Fix Mode** – Auto-debug code errors and improve logic
- **Optimize Mode** – Refactor for better performance/readability
- **Chat Mode** – Multi-turn AI tutor with memory
- **File Upload + Markdown Export**
- **Runs 100% Locally – No API, No Cloud**

---

### 🛠️ Tech Stack

- `Mistral-7B` (GGUF - Q4_K_M)
- `LangChain` + `ConversationBufferMemory`
- `GPT4All` local LLM runtime
- `Streamlit` UI
- Python core tools (`ast`, `tempfile`, `os`, etc.)

---

### 📂 Dual Modes

| Mode | File | Description |
|------|------|-------------|
| `app.py` | 🔧 Static App | Rule-based, no LLMs, fast code analysis |
| `ai_code_assistant_app.py` | 🧠 Agentic App | LLM-based with Mistral-7B, chat-style memory |

---

### 📦 Folder Structure
AI_Code_Developer_Assistant/
├── requirements.txt

├── models/
│   └── mistral-7b-openorca.Q4_K_M.gguf

├── data/
│   ├── example_buggy_code.py
│   ├── example_insecure_code.py
│   └── example_unoptimized_code.py

├── reports/
│   ├── example_buggy_code_analysis.csv
│   ├── example_buggy_code_debug_report.txt
│   ├── example_insecure_code_analysis.csv
│   ├── example_unoptimized_code_analysis.csv
│   ├── example_unoptimized_code_optimized.py
│   ├── inline_opt_temp_optimized.py
│   ├── inline_struct_temp_analysis.csv
│   ├── tmp6gnz615m_debug_report.txt
│   ├── tmp331y4se3_debug_report.txt
│   ├── tmpi9p_hsnn_debug_report.txt
│   └── tmpxkdqb3ti_debug_report.txt

├── src/
│   ├── app.py
│   ├── ai_code_assistant_app.py
│   ├── auto_debugger.py
│   ├── code_analysis.py
│   ├── code_optimizer.py
│   ├── llm_agent.py
│   └── prompt_templates.py

└── README.md



### ⚙️ How to Run

1. Clone this repo and create a virtual environment.
2. Download Mistral model (`mistral-7b-openorca.Q4_K_M.gguf`) and place it in `/models`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt


Run either app:
Static: streamlit run app.py
Agent: streamlit run ai_code_assistant_app.py



Project Highlights
Local-first AI — ideal for secure or educational environments.
No OpenAI or paid API required.
Designed for learners, freelancers, educators, and AI engineers.
Modular — extendable to other languages or multi-agent systems.


Conceptual Study
Read the full deep-dive behind this project: Conceptual Study →

 Author
Prerna Burande
AI | Strategy | Portfolio Engineering


📄 License
MIT — for personal/educational use only. Contact for commercial licensing.

---

