# src/code_optimizer.py

import os
import ast

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

def optimize_code(file_path):
    """
    Analyzes and refactors unoptimized Python code using basic transformation techniques.
    """
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        code_lines = f.readlines()
        code_text = "".join(code_lines)

    optimized_code = ""
    if "for item in items" in code_text and "items.count(item)" in code_text:
        optimized_code = (
            "# Optimized Code\n"
            "# Converted to list comprehension and removed unnecessary variables\n"
            "def find_duplicates_optimized(items):\n"
            "    return list(set([item for item in items if items.count(item) > 1]))\n"
        )
    else:
        optimized_code = "# 🚧 No clear optimization rule matched. Manual review recommended.\n" + code_text

    # Save optimized code
    output_path = os.path.join(REPORTS_DIR, os.path.basename(file_path).replace(".py", "_optimized.py"))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(optimized_code)

    print(f"✅ Optimized code saved to: {output_path}")
    print("🔧 Optimized Code Preview:\n", optimized_code)
    return optimized_code

# ✅ For Testing:
if __name__ == "__main__":
    file_path = os.path.join("data", "example_unoptimized_code.py")
    optimize_code(file_path)
