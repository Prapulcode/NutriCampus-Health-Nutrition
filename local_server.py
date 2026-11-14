#!/usr/bin/env python3
"""
NutriCampus Server - Zero-Dependency HTTP & REST API Server
Course: 25CPD37 - Community Project using Innovation and Design Thinking
Department of Computer Science and Engineering, New Horizon College of Engineering

This server uses Python's built-in standard library (http.server and sqlite3).
No pip install or external virtualenv required!
"""

import http.server
import socketserver
import json
import sqlite3
import os
import sys
from urllib.parse import urlparse

PORT = 5000
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "health_nutrition.db")
STATIC_DIR = os.path.dirname(os.path.abspath(__file__))


def init_database():
    """Initializes SQLite database tables for feedback and water tracking."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Table for Usability Feedback (Objective 5 & Methodology Step 6)
    cursor.execute("""
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

    # Table for Water Tracker Logs (Objective 3)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_date TEXT,
            amount_ml INTEGER,
            log_time TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Pre-seed initial sample data if empty
    cursor.execute("SELECT COUNT(*) FROM feedbacks")
    if cursor.fetchone()[0] == 0:
        seed_data = [
            ("Rahul Verma (1NH25CS142)", "CSE - 3rd Sem", 5, 5, 5, "Yes, significantly", "The water bottle animation and campus canteen food swaps are super practical for hostel life!"),
            ("Sneha Rao (1NH25CS189)", "CSE - 3rd Sem", 5, 4, 5, "Yes, significantly", "Really liked that the BMI tool emphasizes that BMI is only a screening metric and not a medical diagnosis."),
            ("Aman Preet (1NH25CS034)", "CSE - 3rd Sem", 4, 5, 5, "Yes, significantly", "The 20-20-20 rule reminder in the habits section is very helpful during long programming lab sessions.")
        ]
        cursor.executemany("""
            INSERT INTO feedbacks (name, branch, nav_rating, content_rating, tools_rating, awareness_gain, comments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, seed_data)

    conn.commit()
    conn.close()
    print(f"[*] SQLite database initialized: {DB_FILE}")


class NutriRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler serving static files and JSON REST endpoints."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_GET(self):
        parsed = urlparse(self.path)

        # REST API: Fetch all feedbacks
        if parsed.path == "/api/feedback" or parsed.path == "/api/feedbacks":
            try:
                conn = sqlite3.connect(DB_FILE)
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, name, branch, nav_rating, content_rating, tools_rating, 
                           awareness_gain, comments, created_at 
                    FROM feedbacks ORDER BY id DESC
                """)
                rows = [dict(r) for r in cursor.fetchall()]
                conn.close()

                self._set_headers(200)
                self.wfile.write(json.dumps({"success": True, "feedbacks": rows}).encode("utf-8"))
                return
            except Exception as e:
                self._set_headers(500)
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
                return

        # REST API: Health Check
        elif parsed.path == "/api/health":
            self._set_headers(200)
            self.wfile.write(json.dumps({
                "status": "online",
                "project": "NutriCampus NHCE CSE",
                "course": "25CPD37"
            }).encode("utf-8"))
            return

        # Default static file serving (HTML, CSS, JS, Images)
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/feedback":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length).decode("utf-8")
                data = json.loads(body)

                name = data.get("name", "Student Tester")
                branch = data.get("branch", "CSE - 3rd Sem")
                nav_rating = int(data.get("navRating", 5))
                content_rating = int(data.get("contentRating", 5))
                tools_rating = int(data.get("toolsRating", 5))
                gain = data.get("gain", "Yes, significantly")
                comment = data.get("comment", "")

                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO feedbacks (name, branch, nav_rating, content_rating, tools_rating, awareness_gain, comments)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (name, branch, nav_rating, content_rating, tools_rating, gain, comment))
                conn.commit()
                new_id = cursor.lastrowid
                conn.close()

                self._set_headers(201)
                self.wfile.write(json.dumps({
                    "success": True,
                    "message": "Feedback successfully recorded in database.",
                    "id": new_id
                }).encode("utf-8"))
                return
            except Exception as e:
                self._set_headers(400)
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
                return

        self._set_headers(404)
        self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode("utf-8"))


def run():
    init_database()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), NutriRequestHandler) as httpd:
        print("=================================================================")
        print("   NutriCampus - Health & Nutrition Awareness Web App")
        print("   Course: 25CPD37 | Dept of CSE | NHCE")
        print("=================================================================")
        print(f"   🚀 Server running at: http://localhost:{PORT}")
        print(f"   📂 Static root: {STATIC_DIR}")
        print("   Press Ctrl+C to stop the server.")
        print("=================================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server cleanly. Good luck with your project evaluation!")
            httpd.server_close()


if __name__ == "__main__":
    run()
