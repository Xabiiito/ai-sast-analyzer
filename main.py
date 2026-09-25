import os
import ollama
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

# Directorio a escanear (por defecto la carpeta actual del proyecto)
TARGET_DIR = "."
OUTPUT_REPORT = "informe_sast.md"

def scan_file_with_ai(file_path, code_content):
    """Envía el contenido del archivo a Ollama (Mistral) para un análisis SAST profundo."""
    prompt = f"""
    Actúa como un Auditor de Ciberseguridad experto en OWASP Top 10. 
    Analiza el siguiente código fuente en Python en busca de vulnerabilidades de seguridad críticas.
    
    Busca específicamente:
    1. Inyección SQL (SQLi)
    2. Credenciales, contraseñas o claves de API hardcodeadas (Secrets)
    3. Ejecución de comandos del sistema inseguros (ej. os.system, subprocess sin validar)
    4. Deserialización insegura (ej. uso peligroso de pickle)
    5. Manipulación de rutas o Path Traversal (ej. open() con entradas de usuario sin sanitizar)

    Código a analizar ({file_path}):
    ```python
    {code_content}
    ```

    Proporciona un informe claro detallando:
    - Nombre de la vulnerabilidad encontrada.
    - Nivel de riesgo (Alto, Medio, Bajo).
    - Línea aproximada de código afectado.
    - Explicación del riesgo.
    - Solución propuesta para corregirlo.
    """

    try:
        response = ollama.chat(
            model='mistral',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error al conectar con Ollama: {e}"

def main():
    console.print(Panel.fit("🛡️ Iniciando Escáner SAST Avanzado (Ollama + Mistral)", style="bold cyan"))
    
    report_content = "# 📊 Informe Global de Auditoría SAST Avanzada\n\n"
    report_content += "Herramienta de Análisis Estático impulsada por IA Local con cobertura ampliada OWASP Top 10.\n\n---\n\n"

    scanned_files = 0

    # Recorrido recursivo por el directorio
    for root, _, files in os.walk(TARGET_DIR):
        # Ignorar la carpeta del entorno virtual y carpetas ocultas de git
        if "venv" in root or ".git" in root or "assets" in root:
            continue
            
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                console.print(f"\n[yellow]🔍 Analizando archivo:[/yellow] {file_path}")
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code_content = f.read()
                    
                    # Llamada a la IA
                    analysis = scan_file_with_ai(file_path, code_content)
                    
                    # Añadir al informe global
                    report_content += f"## 📁 Archivo: `{file_path}`\n\n"
                    report_content += analysis + "\n\n---\n\n"
                    scanned_files += 1

                except Exception as e:
                    console.print(f"[red]Error leyendo el archivo {file_path}: {e}[/red]")

    if scanned_files > 0:
        # Guardar el informe en formato Markdown
        with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
            f.write(report_content)

        console.print(f"\n[green]✅ ¡Escaneo completado! Se han analizado {scanned_files} archivo(s).[/green]")
        console.print(f"[green]📄 Informe generado con éxito en: {OUTPUT_REPORT}[/green]\n")

        # Mostrar una vista previa del informe en la terminal con Rich
        console.print(Panel(Markdown(report_content), title="[bold blue]Vista Previa del Informe SAST[/bold blue]", border_style="blue"))
    else:
        console.print("[yellow]⚠️ No se encontraron archivos de Python para analizar en el directorio.[/yellow]")

if __name__ == "__main__":
    main()