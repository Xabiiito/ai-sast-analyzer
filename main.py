import pathlib
import ollama
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown

def analizar_proyecto():
    # Directorio actual donde está el script
    directorio_actual = pathlib.Path(".")
    
    # Buscamos todos los archivos .py (excluyendo el propio main.py y carpetas como venv)
    archivos_python = [
        f for f in directorio_actual.glob("*.py") 
        if f.name != "main.py" and "venv" not in f.parts
    ]
    
    if not archivos_python:
        print("[bold red]✖ Error:[/bold red] No se encontraron archivos Python para analizar en este directorio.")
        return

    print(f"[bold cyan]>[/bold cyan] Se han encontrado [bold green]{len(archivos_python)}[/bold green] archivo(s) para auditar.\n")
    
    # Cabecera para el informe global en Markdown
    informe_global = "# 🛡️ Informe Global de Auditoría SAST\n\n"
    informe_global += "Herramienta de Análisis Estático impulsada por IA Local (Ollama + Mistral).\n\n---\n\n"

    for archivo in archivos_python:
        print(f"[yellow]🤖 Analizando archivo: {archivo.name}...[/yellow]")
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                codigo_a_analizar = f.read()
        except Exception as e:
            print(f"[red]No se pudo leer el archivo {archivo.name}: {e}[/red]")
            continue

        prompt = f"""
        Eres un auditor de ciberseguridad experto en SAST. Analiza exhaustivamente el siguiente código fuente en busca de TODAS las vulnerabilidades posibles (Inyección SQL, credenciales/secretos hardcodeados, ejecución de comandos inseguros, etc.).
        
        Archivo afectado: {archivo.name}
        Código a analizar:
        {codigo_a_analizar}

        Genera un informe estructurado que desglose:
        1. Listado de vulnerabilidades encontradas (nombre y nivel de riesgo: Alto/Medio/Bajo).
        2. Ubicación aproximada (línea o fragmento afectado).
        3. Explicación del riesgo y propuesta de código corregido para cada una.
        """

        try:
            response = ollama.chat(model='mistral', messages=[
                {'role': 'user', 'content': prompt}
            ])
            analisis_ia = response['message']['content']
            
            # Agregamos los resultados al informe global
            informe_global += f"## 📂 Archivo: `{archivo.name}`\n\n"
            informe_global += analisis_ia + "\n\n---\n\n"
            
        except Exception as e:
            print(f"[bold red]✖ Error al conectar con Ollama para el archivo {archivo.name}:[/bold red] {e}")

    # Guardamos el informe en un archivo físico de Markdown
    nombre_archivo_salida = "informe_sast.md"
    with open(nombre_archivo_salida, "w", encoding="utf-8") as f_out:
        f_out.write(informe_global)
        
    print(f"\n[bold green]✔ ¡Auditoría completada con éxito![/bold green]")
    print(f"[cyan]💾 Informe guardado en el archivo: {nombre_archivo_salida}[/cyan]\n")

    # Mostramos un resumen formateado en la terminal
    print(Panel(Markdown(informe_global), title="[bold red]🛡️ Vista Previa del Informe SAST[/bold red]", expand=False))

if __name__ == '__main__':
    analizar_proyecto()