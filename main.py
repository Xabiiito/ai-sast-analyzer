import os
import ollama
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

TARGET_DIR = "."
OUTPUT_REPORT = "sast_report.md"

def scan_code_with_ai(file_path, file_content):
    """Sends source code files to Ollama (Mistral) for security auditing against OWASP Top 10."""
    prompt = f"""
    Act as an expert Application Security Engineer and Senior SAST Auditor specialized in secure coding and the OWASP Top 10.
    Analyze the following source code file for security vulnerabilities, bad practices, and security flaws.
    
    Look specifically for:
    1. SQL Injection (SQLi) and other injection flaws.
    2. Hardcoded credentials, passwords, API keys, or sensitive secrets.
    3. Insecure system command executions (e.g., os.system, unsanitized subprocess).
    4. Insecure deserialization (e.g., unsafe use of pickle).
    5. Path Traversal and insecure file reads (e.g., open() with user-controlled inputs).

    File to analyze ({file_path}):
    ```python
    {file_content}
    ```

    Provide a detailed structured report including:
    - Name of the vulnerability or security flaw found.
    - Risk level (High, Medium, Low).
    - Affected line(s) of code.
    - Explanation of the security risk.
    - Solution or recommended secure coding practices to fix it.
    """

    try:
        response = ollama.chat(
            model='mistral',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error connecting to Ollama: {e}"

def main():
    console.print(Panel.fit("🛡️ Starting AI-Powered SAST Security Analyzer (Ollama + Mistral)", style="bold cyan"))
    
    report_content = "# 📊 Global SAST Security Audit Report\n\n"
    report_content += "Static Application Security Testing powered by Local AI.\n\n---\n\n"

    scanned_files = 0

    for root, _, files in os.walk(TARGET_DIR):
        if "venv" in root or ".git" in root or "assets" in root:
            continue
            
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                console.print(f"\n[yellow]🔍 Analyzing source code:[/yellow] {file_path}")
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        file_content = f.read()
                    
                    analysis = scan_code_with_ai(file_path, file_content)
                    
                    report_content += f"## 📄 Source File: `{file_path}`\n\n"
                    report_content += analysis + "\n\n---\n\n"
                    scanned_files += 1

                except Exception as e:
                    console.print(f"[red]Error reading file {file_path}: {e}[/red]")

    if scanned_files > 0:
        with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
            f.write(report_content)

        console.print(f"\n[green]✅ SAST audit completed! {scanned_files} file(s) analyzed.[/green]")
        console.print(f"[green]📄 Report successfully generated at: {OUTPUT_REPORT}[/green]\n")

        console.print(Panel(Markdown(report_content), title="[bold blue]SAST Report Preview[/bold blue]", border_style="blue"))
    else:
        console.print("[yellow]⚠️ No Python source files found in the directory.[/yellow]")

if __name__ == "__main__":
    main()