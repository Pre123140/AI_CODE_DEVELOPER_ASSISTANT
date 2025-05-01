# src/code_assistant_agent.py

import os
import re
import ast
import builtins
import tempfile

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

BUILTIN_NAMES = set(dir(builtins))

def detect_common_bugs(code_text):
    """
    Detect common bugs or bad practices (enhanced logic).
    Returns a list of detected issues.
    """
    bugs = []

    # 1. Division by zero
    if re.search(r'/\s*0', code_text):
        bugs.append("⚠️ Possible division by zero detected.")

    # 2. Undefined variable usage via AST
    try:
        tree = ast.parse(code_text)
        defined_vars = set()
        function_defs = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_defs.add(node.name)
                for arg in node.args.args:
                    defined_vars.add(arg.arg)

            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        defined_vars.add(target.id)

            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                if (
                    node.id not in defined_vars
                    and node.id not in BUILTIN_NAMES
                    and node.id not in function_defs
                ):
                    bugs.append(f"⚠️ Variable '{node.id}' might be used before assignment.")

    except SyntaxError as e:
        bugs.append(f"❌ Syntax Error: {e}")

    # 3. Hardcoded credentials (simulated detection)
    if re.search(r'(password|pwd)\s*=\s*[\"\']', code_text, re.IGNORECASE):
        bugs.append("🔐 Hardcoded password or credentials found.")

    return list(set(bugs))  # Remove duplicates

def analyze_and_debug_code(file_path):
    """
    Analyze a Python file and return debug recommendations.
    """
    if not os.path.exists(file_path):
        return [f"❌ File not found: {file_path}"]

    with open(file_path, "r", encoding="utf-8") as f:
        code_text = f.read()

    bug_report = detect_common_bugs(code_text)

    # Save report
    report_path = os.path.join(REPORTS_DIR, os.path.basename(file_path).replace(".py", "_debug_report.txt"))
    with open(report_path, "w", encoding="utf-8") as f:
        if bug_report:
            f.write("\n".join(bug_report))
        else:
            f.write("✅ No obvious bugs found!")

    print(f"✅ Debug report saved to: {report_path}")
    return bug_report

def analyze_code_from_string(code_string):
    """
    Helper for analyzing inline code (from UI input).
    """
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w", encoding="utf-8") as tmp:
        tmp.write(code_string)
        tmp_path = tmp.name

    print(f"🧪 Temp file created for inline analysis: {tmp_path}")
    return analyze_and_debug_code(tmp_path)

# ✅ For Testing:
if __name__ == "__main__":
    test_code = """
def find_duplicates(items):
    duplicates = []
    for item in items:
        if items.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates
"""
    print("\n🐞 Running Debugger on Inline Code Sample...\n")
    results = analyze_code_from_string(test_code)
    for r in results:
        print(r)
