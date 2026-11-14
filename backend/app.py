"""
NutriCampus Flask Application
Course: 25CPD37 - Community Project using Innovation and Design Thinking
Department of Computer Science and Engineering, New Horizon College of Engineering

Compatible with local execution and Vercel serverless deployment.
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_folder=".", static_url_path="")

# On Vercel serverless environment, the root filesystem is read-only; use /tmp for SQLite
DB_FILE = "/tmp/health_nutrition.db" if os.environ.get("VERCEL") else os.path.join(os.path.dirname(os.path.abspath(__file__)), "health_nutrition.db")


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
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
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS water_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_date TEXT,
                amount_ml INTEGER,
                log_time TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/<path:path>")
def static_files(path):
    if os.path.exists(path):
        return send_from_directory(".", path)
    return send_from_directory(".", "index.html")


@app.route("/api/feedback", methods=["GET"])
def get_feedback():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedbacks ORDER BY id DESC")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return jsonify({"success": True, "feedbacks": rows})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/feedback", methods=["POST"])
def post_feedback():
    try:
        data = request.get_json() or {}
        name = data.get("name", "Student Tester")
        branch = data.get("branch", "CSE - 3rd Sem")
        nav_rating = int(data.get("navRating", 5))
        content_rating = int(data.get("contentRating", 5))
        tools_rating = int(data.get("toolsRating", 5))
        gain = data.get("gain", "Yes, significantly")
        comment = data.get("comment", "")

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO feedbacks (name, branch, nav_rating, content_rating, tools_rating, awareness_gain, comments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, branch, nav_rating, content_rating, tools_rating, gain, comment))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()

        return jsonify({"success": True, "id": new_id, "message": "Feedback recorded."}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


# Auto-initialize database on startup / serverless cold-start
try:
    init_db()
except Exception as e:
    print(f"DB init warning: {e}")

if __name__ == "__main__":
    print("Starting NutriCampus Flask Server at http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)
