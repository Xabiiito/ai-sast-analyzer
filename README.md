# 🛡️ AI-Powered Local SAST Security Analyzer

A lightweight and automated **Static Application Security Testing (SAST) Tool**, powered by a Local Language Model (**Ollama + Mistral**). Designed to scan Python source code for security vulnerabilities (OWASP Top 10 focus) while ensuring **absolute data privacy**, as all processing runs completely offline.

## 🚀 Key Features
- **OWASP Top 10 Focus:** Detects critical security flaws such as SQL Injection (SQLi), Hardcoded Secrets, Insecure Command Execution, Insecure Deserialization, and Path Traversal.
- **Automated Reporting:** Generates a structured markdown security audit report (\sast_report.md\).
- **Interactive Terminal UI:** Clean and professional output rendering using the \ich\ library.
- **100% Local & Private:** No source code leaves your local environment.

## 🛠️ Built With
- **Python 3.11**
- **Ollama** (Local *Mistral* model)
- **Rich** (Terminal UI and Markdown rendering)

## ⚙️ Installation & Usage

1. **Clone the repository:**
   \\\ash
   git clone https://github.com/Xabiiito/ai-sast-analyzer.git
   cd ai-sast-analyzer
   \\\

2. **Set up the virtual environment:**
   \\\ash
   python -m venv venv
   # On Windows (PowerShell):
   .\\venv\\Scripts\\Activate
   \\\

3. **Install dependencies:**
   \\\ash
   pip install ollama rich
   \\\

4. **Ensure Ollama is running and download the model:**
   \\\ash
   ollama pull mistral
   \\\

5. **Run the analyzer:**
   \\\ash
   python main.py
   \\\

## 📸 Preview
![SAST Analyzer Demo in Action](assets/demo.png)
