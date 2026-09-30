import pickle
import os
import sqlite3

# 1. Vulnerability: Hardcoded secrets
API_KEY = "sk-live-secret-token-123456789"
DATABASE_PASSWORD = "SuperSecretPassword123!"

def unsafe_query(user_input):
    # 2. Vulnerability: SQL Injection (SQLi)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_file_read(filename):
    # 3. Vulnerability: Path Traversal
    filepath = os.path.join("/var/www/uploads/", filename)
    with open(filepath, "r") as f:
        return f.read()

def unsafe_deserialization(serialized_data):
    # 4. Vulnerability: Insecure Deserialization (Pickle)
    return pickle.loads(serialized_data)
