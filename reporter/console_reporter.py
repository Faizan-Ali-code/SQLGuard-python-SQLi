def report_findings(findings):
    if not findings:
        print(" No potential SQL Injection issues found.")
        return

    print("\n Potential SQL Injection Issues Detected:\n")

    for idx, f in enumerate(findings, start=1):
        print(f"{idx}. [{f['severity']}] {f['issue']}")
        print(f"   File: {f['file']}")
        print(f"   Line: {f['line']}")
        print(f"   Code: {f['code']}\n")
