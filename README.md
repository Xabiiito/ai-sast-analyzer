# 🛡️ AI-Powered Local SAST Analyzer

Una herramienta de **Análisis Estático de Código (SAST)** ligera y automatizada, impulsada por un Modelo de Lenguaje Local (**Ollama + Mistral**). Diseñada para detectar vulnerabilidades de seguridad (OWASP Top 10) garantizando la **privacidad absoluta de los datos**, ya que todo el procesamiento se ejecuta 100% en local.

## 🚀 Características Principales
- **Multivulnerabilidad:** Detecta inyecciones SQL, credenciales/secretos hardcodeados y ejecución de comandos inseguros (`os.system`).
- **Escaneo Recursivo:** Analiza de forma automática todos los archivos de código fuente de un proyecto Python.
- **Informes Automatizados:** Genera un informe detallado estructurado en formato Markdown (`informe_sast.md`).
- **Interfaz Interactiva:** Visualización elegante de los resultados en la terminal utilizando la librería `rich`.

## 🛠️ Tecnologías Utilizadas
- **Python 3.11**
- **Ollama** (Modelo local *Mistral*)
- **Rich** (UI y renderizado Markdown en terminal)

## ⚙️ Instalación y Uso

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Xabiiito/ai-sast-analyzer.git
   cd ai-sast-analyzer