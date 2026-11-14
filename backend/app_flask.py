"""
NutriCampus Flask Application Entrypoint
Course: 25CPD37 - Community Project using Innovation and Design Thinking
Department of Computer Science and Engineering, New Horizon College of Engineering
"""

from app import app, init_db

if __name__ == "__main__":
    init_db()
    print("Starting NutriCampus Flask Server at http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)
