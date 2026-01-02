import re

SQL_KEYWORDS = ["SELECT", "INSERT", "UPDATE", "DELETE"]


def scan_file(file_path):
    findings = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return findings

    for line_no, line in enumerate(lines, start=1):
        upper_line = line.upper()

        if any(keyword in upper_line for keyword in SQL_KEYWORDS):
            if is_unsafe_sql(line):
                findings.append({
                    "file": file_path,
                    "line": line_no,
                    "code": line.strip(),
                    "severity": "HIGH",
                    "issue": "Potential SQL Injection (Non-parameterized query)"
                })

    return findings


def is_unsafe_sql(line):
    # string concatenation
    if "+" in line:
        return True

    # f-strings
    if re.search(r"f\".*\{.*\}.*\"", line):
        return True

    # format strings
    if ".format(" in line:
        return True

    return False
