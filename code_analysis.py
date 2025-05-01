# src/code_analysis.py

import ast
import os
import pandas as pd

def analyze_code_structure(code_text):
    """
    Analyze code structure using AST: count functions, classes, lines, etc.
    """
    try:
        tree = ast.parse(code_text)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        total_lines = len(code_text.splitlines())

        return {
            "num_functions": len(functions),
            "functions": functions,
            "num_classes": len(classes),
            "classes": classes,
            "total_lines": total_lines,
        }
    except SyntaxError as e:
        return {"error": f"Syntax Error: {e}"}

def analyze_code_file(file_path):
    """
    Load and analyze a Python file from the given path.
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    with open(file_path, "r", encoding="utf-8") as f:
        code_text = f.read()

    analysis = analyze_code_structure(code_text)

    # Save result to reports folder
    report_path = os.path.join("reports", os.path.basename(file_path).replace(".py", "_analysis.csv"))
    pd.DataFrame([analysis]).to_csv(report_path, index=False)
    print(f"✅ Code analysis saved to: {report_path}")

    return analysis

# ✅ For Testing:
if __name__ == "__main__":
    sample_files = [
        os.path.join("data", "example_buggy_code.py"),
        os.path.join("data", "example_insecure_code.py"),
        os.path.join("data", "example_unoptimized_code.py"),
    ]
    for file_path in sample_files:
        print(f"\n🔍 Analyzing {file_path}...")
        analysis = analyze_code_file(file_path)
        print(pd.DataFrame([analysis]))
