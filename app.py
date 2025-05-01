# app.py – AI-Powered Code & Developer Assistant (Streamlit UI)

import streamlit as st
import os
from code_assistant_agent import analyze_code_from_string, analyze_and_debug_code
from code_analysis import analyze_code_file
from code_optimizer import optimize_code

st.set_page_config(page_title="AI Code Assistant", layout="wide")
st.title("🤖 AI-Powered Code & Developer Assistant")

TAB1, TAB2, TAB3 = st.tabs(["🐞 Debug Code", "📊 Code Structure", "⚙️ Optimize Code"])

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

with TAB1:
    st.header("🐛 Bug & Issue Detection")
    code_input = st.text_area("Paste your Python code here:", height=300)
    uploaded_file = st.file_uploader("...or upload a .py file", type=["py"], key="debug")

    if st.button("Run Debugger"):
        if code_input:
            results = analyze_code_from_string(code_input)
            st.subheader("🔎 Issues Found:")
            st.write(results)
        elif uploaded_file:
            with open(os.path.join("data", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.read())
            results = analyze_and_debug_code(os.path.join("data", uploaded_file.name))
            st.subheader("🔎 Issues Found:")
            st.write(results)
        else:
            st.warning("Please enter code or upload a file.")

with TAB2:
    st.header("📊 Structural Code Analysis")
    code_struct_input = st.text_area("Paste your Python code here for structure analysis:", height=300, key="struct_input")
    struct_file = st.file_uploader("...or upload a .py file", type=["py"], key="struct_upload")

    if st.button("Analyze Structure"):
        if code_struct_input:
            tmp_path = "data/inline_struct_temp.py"
            with open(tmp_path, "w", encoding="utf-8") as f:
                f.write(code_struct_input)
            summary = analyze_code_file(tmp_path)
            st.subheader("🧠 Code Summary:")
            st.json(summary)
        elif struct_file:
            file_path = os.path.join("data", struct_file.name)
            with open(file_path, "wb") as f:
                f.write(struct_file.read())
            summary = analyze_code_file(file_path)
            st.subheader("🧠 Code Summary:")
            st.json(summary)
        else:
            st.warning("Please enter code or upload a file.")

with TAB3:
    st.header("⚙️ Code Optimization")
    code_opt_input = st.text_area("Paste your Python code here for optimization:", height=300, key="opt_input")
    opt_file = st.file_uploader("...or upload a .py file", type=["py"], key="opt_upload")

    if st.button("Optimize Code"):
        if code_opt_input:
            tmp_path = "data/inline_opt_temp.py"
            with open(tmp_path, "w", encoding="utf-8") as f:
                f.write(code_opt_input)
            optimized_code = optimize_code(tmp_path)
            st.subheader("✨ Optimized Code")
            st.code(optimized_code or "No optimization applied.", language="python")
        elif opt_file:
            file_path = os.path.join("data", opt_file.name)
            with open(file_path, "wb") as f:
                f.write(opt_file.read())
            optimized_code = optimize_code(file_path)
            st.subheader("✨ Optimized Code")
            st.code(optimized_code or "No optimization applied.", language="python")
        else:
            st.warning("Please enter code or upload a file.")

st.markdown("---")
