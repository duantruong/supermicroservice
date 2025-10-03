# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
from Connection import get_sql_connection  # uses your MySQL settings :contentReference[oaicite:0]{index=0}

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173","http://localhost:3000"], "supports_credentials": True}})

@app.post("/auth/login")
def login():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    if not email or not password:
        return jsonify({"ok": False, "error": "Missing email or password"}), 400

    conn = get_sql_connection()
    # if your get_sql_connection() returns strings on error, treat them as failures:
    if not hasattr(conn, "cursor"):
        return jsonify({"ok": False, "error": f"DB error: {conn}"}), 500

    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT idusers, email, password FROM users WHERE email=%s", (email,))
        row = cur.fetchone()
        if not row:
            return jsonify({"ok": False, "error": "Invalid credentials"}), 401

        if not bcrypt.checkpw(password.encode(), row["password"].encode()):
            return jsonify({"ok": False, "error": "Invalid credentials"}), 401

        # Keep it simple for now (no JWT). Signal success.
        return jsonify({"ok": True, "userId": row["id"]}), 200
    finally:
        try:
            cur.close(); conn.close()
        except Exception:
            pass

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
