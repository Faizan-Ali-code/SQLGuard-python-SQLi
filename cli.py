import sys
from scanner.file_loader import load_python_files
from scanner.pattern_scanner import scan_file
from reporter.console_reporter import report_findings


def main():
    if len(sys.argv) != 2:
        print("Usage: python cli.py test_sql.py")
        sys.exit(1)

    target_path = sys.argv[1]

    python_files = load_python_files(target_path)
    all_findings = []

    for file_path in python_files:
        findings = scan_file(file_path)
        all_findings.extend(findings)

    report_findings(all_findings)


if __name__ == "__main__":
    main()
