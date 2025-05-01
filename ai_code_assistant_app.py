# ai_code_assistant_app.py – Streamlit UI with Chat Memory (Only for General Chat Mode)

import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain, LLMChain
from langchain_community.llms import GPT4All
from langchain.prompts import PromptTemplate
from prompt_templates import get_prompt_template
import os
import datetime

# Path to GGUF model
MODEL_PATH = r"D:/PERSONAL/PORTFOLIO/TECHNICAL PROJECTS/CODE_DEVELOPER_ASSISTANT/AI_Code_Developer_Assistant/models/mistral-7b-openorca.Q4_K_M.gguf"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file not found at: {MODEL_PATH}")

# Load LLM
llm = GPT4All(model=MODEL_PATH, backend="llama", verbose=True)

# Initialize memory only for general chat
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

st.set_page_config(page_title="🧠 AI Code Chat Agent", layout="wide")
st.title("🧠 AI Code Assistant – Hybrid Mode")

st.markdown("Chat with the AI assistant. Paste code, upload a file, or choose a specific mode to get help.")

uploaded_file = st.file_uploader("📁 Upload a Python file", type=["py"])
user_input = st.text_area("💬 Or paste your code/message below:", height=200)
mode = st.selectbox("🧠 Choose Action", ["general chat", "explain", "fix", "optimize"])

# Load code from uploaded file if exists
if uploaded_file is not None:
    user_input = uploaded_file.read().decode("utf-8")

if st.button("🧠 Run AI Assistant"):
    if user_input:
        with st.spinner("Thinking..."):
            if mode == "general chat":
                chat_chain = ConversationChain(llm=llm, memory=st.session_state.memory, verbose=True)
                response = chat_chain.run(user_input)
            else:
                prompt_template = PromptTemplate(template=get_prompt_template(mode), input_variables=["code"])
                chain = LLMChain(llm=llm, prompt=prompt_template)
                response = chain.run({"code": user_input})

            st.session_state.chat_history = st.session_state.get("chat_history", [])
            st.session_state.chat_history.append((user_input, response))
            st.subheader("🧠 AI Response")
            st.code(response, language="markdown")

            # Download response button
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ai_response_{mode}_{timestamp}.txt"
            st.download_button(
                label="💾 Download AI Response",
                data=response,
                file_name=filename,
                mime="text/plain"
            )
    else:
        st.warning("Please enter a message or upload a file.")

# Display history
if "chat_history" in st.session_state:
    st.markdown("---")
    st.subheader("🗂️ Conversation History")
    for i, (q, a) in enumerate(reversed(st.session_state.chat_history), 1):
        with st.expander(f"🔹 Q{i}: {q[:50]}..."):
            st.markdown(f"**You:** {q}")
            st.markdown(f"**AI:** {a}")

st.markdown("---")
st.caption("Powered by LangChain + Mistral-7B — Chat memory active only for general conversations 🧠")
