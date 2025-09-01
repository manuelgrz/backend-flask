from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT name, email FROM users WHERE email=? AND password=?", (email, password))
    user = cur.fetchone()
    conn.close()

    if user:
        return jsonify({"success": True, "name": user["name"], "email": user["email"]})
    return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"})

@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Usuario registrado correctamente"})
    except sqlite3.IntegrityError:
        return jsonify({"success": False, "message": "El correo ya está registrado"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Railway da el puerto en variable PORT
    app.run(host="0.0.0.0", port=port)
