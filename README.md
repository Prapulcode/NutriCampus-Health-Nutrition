# NutriCampus: Health & Nutrition Awareness Web Application

> **Course:** Community Project using Innovation and Design Thinking (25CPD37)  
> **Institution:** New Horizon College of Engineering, Bengaluru  
> **Department:** Department of Computer Science and Engineering  
> **Semester:** III (Sep 2026 – Dec 2026)

---

## 🌟 Overview & Objectives

NutriCampus is a student-centered health and nutrition awareness web application built to address the irregular meal habits, screen fatigue, and hydration gaps common among engineering and undergraduate students.

### Core Application Modules:
1. **Nutrition & Balanced Diet Guide**: Clear, relatable information on carbohydrates, proteins, healthy fats, vitamins, and minerals with Indian campus canteen/hostel food swaps.
2. **Interactive BMI Calculator**: Calculates BMI using metric or imperial units, features a dynamic visual gauge, and provides essential educational disclaimers clarifying that BMI is a screening ratio, not a medical diagnosis.
3. **Daily Water Intake Tracker**: Interactive animated liquid bottle with custom daily goals (2.0L – 3.5L), quick-add portions (+200ml, +250ml, +500ml, +150ml), consumption log history, and daily persistence.
4. **Nutrition & Wellness Quiz**: 7 high-yield questions addressing common college dietary myths with instant feedback and scientific explanations.
5. **Campus Healthy Habits**: Ergonomic 20-20-20 screen relief rules for computer labs, exam-period nutrition, late-night study snacks, and dorm stretches.
6. **Usability & Community Evaluation**: Form for college volunteer testers with 5-star ratings, real-time metric tallying, and peer reviews.

---

## 🚀 How to Run the Application

You can run NutriCampus using any of the following methods:

### Method 1: Instant Browser Launch (Zero Installation)
Simply double-click `index.html` or right-click and open with **Google Chrome**, **Mozilla Firefox**, or **Microsoft Edge**. All features, calculations, animations, and local data persistence work out-of-the-box!

### Method 2: Python Standard Library Server (Recommended for Demos)
Run the built-in zero-dependency server:
```bash
cd C:\Users\hi\.gemini\antigravity\scratch\health-nutrition-app
python backend/local_server.py
```
Open your browser to: **`http://localhost:5000`**  
- Automatically sets up a local SQLite database (`health_nutrition.db`)
- Provides live REST API endpoints (`/api/feedback`)

### Method 3: Flask Backend (Optional)
If your evaluators ask for Flask specifically:
```bash
cd C:\Users\hi\.gemini\antigravity\scratch\health-nutrition-app
pip install -r requirements.txt
python app.py
```
Open **`http://localhost:5000`**.

---

## 📁 Project Structure

```
health-nutrition-app/
├── index.html          # Main responsive single-page application
├── styles.css          # Modern CSS3 with dark/light themes, animations & print stylesheet
├── app.js              # Application logic (BMI, Water tracker, Quiz, Feedback, Storage)
├── public/             # index.html, app.js, styles.css (static front end)
├── backend/local_server.py  # Standard Python HTTP + SQLite REST API server (Zero dependency)
├── app.py              # Flask server + API (also the Vercel entrypoint)
├── requirements.txt    # Optional Flask dependencies
├── SYNOPSIS.md         # Formatted Markdown project synopsis
└── README.md           # Documentation and guide
```

---

## 💡 Key Features & Academic Value

- **Non-Diagnostic Health Screening**: Fully respects medical ethics by displaying clear disclaimers that the app provides educational awareness only.
- **Responsive UI**: Tested on both mobile screens and desktop monitors.
- **Local Persistence**: Stores water logs, dark/light theme preferences, and feedback ratings in browser `localStorage` and SQLite.
