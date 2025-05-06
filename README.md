# 🧠 AI-Powered Code & Developer Assistant

A local GenAI-powered coding agent that helps you **analyze, debug, and optimize Python code** — with or without LLMs. Designed for developers, learners, and security-conscious teams, it uses `mistral-7b-openorca.Q4_K_M.gguf` to run completely offline.

---

## 🎯 Project Objective
To create a dual-mode code assistant that:
- Understands and explains code behavior line-by-line
- Automatically detects and fixes bugs in code
- Refactors and optimizes scripts for readability and performance
- Engages in contextual multi-turn conversations (Agent Mode)

---

## 🚀 Key Features
- **Explain Mode** – Understand any Python code snippet
- **Fix Mode** – Auto-debug common issues and broken logic
- **Optimize Mode** – Refactor for readability, performance, or PEP8
- **Agent Chat Mode** – LLM-powered, memory-aware conversations
- **Markdown Export** – Save results for learning or review
- **Local Execution** – No cloud, no OpenAI API — 100% offline

---

## 🧠 Conceptual Study
Want to dive deeper into how this works?
👉 [Read the Full Conceptual Study →](https://github.com/Pre123140/AI_CODE_DEVELOPER_ASSISTANT/blob/main/AI_CODE_DEVELOPER_ASSISTANT.pdf)

---

## 🛠️ Tech Stack
- `mistral-7b-openorca.Q4_K_M.gguf` via GPT4All
- `LangChain` with memory support
- `Streamlit` UI (dual apps)
- Python core: `ast`, `tempfile`, `markdown`, etc.


---

## 📁 Folder Structure
```
AI_Code_Developer_Assistant/
├── requirements.txt
├── models/
│   └── mistral-7b-openorca.Q4_K_M.gguf
├── data/
│   ├── example_buggy_code.py
│   ├── example_insecure_code.py
│   └── example_unoptimized_code.py
├── reports/
│   ├── *.csv, *.txt, *.py (auto-generated reports)
├── src/
│   ├── app.py                      # Rule-based version
│   ├── ai_code_assistant_app.py   # LLM-powered assistant
│   ├── code_analysis.py
│   ├── code_optimizer.py
│   ├── auto_debugger.py
│   ├── llm_agent.py
│   └── prompt_templates.py
```

---

## ⚙️ How to Run the Project
## ⚙️ How to Run the Project

### 1. 📂 Clone the Repository
```bash
git clone https://github.com/yourname/AI_Code_Developer_Assistant
cd AI_Code_Developer_Assistant
```

### 2. ✨ Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. ⚖️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🤖 Add Your LLM Model
Place `mistral-7b-openorca.Q4_K_M.gguf` in the `/models/` folder.

### 5. 🔹 Launch the App
```bash
streamlit run src/app.py                    # Static mode (no LLM)
streamlit run src/ai_code_assistant_app.py  # Agentic mode (LLM)
```


---



## ✨ Project Highlights
- **Local-First AI**: No internet required — privacy-preserving
- **Dual Mode**: Toggle between rule-based and LLM-powered analysis
- **Multi-Agent Ready**: Modular structure for extending capabilities
- **Developer-Friendly**: Markdown outputs, no API costs

---

## 📜 License

This project is open for educational use only. For commercial deployment, contact the author.

---

## 📬 Contact
If you'd like to learn more or collaborate on projects or other initiatives, feel free to connect on [LinkedIn](https://www.linkedin.com/in/prerna-burande-99678a1bb/) or check out my [portfolio site](https://youtheleader.com/).

