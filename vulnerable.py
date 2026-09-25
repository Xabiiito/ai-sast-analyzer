import sqlite3
import os

# ⚠️ VULNERABILIDAD 1: Credenciales y Claves API hardcodeadas
API_KEY = "sk-live-secret-987654321abcdef"
DATABASE_PASSWORD = "SuperSecretAdminPassword2026"

def buscar_usuario(nombre_usuario):
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()
    
    # ⚠️ VULNERABILIDAD 2: Inyección SQL directa
    query = f"SELECT * FROM usuarios WHERE username = '{nombre_usuario}'"
    cursor.execute(query)
    
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def ejecutar_mantenimiento(parametro_externo):
    # ⚠️ VULNERABILIDAD 3: Ejecución de comandos insegura / Command Injection
    os.system(f"echo Limpiando logs para {parametro_externo}")
