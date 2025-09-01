import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Usuario de prueba
c.execute("INSERT OR IGNORE INTO users (name, email, password) VALUES (?, ?, ?)", 
          ("Juan", "juan@test.com", "1234"))

conn.commit()
conn.close()
print("✅ Base de datos inicializada con usuario de prueba.")
