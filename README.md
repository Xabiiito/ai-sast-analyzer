# 🛡️ AI-Powered Local SAST Security Analyzer

A lightweight and automated **Static Application Security Testing (SAST) Tool**, powered by a Local Language Model (**Ollama + Mistral**). Designed to scan Python source code for security vulnerabilities (OWASP Top 10 focus) while ensuring **absolute data privacy**, as all processing runs completely offline.

## 🚀 Key Features
- **OWASP Top 10 Focus:** Detects critical security flaws such as SQL Injection (SQLi), Hardcoded Secrets, Insecure Command Execution, Insecure Deserialization, and Path Traversal.
- **Automated Reporting:** Generates a structured markdown security audit report (`sast_report.md`).
- **Interactive Terminal UI:** Clean and professional output rendering using the `rich` library.
- **100% Local & Private:** No source code leaves your local environment.

## 🛠️ Built With
- **Python 3.11**
- **Ollama** (Local *Mistral* model)
- **Rich** (Terminal UI and Markdown rendering)

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Xabiiito/ai-sast-analyzer.git](https://github.com/Xabiiito/ai-sast-analyzer.git)
   cd ai-sast-analyzer