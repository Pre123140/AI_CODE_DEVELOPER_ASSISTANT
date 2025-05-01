# src/llm_agent.py

from langchain_community.llms import GPT4All
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from prompt_templates import get_prompt_template

# ✅ Updated path for GGUF model
MODEL_PATH = r"D:/PERSONAL/PORTFOLIO/TECHNICAL PROJECTS/CODE_DEVELOPER_ASSISTANT/AI_Code_Developer_Assistant/models/mistral-7b-openorca.Q4_K_M.gguf"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file not found at: {MODEL_PATH}")

# ✅ Use "llama" backend for GGUF
llm = GPT4All(model=MODEL_PATH, backend="llama", verbose=True)

def run_code_agent(code_input: str, mode: str = "explain") -> str:
    prompt_template = PromptTemplate(
        template=get_prompt_template(mode),
        input_variables=["code"]
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run({"code": code_input})
    return response.strip()

if __name__ == "__main__":
    test_code = '''
def greet(name):
    print("Hello " + name)
greet("Alice")
'''
    result = run_code_agent(test_code, mode="explain")
    print("🧠 AI Assistant Response:\n", result)
