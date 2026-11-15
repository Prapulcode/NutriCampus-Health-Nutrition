"""
NutriCampus Flask Application (Vercel + local)
Course: 25CPD37 - Community Project using Innovation and Design Thinking
Department of Computer Science and Engineering, New Horizon College of Engineering

Layout:
  app.py          <- Flask app (Vercel auto-detects the `app` object here)
  public/         <- index.html, app.js, styles.css (served by Vercel's CDN)
  backend/        <- optional zero-dependency local server

Run locally:  pip install -r requirements.txt && python app.py
"""

import os
import sqlite3

from flask import Flask, jsonify, request, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

app = Flask(__name__, static_folder=None)

# Vercel's filesystem is read-only except /tmp. Data in /tmp is temporary
# (it resets on cold starts), which is fine for a demo feedback form.
ON_VERCEL = bool(os.environ.get("VERCEL"))
DB_FILE = "/tmp/health_nutrition.db" if ON_VERCEL else os.path.join(BASE_DIR, "health_nutrition.db")


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS feedbacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                branch TEXT,
                nav_rating INTEGER,
                content_rating INTEGER,
                tools_rating INTEGER,
                awareness_gain TEXT,
                comments TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS water_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_date TEXT,
                amount_ml INTEGER,
                log_time TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


# ---------- Static site (used locally; on Vercel, public/ is served by the CDN) ----------
@app.route("/")
def index():
    return send_from_directory(PUBLIC_DIR, "index.html")


@app.route("/<path:path>")
def static_files(path):
    if path.startswith("api/"):
        return jsonify({"success": False, "error": "Not found"}), 404
    if os.path.isfile(os.path.join(PUBLIC_DIR, path)):
        return send_from_directory(PUBLIC_DIR, path)
    return send_from_directory(PUBLIC_DIR, "index.html")


# ---------- API ----------
@app.route("/api/health")
def health():
    return jsonify({"success": True, "status": "ok"})


@app.route("/api/feedback", methods=["GET"])
@app.route("/api/feedbacks", methods=["GET"])
def get_feedback():
    try:
        init_db()
        conn = get_db()
        try:
            rows = [dict(r) for r in conn.execute("SELECT * FROM feedbacks ORDER BY id DESC")]
        finally:
            conn.close()
        return jsonify({"success": True, "feedbacks": rows})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/feedback", methods=["POST"])
def post_feedback():
    try:
        data = request.get_json(silent=True) or {}
        name = data.get("name", "Student Tester")
        branch = data.get("branch", "CSE - 3rd Sem")
        nav_rating = int(data.get("navRating", 5))
        content_rating = int(data.get("contentRating", 5))
        tools_rating = int(data.get("toolsRating", 5))
        gain = data.get("gain", "Yes, significantly")
        comment = data.get("comment", "")

        init_db()
        conn = get_db()
        try:
            cur = conn.execute(
                """
                INSERT INTO feedbacks (name, branch, nav_rating, content_rating, tools_rating, awareness_gain, comments)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (name, branch, nav_rating, content_rating, tools_rating, gain, comment),
            )
            conn.commit()
            new_id = cur.lastrowid
        finally:
            conn.close()
        return jsonify({"success": True, "id": new_id, "message": "Feedback recorded."}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    init_db()
    print("Starting NutriCampus at http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)
