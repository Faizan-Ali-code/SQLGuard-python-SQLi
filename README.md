

# 🔐 SQLGuard
**A Static SQL Injection Detection Tool**

---

## 📌 Overview

**SQLGuard** is a lightweight, command-line static analysis tool designed to detect **potential SQL Injection risks** in Python source code by identifying unsafe SQL query construction patterns.

The tool focuses on detecting **non-parameterized queries**, **string concatenation**, and other risky coding practices that may lead to SQL injection vulnerabilities.

SQLGuard is intended as an **early-warning security tool**, not a replacement for manual review or dynamic testing.

---

## 🎯 Purpose

The purpose of SQLGuard is to:

- Identify potential SQL injection risks during development
- Assist developers and security testers in early vulnerability detection
- Promote secure coding practices
- Provide a simple, offline static analysis utility
- Support learning and research in application security

SQLGuard performs **heuristic-based static analysis** and reports **potential risks**, not guaranteed vulnerabilities.

---

## 🧠 Key Features

- Static analysis of Python source code
- Detection of non-parameterized SQL queries
- Identification of string concatenation, f-strings, and `.format()` usage in SQL
- File-level and line-level findings
- Clear severity and issue description
- Command-line interface (CLI)
- Windows double-click execution using a `.bat` file
- Modular and extendable project structure

---

## 📂 Project Structure

```

sqlguard/
│
├── cli.py
├── run_sqlguard.bat
│
├── scanner/
│   ├── file_loader.py
│   └── pattern_scanner.py
│
├── rules/
│   └── python_sql.json
│
├── reporter/
│   └── console_reporter.py
│
└── README.md

````

---

## ▶️ How to Run

### Option 1: Windows (Recommended)

1. Open the project folder
2. Double-click **`run_sqlguard.bat`**
3. Enter the path to the Python file or folder to scan

### Option 2: Command Line

```bash
cd sqlguard
python cli.py path/to/python/project
````

Example:

```bash
python cli.py ./test_app
```

---

## 🔍 What SQLGuard Detects

SQLGuard flags code that:

* Builds SQL queries using string concatenation
* Uses f-strings or `.format()` in SQL query construction
* Lacks parameterized query usage

### Example (Vulnerable Code)

```python
user_id = input("Enter ID: ")
query = "SELECT * FROM users WHERE id = " + user_id
cursor.execute(query)
```

---

## ⚠️ Disclaimer

SQLGuard performs **static heuristic analysis**.

Findings indicate **potential security risks** and do not guarantee exploitability.
Manual code review and dynamic testing are always recommended.

---

## ⚠️ Limitations

SQLGuard is intentionally designed as a **lightweight static analysis tool** and has the following limitations:

* It uses **pattern-based heuristics**, not full semantic or data-flow analysis.
* It does **not perform runtime analysis** or execute the code.
* It does **not detect SQL queries generated through ORMs** such as Django ORM or SQLAlchemy.
* It may produce **false positives**, especially in complex or dynamically constructed queries.
* Findings represent **potential risks**, not confirmed vulnerabilities.

SQLGuard is best used as an **early detection and awareness tool**, especially for legacy code, scripts, and beginner-written applications.

---

## 🚀 Future Enhancements

Planned improvements include:

* Rule-driven scanning using JSON-based rules
* Taint analysis (user input flow tracking)
* Support for additional languages (Java, PHP)
* JSON and HTML reporting formats
* CI/CD pipeline integration

---

## 📄 License

This project is intended for **educational and security research purposes only**.

---

## 🤝 Contributions

Contributions are welcome.

You may:

* Add new detection rules
* Improve detection accuracy
* Enhance reporting
* Extend language support

---

## 📬 Author

**Faizan Ali**

Developed as a cybersecurity tooling and application security research initiative.

---

### ✅ Final Note

SQLGuard is designed to promote **secure coding awareness** and **early vulnerability detection**, helping developers and learners identify risky SQL patterns before they reach production.


