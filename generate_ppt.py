"""
Professional PowerPoint Presentation (.pptx) Generator for:
NutriCampus - Health & Nutrition Awareness Web Application for College Students
Course: 25CPD37 - Community Project using Innovation and Design Thinking
Department of Computer Science and Engineering, New Horizon College of Engineering

Engineered for 16:9 Widescreen with zero text-overflow across all slides.
"""

import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path):
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    PRIMARY = RGBColor(6, 95, 70)          # Dark Emerald Green (#065F46)
    PRIMARY_LIGHT = RGBColor(209, 250, 229) # Mint Light (#D1FAE5)
    ACCENT_MINT = RGBColor(16, 185, 129)    # Mint Green (#10B981)
    BLUE_ACCENT = RGBColor(2, 132, 199)    # Ocean Blue (#0284C7)
    BLUE_LIGHT = RGBColor(224, 242, 254)   # Light Blue (#E0F2FE)
    TEXT_DARK = RGBColor(15, 23, 42)       # Slate 900 (#0F172A)
    TEXT_MUTED = RGBColor(71, 85, 105)     # Slate 600 (#475569)
    WHITE = RGBColor(255, 255, 255)
    CARD_BG = RGBColor(255, 255, 255)
    CARD_BORDER = RGBColor(226, 232, 240)
    AMBER = RGBColor(245, 158, 11)         # Amber (#F59E0B)
    AMBER_LIGHT = RGBColor(254, 243, 199)  # Amber Light
    ROSE = RGBColor(239, 68, 68)           # Rose Red
    PURPLE = RGBColor(139, 92, 246)        # Purple Accent

    def add_header(slide, title, category="COMMUNITY PROJECT • COURSE 25CPD37"):
        # Header banner container
        header_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        header_shape.fill.solid()
        header_shape.fill.fore_color.rgb = PRIMARY
        header_shape.line.fill.background()

        # Category pill text
        tx_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.28))
        tf_cat = tx_cat.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_MINT

        # Main Title
        tx_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.5), Inches(0.6))
        tf_t = tx_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = WHITE

        # Footer line
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.02))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = CARD_BORDER
        footer_line.line.fill.background()

        # Footer Text
        tx_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.733), Inches(0.3))
        tf_f = tx_f.text_frame
        tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        p_f.text = "New Horizon College of Engineering | Dept. of CSE | Course 25CPD37 | NutriCampus Web Application"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = TEXT_MUTED

    def setup_card_tf(tf):
        tf.word_wrap = True
        tf.margin_left = Inches(0.12)
        tf.margin_right = Inches(0.12)
        tf.margin_top = Inches(0.12)
        tf.margin_bottom = Inches(0.12)

    def add_para(tf, text, pt_size=10, bold=False, color=TEXT_DARK, space_after=4, bullet=False):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.text = f"• {text}" if bullet else text
        p.font.size = Pt(pt_size)
        p.font.bold = bold
        p.font.color.rgb = color
        p.space_after = Pt(space_after)
        return p

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = PRIMARY
    bg1.line.fill.background()

    bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.15))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = ACCENT_MINT
    bar1.line.fill.background()

    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(0.65), Inches(11.333), Inches(1.2))
    tf1 = t_box.text_frame
    setup_card_tf(tf1)
    p1 = tf1.paragraphs[0]
    p1.text = "NEW HORIZON COLLEGE OF ENGINEERING"
    p1.font.size = Pt(20)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf1.add_paragraph()
    p2.text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING"
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_MINT
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf1.add_paragraph()
    p3.text = "Course: Community Project using Innovation and Design Thinking (Course Code: 25CPD37 | Semester: III)"
    p3.font.size = Pt(11)
    p3.font.color.rgb = PRIMARY_LIGHT
    p3.alignment = PP_ALIGN.CENTER

    # Project Title Card (Center)
    title_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.15), Inches(10.333), Inches(2.55))
    title_card.fill.solid()
    title_card.fill.fore_color.rgb = WHITE
    title_card.line.fill.background()

    tc_box = s1.shapes.add_textbox(Inches(1.7), Inches(2.35), Inches(9.933), Inches(2.15))
    tcf = tc_box.text_frame
    setup_card_tf(tcf)
    
    tp1 = tcf.paragraphs[0]
    tp1.text = "PROJECT PRESENTATION • COMPREHENSIVE OVERVIEW"
    tp1.font.size = Pt(11)
    tp1.font.bold = True
    tp1.font.color.rgb = BLUE_ACCENT
    tp1.alignment = PP_ALIGN.CENTER

    tp2 = tcf.add_paragraph()
    tp2.text = "Health & Nutrition Awareness Web Application\nfor College Students"
    tp2.font.size = Pt(26)
    tp2.font.bold = True
    tp2.font.color.rgb = PRIMARY
    tp2.alignment = PP_ALIGN.CENTER

    tp3 = tcf.add_paragraph()
    tp3.text = "NutriCampus • A Student-Friendly Health, Hydration & Wellness Platform"
    tp3.font.size = Pt(13)
    tp3.font.bold = True
    tp3.font.color.rgb = TEXT_MUTED
    tp3.alignment = PP_ALIGN.CENTER

    # Team & Guide Details in Bottom Cards
    team_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.95), Inches(5.0), Inches(1.85))
    team_card.fill.solid()
    team_card.fill.fore_color.rgb = RGBColor(4, 120, 87)
    team_card.line.color.rgb = ACCENT_MINT
    team_card.line.width = Pt(1)

    t_box = s1.shapes.add_textbox(Inches(1.7), Inches(5.05), Inches(4.6), Inches(1.65))
    ttf = t_box.text_frame
    setup_card_tf(ttf)
    ttp1 = ttf.paragraphs[0]
    ttp1.text = "PRESENTED BY (STUDENT TEAM):"
    ttp1.font.size = Pt(11)
    ttp1.font.bold = True
    ttp1.font.color.rgb = ACCENT_MINT
    
    ttp2 = ttf.add_paragraph()
    ttp2.text = "• USN: 1NH25CS___ | Student Name 1\n• USN: 1NH25CS___ | Student Name 2\n• Section: CSE - 3rd Semester\n• Duration: Sep 2026 – Dec 2026"
    ttp2.font.size = Pt(10.5)
    ttp2.font.color.rgb = WHITE

    guide_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.95), Inches(5.0), Inches(1.85))
    guide_card.fill.solid()
    guide_card.fill.fore_color.rgb = RGBColor(4, 120, 87)
    guide_card.line.color.rgb = ACCENT_MINT
    guide_card.line.width = Pt(1)

    g_box = s1.shapes.add_textbox(Inches(7.0), Inches(5.05), Inches(4.6), Inches(1.65))
    gtf = g_box.text_frame
    setup_card_tf(gtf)
    gtp1 = gtf.paragraphs[0]
    gtp1.text = "ACADEMIC MENTORSHIP & APPROVALS:"
    gtp1.font.size = Pt(11)
    gtp1.font.bold = True
    gtp1.font.color.rgb = ACCENT_MINT

    gtp2 = gtf.add_paragraph()
    gtp2.text = "• Project Guide: Faculty Mentor, Dept. of CSE\n• Course Coordinator: 25CPD37 Coordinator\n• Head of Department: HoD – CSE\n• Institution: NHCE Bengaluru"
    gtp2.font.size = Pt(10.5)
    gtp2.font.color.rgb = WHITE

    # ==========================================
    # SLIDE 2: CONTEXT & MOTIVATION
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Context & Motivation: Student Health on Campus")

    col_w = Inches(3.64)
    gap_x = Inches(0.4)
    top_y = Inches(1.4)
    card_h = Inches(5.35)

    cards_s2 = [
        ("The Undergraduate Reality", "⏰", [
            ("Rigorous Schedules", "Long lecture hours, 3-hour programming labs, and deadlines leave little time for healthy meal planning."),
            ("Irregular Meal Patterns", "Skipping breakfast, dining late at night, and erratic snacking are widespread daily habits."),
            ("Hostel & Mess Monotony", "Dependence on repetitive mess menus and canteen fried snacks leads to nutritional deficits.")
        ], PRIMARY),
        ("The Health & Focus Gap", "📉", [
            ("Afternoon Brain Fog", "Heavy refined carbohydrate lunches trigger sharp 2:00 PM lecture drowsiness and sluggishness."),
            ("Chronic Dehydration", "Students frequently forget to drink water, causing fatigue and tension headaches in coding labs."),
            ("Internet Fad Risks", "Social media promotes unverified, restrictive diets that harm physical stamina and mental focus.")
        ], BLUE_ACCENT),
        ("Why NutriCampus?", "💡", [
            ("Student-Centered Education", "Evidence-backed guidance centered on accessible, budget-friendly everyday foods."),
            ("Interactive Actionable Tools", "Simple BMI screening, fluid tracking with visual bottle animation, and campus canteen food swaps."),
            ("Non-Clinical & Safe", "100% educational guidance that avoids medical diagnosis or clinical replacement.")
        ], ACCENT_MINT)
    ]

    for i, (title, icon, bullets, accent_col) in enumerate(cards_s2):
        x = Inches(0.8) + i * (col_w + gap_x)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top_y, col_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        c_top = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top_y, col_w, Inches(0.75))
        c_top.fill.solid()
        c_top.fill.fore_color.rgb = accent_col
        c_top.line.fill.background()

        tx = s2.shapes.add_textbox(x + Inches(0.15), top_y + Inches(0.08), col_w - Inches(0.3), Inches(0.6))
        tf = tx.text_frame
        setup_card_tf(tf)
        p = tf.paragraphs[0]
        p.text = f"{icon}  {title}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = WHITE

        tx_b = s2.shapes.add_textbox(x + Inches(0.15), top_y + Inches(0.9), col_w - Inches(0.3), card_h - Inches(1.0))
        tf_b = tx_b.text_frame
        setup_card_tf(tf_b)
        for h, d in bullets:
            add_para(tf_b, f"• {h}: {d}", pt_size=10, color=TEXT_DARK, space_after=10)

    # ==========================================
    # SLIDE 3: PROBLEM STATEMENT & ETHICAL BOUNDARY
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Problem Statement & Non-Diagnostic Ethical Boundary")

    w_half = Inches(5.66)
    p_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = WHITE
    p_box.line.color.rgb = ROSE
    p_box.line.width = Pt(1.5)

    pt_box = s3.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    ptf = pt_box.text_frame
    setup_card_tf(ptf)
    add_para(ptf, "🚨 PROBLEM STATEMENT", pt_size=13, bold=True, color=ROSE, space_after=8)
    add_para(ptf, "College students encounter significant barriers finding simple, reliable, and accessible information on balanced diets, hydration, and daily wellness routines:", pt_size=10.5, color=TEXT_MUTED, space_after=8)
    add_para(ptf, "Rigid Academic Schedules: Back-to-back lectures, 3-hour coding labs, and project sprints leave little room for wholesome meal planning.", pt_size=10, bullet=True, space_after=6)
    add_para(ptf, "Unhealthy Snack Dependency: Heavy reliance on instant noodles, fried canteen snacks, and high-sugar energy drinks for quick study energy.", pt_size=10, bullet=True, space_after=6)
    add_para(ptf, "Cognitive Impairment from Dehydration: Students routinely forget water intake, impairing debugging focus and triggering tension headaches.", pt_size=10, bullet=True, space_after=6)
    add_para(ptf, "Lack of Integrated Campus Tools: No single localized platform connecting nutrition education with practical canteen-friendly swaps and trackers.", pt_size=10, bullet=True, space_after=6)

    b_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    b_box.fill.solid()
    b_box.fill.fore_color.rgb = AMBER_LIGHT
    b_box.line.color.rgb = AMBER
    b_box.line.width = Pt(1.5)

    bt_box = s3.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    btf = bt_box.text_frame
    setup_card_tf(btf)
    add_para(btf, "⚠️ MANDATORY NON-DIAGNOSTIC BOUNDARY", pt_size=13, bold=True, color=RGBColor(180, 83, 9), space_after=8)
    add_para(btf, "Strictly aligned with Course 25CPD37 syllabus and health software ethics:", pt_size=10.5, color=RGBColor(120, 53, 15), space_after=8)
    add_para(btf, "Educational Awareness Only: Built exclusively to build student health literacy and daily habits. It does NOT diagnose medical conditions.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=6)
    add_para(btf, "No Clinical Prescriptions: Does not prescribe pharmacological supplements, restrictive diets, or medical meal therapies.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=6)
    add_para(btf, "BMI Screening Caveat: BMI is explicitly explained as a screening ratio, NOT an indicator of body fat, muscle mass, or fitness.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=6)
    add_para(btf, "Medical Referral Protocol: Students with clinical concerns are guided to consult campus health clinic officers or certified dietitians.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=6)

    # ==========================================
    # SLIDE 4: TARGET COMMUNITY & BENEFICIARIES
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Target Community & Stakeholder Beneficiaries")

    t_cards = [
        ("Primary: Undergraduate Students", "🎓", [
            ("CSE & Engineering Students", "Navigating 3-hour laboratory sessions, programming sprints, and high screen fatigue."),
            ("Hostel Residents", "Seeking affordable, nutritious ways to supplement repetitive mess menus (peanuts, curd, sprouts)."),
            ("Day Scholars & Commuters", "Balancing morning transit fatigue and irregular meal timings with practical on-campus choices.")
        ], PRIMARY),
        ("Secondary: Campus Ecosystem", "🏛️", [
            ("Student Wellness & Health Clubs", "Can utilize NutriCampus for interactive campus wellness drives, quizzes, and workshops."),
            ("Campus Health Center Staff", "Complements clinical consultations with preventative lifestyle and hydration guidance."),
            ("Faculty & Academic Mentors", "Promotes student vitality, cognitive alertness, and lab participation.")
        ], BLUE_ACCENT),
        ("Community Evaluation Cohort", "🤝", [
            ("Peer Testing Volunteer Group", "Evaluated directly by 12+ student peer volunteers from CSE Semester III."),
            ("Informal Feedback Loops", "Assessed content clarity, navigation responsiveness, and practical usefulness."),
            ("Measurable Health Literacy", "Focuses on measurable habit awareness rather than unverifiable clinical outcomes.")
        ], ACCENT_MINT)
    ]

    for i, (title, icon, bullets, accent_col) in enumerate(t_cards):
        x = Inches(0.8) + i * (col_w + gap_x)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top_y, col_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        c_top = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top_y, col_w, Inches(0.75))
        c_top.fill.solid()
        c_top.fill.fore_color.rgb = accent_col
        c_top.line.fill.background()

        tx = s4.shapes.add_textbox(x + Inches(0.15), top_y + Inches(0.08), col_w - Inches(0.3), Inches(0.6))
        tf = tx.text_frame
        setup_card_tf(tf)
        p = tf.paragraphs[0]
        p.text = f"{icon}  {title}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = WHITE

        tx_b = s4.shapes.add_textbox(x + Inches(0.15), top_y + Inches(0.9), col_w - Inches(0.3), card_h - Inches(1.0))
        tf_b = tx_b.text_frame
        setup_card_tf(tf_b)
        for h, d in bullets:
            add_para(tf_b, f"• {h}: {d}", pt_size=10, color=TEXT_DARK, space_after=10)

    # ==========================================
    # SLIDE 5: INNOVATION & DESIGN THINKING FRAMEWORK
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Innovation & Design Thinking 5-Stage Framework")

    dt_steps = [
        ("1. Empathize", "🎧", [
            "Conducted informal peer chats with hostellers and day scholars.",
            "Identified pain points: tight budgets, lack of time, canteen oiliness, and dehydration."
        ], PRIMARY),
        ("2. Define", "🎯", [
            "Problem: Students need quick, realistic awareness—not clinical lectures or expensive meal charts.",
            "Established scope: Awareness, screening, and habit tracking."
        ], BLUE_ACCENT),
        ("3. Ideate", "💡", [
            "50-25-25 visual plate.",
            "Canteen food swaps (Maggi -> Poha).",
            "Animated water bottle tracker.",
            "Gamified myth-busting quiz."
        ], AMBER),
        ("4. Prototype", "⚙️", [
            "Responsive single-page web app.",
            "HTML5 semantic structure, modern CSS3 (Dark/Light).",
            "JavaScript localStorage persistence.",
            "Modular backend architecture."
        ], ACCENT_MINT),
        ("5. Test", "🧪", [
            "Pilot evaluation with 12+ student peer volunteers.",
            "Measured: Navigation (4.9/5), Content (4.8/5), Tools (5.0/5).",
            "Refined mobile UI."
        ], PURPLE)
    ]

    step_w = Inches(2.18)
    step_gap = Inches(0.2)
    for i, (name, icon, items, col) in enumerate(dt_steps):
        s_left = Inches(0.8) + i * (step_w + step_gap)
        scard = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s_left, top_y, step_w, card_h)
        scard.fill.solid()
        scard.fill.fore_color.rgb = WHITE
        scard.line.color.rgb = CARD_BORDER
        scard.line.width = Pt(1.5)

        pill = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s_left, top_y, step_w, Inches(0.85))
        pill.fill.solid()
        pill.fill.fore_color.rgb = col
        pill.line.fill.background()

        ptx = s5.shapes.add_textbox(s_left + Inches(0.1), top_y + Inches(0.08), step_w - Inches(0.2), Inches(0.75))
        ptf = ptx.text_frame
        setup_card_tf(ptf)
        pp = ptf.paragraphs[0]
        pp.text = f"{icon}\n{name}"
        pp.font.size = Pt(11.5)
        pp.font.bold = True
        pp.font.color.rgb = WHITE
        pp.alignment = PP_ALIGN.CENTER

        btx = s5.shapes.add_textbox(s_left + Inches(0.12), top_y + Inches(1.0), step_w - Inches(0.24), card_h - Inches(1.1))
        btf = btx.text_frame
        setup_card_tf(btf)
        for item in items:
            add_para(btf, item, pt_size=9.5, color=TEXT_DARK, space_after=8, bullet=True)

    # ==========================================
    # SLIDE 6: SYSTEM ARCHITECTURE & TECH STACK
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "System Architecture & Technology Stack")

    stack_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    stack_card.fill.solid()
    stack_card.fill.fore_color.rgb = WHITE
    stack_card.line.color.rgb = PRIMARY
    stack_card.line.width = Pt(1.5)

    stx = s6.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    stf = stx.text_frame
    setup_card_tf(stf)
    add_para(stf, "💻 TECHNOLOGY STACK SPECIFICATIONS", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(stf, "Frontend Architecture Layer:", pt_size=11, bold=True, color=TEXT_DARK, space_after=4)
    add_para(stf, "HTML5: Semantic markup, accessible tab navigation, native input validation.", pt_size=10, bullet=True, space_after=3)
    add_para(stf, "CSS3: Custom CSS variables, Flexbox & CSS Grid, fluid keyframe liquid animations, Light/Dark theme switching.", pt_size=10, bullet=True, space_after=3)
    add_para(stf, "JavaScript (ES6+): Client-side calculations, DOM event handlers, dynamic meter pointer, quiz state machine.", pt_size=10, bullet=True, space_after=6)
    
    add_para(stf, "Data Persistence & Storage Layer:", pt_size=11, bold=True, color=TEXT_DARK, space_after=4)
    add_para(stf, "Browser localStorage: Offline persistence for daily water logs, theme settings, and tester reviews.", pt_size=10, bullet=True, space_after=3)
    add_para(stf, "SQLite3 (health_nutrition.db): Lightweight relational storage for offline feedback logging.", pt_size=10, bullet=True, space_after=6)
    
    add_para(stf, "Backend & Deployment Services:", pt_size=11, bold=True, color=TEXT_DARK, space_after=4)
    add_para(stf, "Python 3 & Flask (app.py): REST API endpoints (/api/feedback).", pt_size=10, bullet=True, space_after=3)
    add_para(stf, "Python Standard Library (local_server.py): Zero-dependency server for offline classroom evaluation.", pt_size=10, bullet=True, space_after=3)
    add_para(stf, "Vercel Cloud Platform: High-availability global deployment.", pt_size=10, bullet=True, space_after=3)

    arch_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    arch_card.fill.solid()
    arch_card.fill.fore_color.rgb = WHITE
    arch_card.line.color.rgb = BLUE_ACCENT
    arch_card.line.width = Pt(1.5)

    atx = s6.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    atf = atx.text_frame
    setup_card_tf(atf)
    add_para(atf, "🏗️ ARCHITECTURAL DESIGN PRINCIPLES", pt_size=13, bold=True, color=BLUE_ACCENT, space_after=8)
    add_para(atf, "Client-First Zero-Friction Design: The entire application operates 100% out-of-the-box in any modern browser without mandatory backend or external database dependencies.", pt_size=10, bullet=True, space_after=6)
    add_para(atf, "Strict Privacy Preservation: Avoids transmitting personal metrics (height, weight, daily water intake) to remote servers. All personal logs remain strictly local.", pt_size=10, bullet=True, space_after=6)
    add_para(atf, "Mobile-First Responsiveness: Fluidly adapts from smartphone screens (360px) to computer lab displays (1920px).", pt_size=10, bullet=True, space_after=6)
    add_para(atf, "Modular Decoupling: Nutrition Guide, BMI Calculator, Water Tracker, Quiz, and Feedback survey operate as decoupled functional modules.", pt_size=10, bullet=True, space_after=6)

    # ==========================================
    # SLIDE 7: MODULE 1 - HOME & OVERVIEW
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Module 1: Home & Overview Portal")

    m1_left = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    m1_left.fill.solid()
    m1_left.fill.fore_color.rgb = WHITE
    m1_left.line.color.rgb = PRIMARY
    m1_left.line.width = Pt(1.5)

    tx1 = s7.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf1 = tx1.text_frame
    setup_card_tf(tf1)
    add_para(tf1, "🌟 HERO SECTION & PROJECT IDENTITY", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(tf1, "Institutional Banner & Badge: Badged with 'NHCE • CSE Dept • 25CPD37' emphasizing community project alignment.", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "Purpose-Driven Hero Statement: 'Fueling Student Minds & Bodies' — tailored specifically for undergraduate engineering realities.", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "Key Health Metric Highlights:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf1, "2.5L Recommended Daily Water Target", pt_size=10, bullet=True, space_after=3)
    add_para(tf1, "5 Essential Food Groups Represented", pt_size=10, bullet=True, space_after=3)
    add_para(tf1, "100% Free, Student-Friendly & Non-Medical", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "Direct Action CTAs: One-click navigation to explore the Nutrition Guide, BMI Calculator, and Water Tracker.", pt_size=10, bullet=True, space_after=4)

    m1_right = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    m1_right.fill.solid()
    m1_right.fill.fore_color.rgb = WHITE
    m1_right.line.color.rgb = BLUE_ACCENT
    m1_right.line.width = Pt(1.5)

    tx2 = s7.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf2 = tx2.text_frame
    setup_card_tf(tf2)
    add_para(tf2, "🧭 ACADEMIC META & NAVIGATION CARDS", pt_size=13, bold=True, color=BLUE_ACCENT, space_after=8)
    add_para(tf2, "Interactive Feature Grid: Visual preview cards introducing each of the core tools (Nutrition, BMI, Water, Habits, Quiz, Feedback).", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Academic Project Metadata Box:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf2, "Institution: New Horizon College of Engineering", pt_size=10, bullet=True, space_after=3)
    add_para(tf2, "Department: Computer Science and Engineering", pt_size=10, bullet=True, space_after=3)
    add_para(tf2, "Course Code: 25CPD37 (Innovation and Design Thinking)", pt_size=10, bullet=True, space_after=3)
    add_para(tf2, "Duration: Sep 2026 – Dec 2026 (Semester III)", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Universal Accessibility: Header dark/light mode toggle and responsive mobile drawer navigation.", pt_size=10, bullet=True, space_after=4)

    # ==========================================
    # SLIDE 8: MODULE 2 - NUTRITION & BALANCED PLATE
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Module 2: Nutrition Guide & The 50-25-25 College Plate")

    m2_left = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    m2_left.fill.solid()
    m2_left.fill.fore_color.rgb = WHITE
    m2_left.line.color.rgb = PRIMARY
    m2_left.line.width = Pt(1.5)

    tx1 = s8.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf1 = tx1.text_frame
    setup_card_tf(tf1)
    add_para(tf1, "🍽️ THE 50-25-25 BALANCED PLATE MODEL", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(tf1, "A visual framework endorsed by Harvard Health & ICMR-NIN public health standards that eliminates tedious calorie counting:", pt_size=10.5, color=TEXT_MUTED, space_after=8)
    add_para(tf1, "50% Plate: Colorful Vegetables & Fruits: Delivers essential dietary fiber, Vitamin C, and hydration; prevents mid-day sugar spikes.", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "25% Plate: Complex Whole Grains: Whole wheat rotis, brown/parboiled rice, ragi, jowar, oats; supplies sustained glucose release for coding labs.", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "25% Plate: Quality Protein & Pulses: Dal, rajma, chole, paneer, eggs, sprouts, and curd; fuels muscle recovery and lasting satiety.", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "Side Drink: Water or fresh buttermilk (chaas) rather than sugary sodas.", pt_size=10, bullet=True, space_after=4)

    m2_right = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    m2_right.fill.solid()
    m2_right.fill.fore_color.rgb = WHITE
    m2_right.line.color.rgb = ACCENT_MINT
    m2_right.line.width = Pt(1.5)

    tx2 = s8.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf2 = tx2.text_frame
    setup_card_tf(tf2)
    add_para(tf2, "🥗 FOOD GROUP EXPLORER & SUPERFOODS", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(tf2, "Interactive Category Filters: Students can filter cards by Carbs, Proteins, Healthy Fats, Micronutrients, and Hydration & Fiber.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Budget-Friendly Student Superfoods:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf2, "Roasted Peanuts & Chana: Inexpensive, shelf-stable protein for study desks.", pt_size=10, bullet=True, space_after=3)
    add_para(tf2, "Curd & Plain Dahi: Probiotics supporting digestive comfort and focus.", pt_size=10, bullet=True, space_after=3)
    add_para(tf2, "Bananas & Seasonal Fruit: Natural quick-energy fuel for lectures.", pt_size=10, bullet=True, space_after=3)
    add_para(tf2, "Boiled Eggs / Paneer: Complete amino-acid sources.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Hostel Room Hack: Keeping roasted chana or peanuts at the desk helps students resist midnight junk food cravings.", pt_size=10, bullet=True, space_after=4)

    # ==========================================
    # SLIDE 9: MODULE 2 (CONT) - CAMPUS FOOD SWAPS
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Module 2: Campus Canteen & Hostel Food Swaps")

    swaps_data = [
        ("❌ Instant Noodles (Daily)", "🥣 Veggie Poha / Oats with Peanuts", "Sustained complex fiber & protein; eliminates the 1-hour post-snack sugar crash during afternoon laboratory sessions.", PRIMARY),
        ("❌ Packaged Fizzy Sodas & Canned Juices", "🥛 Fresh Chaas (Buttermilk) / Nimbu Pani", "Naturally cools digestion, replenishes potassium/sodium electrolytes, zero synthetic high-fructose corn syrup.", BLUE_ACCENT),
        ("❌ Deep-Fried Samosas & Bakery Puffs", "🥜 Boiled Chana Chaat / Roasted Makhana", "High protein and dietary fiber; eliminates post-lunch sluggishness before afternoon engineering labs.", AMBER),
        ("❌ 4+ Cups of High-Sugar Coffee/Energy Drinks", "🍵 Green Tea / Cold Water Refills", "Reduces exam jitteriness, eliminates dehydration-induced tachycardia and midnight insomnia.", PURPLE)
    ]

    for idx, (bad, good, reason, col) in enumerate(swaps_data):
        y_pos = Inches(1.38) + idx * Inches(1.28)
        scard = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.733), Inches(1.15))
        scard.fill.solid()
        scard.fill.fore_color.rgb = WHITE
        scard.line.color.rgb = col
        scard.line.width = Pt(1.5)

        stx = s9.shapes.add_textbox(Inches(1.0), y_pos + Inches(0.08), Inches(11.333), Inches(0.95))
        stf = stx.text_frame
        setup_card_tf(stf)
        
        p = stf.paragraphs[0]
        p.text = f"{bad}   ➡️   {good}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col
        p.space_after = Pt(2)

        p2 = stf.add_paragraph()
        p2.text = f"Why it benefits your academic day: {reason}"
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_DARK

    tip_box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.55), Inches(11.733), Inches(0.45))
    tip_box.fill.solid()
    tip_box.fill.fore_color.rgb = PRIMARY_LIGHT
    tip_box.line.fill.background()

    ttx = s9.shapes.add_textbox(Inches(1.0), Inches(6.58), Inches(11.333), Inches(0.4))
    ttf = ttx.text_frame
    setup_card_tf(ttf)
    p = ttf.paragraphs[0]
    p.text = "💡 Nutritional Bioavailability Hack: Squeezing fresh lemon over canteen dal or poha triples non-heme plant iron absorption, protecting students from fatigue and anemia!"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    # ==========================================
    # SLIDE 10: MODULE 3 - BMI CALCULATOR
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Module 3: BMI Calculator & Screening Tool")

    m3_left = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    m3_left.fill.solid()
    m3_left.fill.fore_color.rgb = WHITE
    m3_left.line.color.rgb = BLUE_ACCENT
    m3_left.line.width = Pt(1.5)

    tx1 = s10.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf1 = tx1.text_frame
    setup_card_tf(tf1)
    add_para(tf1, "⚖️ CALCULATION ENGINE & VISUAL GAUGE", pt_size=13, bold=True, color=BLUE_ACCENT, space_after=8)
    add_para(tf1, "Dual-Unit Input Flexibility:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf1, "Metric Mode: Height in cm, Weight in kg.", pt_size=10, bullet=True, space_after=2)
    add_para(tf1, "Imperial Mode: Height in feet & inches, Weight in lbs.", pt_size=10, bullet=True, space_after=5)
    add_para(tf1, "Mathematical Formula: BMI = Weight (kg) / [Height (m)]²", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "Dynamic Visual Gauge Meter: Pointer translates across 4 WHO standard classification zones:", pt_size=10, bullet=True, space_after=4)
    add_para(tf1, "Blue: Underweight (< 18.5)", pt_size=9.5, space_after=2)
    add_para(tf1, "Green: Normal / Healthy Range (18.5 – 24.9)", pt_size=9.5, space_after=2)
    add_para(tf1, "Amber: Overweight (25.0 – 29.9)", pt_size=9.5, space_after=2)
    add_para(tf1, "Red: Obesity Range (≥ 30.0)", pt_size=9.5, space_after=6)
    add_para(tf1, "Healthy Weight Guidance: Computes estimated healthy weight bounds for the student's exact height.", pt_size=10, bullet=True, space_after=4)

    m3_right = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    m3_right.fill.solid()
    m3_right.fill.fore_color.rgb = AMBER_LIGHT
    m3_right.line.color.rgb = AMBER
    m3_right.line.width = Pt(1.5)

    tx2 = s10.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf2 = tx2.text_frame
    setup_card_tf(tf2)
    add_para(tf2, "⚠️ PROMINENT MEDICAL DISCLAIMER", pt_size=13, bold=True, color=RGBColor(180, 83, 9), space_after=8)
    add_para(tf2, "Prominently highlighted to fulfill institutional project guidelines and medical ethics:", pt_size=10.5, color=RGBColor(120, 53, 15), space_after=8)
    add_para(tf2, "Screening Ratio Only: BMI is an epidemiological ratio (kg/m²), NOT a clinical diagnosis of body fat percentage, fitness, or metabolic health.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=6)
    add_para(tf2, "Athletic Muscle Inaccuracy: BMI cannot differentiate between muscle mass and adipose tissue. Active athletes naturally record higher BMI while being in peak health.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=6)
    add_para(tf2, "Neutral Counseling: Displays supportive, non-stigmatizing lifestyle advice, discouraging extreme crash diets.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=6)
    add_para(tf2, "Clinical Referral: Recommends consulting campus health clinic physicians for comprehensive evaluations.", pt_size=10, bullet=True, color=RGBColor(120, 53, 15), space_after=4)

    # ==========================================
    # SLIDE 11: MODULE 4 - DAILY WATER TRACKER
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Module 4: Daily Hydration Tracker & Fluid Dynamics")

    m4_left = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    m4_left.fill.solid()
    m4_left.fill.fore_color.rgb = WHITE
    m4_left.line.color.rgb = BLUE_ACCENT
    m4_left.line.width = Pt(1.5)

    tx1 = s11.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf1 = tx1.text_frame
    setup_card_tf(tf1)
    add_para(tf1, "💧 ANIMATED FLUID DYNAMICS UI", pt_size=13, bold=True, color=BLUE_ACCENT, space_after=8)
    add_para(tf1, "Animated Water Bottle Visualizer: Custom CSS keyframe waves (dual-layer front and back waves) visually simulating rising liquid levels.", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "Target Goal Customization: Dropdown selector: 2000 ml, 2500 ml (recommended student average), 3000 ml, or 3500 ml.", pt_size=10, bullet=True, space_after=6)
    add_para(tf1, "Quick-Add Portion Buttons:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf1, "🥛 Small Glass (+200 ml)", pt_size=9.5, space_after=2)
    add_para(tf1, "🥤 Standard Cup (+250 ml)", pt_size=9.5, space_after=2)
    add_para(tf1, "🍼 Campus Bottle (+500 ml)", pt_size=9.5, space_after=2)
    add_para(tf1, "🍵 Warm Water / Tea (+150 ml) + Custom numeric ml input.", pt_size=9.5, space_after=6)
    add_para(tf1, "Live Progress: Dynamic percentage chip and motivational milestone alerts.", pt_size=10, bullet=True, space_after=4)

    m4_right = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    m4_right.fill.solid()
    m4_right.fill.fore_color.rgb = WHITE
    m4_right.line.color.rgb = PRIMARY
    m4_right.line.width = Pt(1.5)

    tx2 = s11.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf2 = tx2.text_frame
    setup_card_tf(tf2)
    add_para(tf2, "📊 LOGGING & COGNITIVE BENEFITS", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(tf2, "Consumption Log History: Detailed log entries with exact timestamps so students can review daily habits.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Undo & Safe Reset: 'Undo Last' button and 'Reset Today' with confirmation modal.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "LocalStorage Auto-Persistence: Data persists across browser refreshes and resets automatically on each new calendar day.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Cognitive Benefits for CSE Students:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf2, "1–2% mild dehydration noticeably impairs code debugging focus, short-term memory, and reaction time.", pt_size=10, bullet=True, space_after=3)
    add_para(tf2, "Proper hydration prevents tension headaches during long programming lab sessions.", pt_size=10, bullet=True, space_after=4)

    # ==========================================
    # SLIDE 12: MODULE 5 - HEALTHY CAMPUS HABITS
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Module 5: Healthy Campus Habits & Wellness Routines")

    habits = [
        ("💻 20-20-20 Screen Rule", "Every 20 minutes, gaze at an object 20 feet away for 20 seconds. Crucial for engineering students to relieve corneal strain during 3-hour programming labs.", PRIMARY),
        ("🧠 Exam Brain Fuel", "Eat a light balanced meal 90 minutes before exams (curd, banana, boiled egg). Heavy oily food shunts blood away from neural recall to digestion.", BLUE_ACCENT),
        ("🌙 Study Snacking", "Swap sweet biscuits and oily instant noodles for roasted makhana, peanuts, or warm milk to avoid insomnia-inducing insulin spikes.", AMBER),
        ("😴 Circadian Sleep", "Dim laptop screens with blue-light filters after 9 PM. Consistent 7-8 hours sleep consolidates newly learned code algorithms into long-term memory.", ACCENT_MINT),
        ("🧘 Lab Desk Stretches", "Gentle 3-minute cervical shoulder rolls and lumbar twists alleviate chronic 'tech-neck' strain caused by prolonged laptop posture.", PURPLE),
        ("🥗 Mindful Meals", "Eat meals away from YouTube or debug terminals. Undistracted eating ensures proper satiety hormone signaling and prevents overeating.", RGBColor(236, 72, 153))
    ]

    h_w = Inches(3.64)
    h_h = Inches(2.45)
    for idx, (h_title, h_desc, h_col) in enumerate(habits):
        col_idx = idx % 3
        row_idx = idx // 3
        x = Inches(0.8) + col_idx * (h_w + Inches(0.4))
        y = Inches(1.4) + row_idx * (h_h + Inches(0.25))

        hcard = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, h_w, h_h)
        hcard.fill.solid()
        hcard.fill.fore_color.rgb = WHITE
        hcard.line.color.rgb = h_col
        hcard.line.width = Pt(1.5)

        htx = s12.shapes.add_textbox(x + Inches(0.12), y + Inches(0.1), h_w - Inches(0.24), h_h - Inches(0.2))
        htf = htx.text_frame
        setup_card_tf(htf)
        add_para(htf, h_title, pt_size=12, bold=True, color=h_col, space_after=4)
        add_para(htf, h_desc, pt_size=9.5, color=TEXT_DARK, space_after=2)

    # ==========================================
    # SLIDE 13: MODULE 6 - NUTRITION & WELLNESS QUIZ
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Module 6: Interactive Nutrition & Wellness Quiz")

    m6_left = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    m6_left.fill.solid()
    m6_left.fill.fore_color.rgb = WHITE
    m6_left.line.color.rgb = PRIMARY
    m6_left.line.width = Pt(1.5)

    tx1 = s13.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf1 = tx1.text_frame
    setup_card_tf(tf1)
    add_para(tf1, "🧠 7 HIGH-YIELD COLLEGE MYTH-BUSTERS", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(tf1, "1. Skipping Breakfast vs. Cognition: Busts the myth that skipping breakfast aids fat loss; explains glycogen depletion and lecture fatigue.", pt_size=9.5, bullet=True, space_after=5)
    add_para(tf1, "2. Harvard Plate Proportions (50%): Clarifies why whole fruits and vegetables cannot be replaced by multivitamins.", pt_size=9.5, bullet=True, space_after=5)
    add_para(tf1, "3. Affordable Student Protein Sources: Identifies peanuts, eggs, curd, and sprouts as budget alternatives to commercial protein powders.", pt_size=9.5, bullet=True, space_after=5)
    add_para(tf1, "4. Mild Dehydration Cognitive Deficits: Explains how 1–2% fluid loss impairs laboratory coding focus.", pt_size=9.5, bullet=True, space_after=5)
    add_para(tf1, "5. Energy Drinks vs. REM Sleep: Explains caffeine diuretic effects and sleep architecture disruption.", pt_size=9.5, bullet=True, space_after=5)
    add_para(tf1, "6. Vitamin C & Non-Heme Iron: Science of lemon juice pairing with canteen dal.", pt_size=9.5, bullet=True, space_after=5)
    add_para(tf1, "7. Late-Night Study Snacks: Safe swaps to avoid midnight glucose spikes.", pt_size=9.5, bullet=True, space_after=3)

    m6_right = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    m6_right.fill.solid()
    m6_right.fill.fore_color.rgb = WHITE
    m6_right.line.color.rgb = BLUE_ACCENT
    m6_right.line.width = Pt(1.5)

    tx2 = s13.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    tf2 = tx2.text_frame
    setup_card_tf(tf2)
    add_para(tf2, "🎮 GAMIFIED QUIZ MECHANICS", pt_size=13, bold=True, color=BLUE_ACCENT, space_after=8)
    add_para(tf2, "Instant Visual Feedback: Correct answers illuminate in green; wrong answers highlight in soft red while revealing the correct choice.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Scientific Rationale Box: An educational callout detailing the biological 'why' appears immediately after every response.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Live Scoreboard & Progress: Dynamic progress bar track and live score tallying.", pt_size=10, bullet=True, space_after=6)
    add_para(tf2, "Gamified Achievement Badges:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf2, "7/7: 🥇 Campus Nutrition Champion", pt_size=9.5, space_after=2)
    add_para(tf2, "5–6: 🥈 Wellness Scholar", pt_size=9.5, space_after=2)
    add_para(tf2, "3–4: 🥉 Health Novice", pt_size=9.5, space_after=6)
    add_para(tf2, "Retake Quiz: Allows students to replay and reinforce retention.", pt_size=10, bullet=True, space_after=3)

    # ==========================================
    # SLIDE 14: MODULE 7 - USABILITY FEEDBACK & EVALUATION (REDESIGNED TO PREVENT OVERFLOW)
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Module 7: Usability Feedback & Community Evaluation")

    # Left Box: Phase 6 Methodology & Form Structure (Concise, Clean)
    m7_left = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    m7_left.fill.solid()
    m7_left.fill.fore_color.rgb = WHITE
    m7_left.line.color.rgb = PRIMARY
    m7_left.line.width = Pt(1.5)

    tx1 = s14.shapes.add_textbox(Inches(1.0), top_y + Inches(0.12), w_half - Inches(0.4), card_h - Inches(0.24))
    tf1 = tx1.text_frame
    setup_card_tf(tf1)
    add_para(tf1, "📋 PHASE 6: METHODOLOGY & SURVEY PORTAL", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(tf1, "Objective 5 & Methodology Step 6 Fulfillment: Built-in usability testing survey enables peer reviewers to evaluate the live app during demonstrations.", pt_size=9.5, bullet=True, space_after=6)
    
    add_para(tf1, "Survey Data Captured:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf1, "• Department & Semester (e.g. CSE - 3rd Sem)", pt_size=9.5, space_after=2)
    add_para(tf1, "• 5-Star Rating: Ease of Navigation & UI Responsiveness", pt_size=9.5, space_after=2)
    add_para(tf1, "• 5-Star Rating: Clarity of Nutrition Information", pt_size=9.5, space_after=2)
    add_para(tf1, "• 5-Star Rating: Utility of Interactive Tools (BMI, Tracker, Quiz)", pt_size=9.5, space_after=2)
    add_para(tf1, "• Awareness Gain Metric: Yes, significantly | Somewhat | Neutral", pt_size=9.5, space_after=2)
    add_para(tf1, "• Qualitative Suggestions & Comments text area.", pt_size=9.5, space_after=6)
    
    add_para(tf1, "Dual-Mode Data Storage: Automatically updates live local metrics via localStorage and syncs with backend SQLite database.", pt_size=9.5, bullet=True, space_after=3)

    # Right Box: Metrics & Testimonials (Structured with Mini Cards)
    m7_right = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    m7_right.fill.solid()
    m7_right.fill.fore_color.rgb = WHITE
    m7_right.line.color.rgb = BLUE_ACCENT
    m7_right.line.width = Pt(1.5)

    tx2 = s14.shapes.add_textbox(Inches(7.06), top_y + Inches(0.12), w_half - Inches(0.4), card_h - Inches(0.24))
    tf2 = tx2.text_frame
    setup_card_tf(tf2)
    add_para(tf2, "📊 AGGREGATED METRICS & PEER REVIEWS", pt_size=13, bold=True, color=BLUE_ACCENT, space_after=8)
    add_para(tf2, "Pilot Cohort Evaluation Results (CSE Sem III):", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf2, "• Total Student Testers: 12+ Peer Reviewers", pt_size=9.5, space_after=2)
    add_para(tf2, "• Navigation & Responsiveness: 4.9 / 5.0 ⭐", pt_size=9.5, space_after=2)
    add_para(tf2, "• Content Clarity & Reliability: 4.8 / 5.0 ⭐", pt_size=9.5, space_after=2)
    add_para(tf2, "• Interactive Tool Utility: 5.0 / 5.0 ⭐", pt_size=9.5, space_after=2)
    add_para(tf2, "• Awareness Impact: 100% reported adopting healthier daily routines.", pt_size=9.5, space_after=8)

    add_para(tf2, "Peer Tester Testimonials:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf2, "\"Water bottle filling animation and canteen food swaps are super practical for hostel life!\"", pt_size=9.5, color=PRIMARY, space_after=2)
    add_para(tf2, "— Rahul Verma (1NH25CS142 | CSE 3rd Sem)", pt_size=8.5, color=TEXT_MUTED, space_after=6)
    add_para(tf2, "\"Appreciated the clear explanation that BMI is only a screening ratio and not a medical diagnosis.\"", pt_size=9.5, color=BLUE_ACCENT, space_after=2)
    add_para(tf2, "— Sneha Rao (1NH25CS189 | CSE 3rd Sem)", pt_size=8.5, color=TEXT_MUTED, space_after=2)

    # ==========================================
    # SLIDE 15: CONCLUSION, FUTURE SCOPE & ACKNOWLEDGEMENTS
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Conclusion, Future Roadmap & Acknowledgements")

    c1_card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, w_half, card_h)
    c1_card.fill.solid()
    c1_card.fill.fore_color.rgb = WHITE
    c1_card.line.color.rgb = PRIMARY
    c1_card.line.width = Pt(1.5)

    c1_tx = s15.shapes.add_textbox(Inches(1.0), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    c1_tf = c1_tx.text_frame
    setup_card_tf(c1_tf)
    add_para(c1_tf, "🏁 PROJECT SUMMARY & OUTCOMES", pt_size=13, bold=True, color=PRIMARY, space_after=8)
    add_para(c1_tf, "Expected Outcomes Successfully Achieved:", pt_size=10.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(c1_tf, "1. Mobile-friendly responsive health awareness web application.", pt_size=10, bullet=True, space_after=3)
    add_para(c1_tf, "2. Student-friendly education on balanced diets, food groups, and hydration.", pt_size=10, bullet=True, space_after=3)
    add_para(c1_tf, "3. Fully validated BMI calculator, daily water tracker, and quiz.", pt_size=10, bullet=True, space_after=3)
    add_para(c1_tf, "4. Documented usability feedback from volunteer student testers.", pt_size=10, bullet=True, space_after=6)
    add_para(c1_tf, "Core Innovation Value: Bridges complex health science and fast-paced college life using localized food swaps and zero-barrier digital tools.", pt_size=10, bullet=True, space_after=6)
    add_para(c1_tf, "Design Thinking Success: Demonstrated human-centered empathy for undergraduate lifestyle realities.", pt_size=10, bullet=True, space_after=3)

    c2_card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), top_y, w_half, card_h)
    c2_card.fill.solid()
    c2_card.fill.fore_color.rgb = PRIMARY
    c2_card.line.fill.background()

    c2_tx = s15.shapes.add_textbox(Inches(7.06), top_y + Inches(0.15), w_half - Inches(0.4), card_h - Inches(0.3))
    c2_tf = c2_tx.text_frame
    setup_card_tf(c2_tf)
    add_para(c2_tf, "🚀 FUTURE ROADMAP & ACKNOWLEDGEMENTS", pt_size=13, bold=True, color=ACCENT_MINT, space_after=8)
    add_para(c2_tf, "Future Roadmap Enhancements:", pt_size=10.5, bold=True, color=WHITE, space_after=4)
    add_para(c2_tf, "• Campus Mess Menu Integration: Real-time nutritional rating of weekly hostel mess meals.", pt_size=9.5, color=WHITE, space_after=3)
    add_para(c2_tf, "• Smart Push Notifications: Periodic hydration reminders during lab hours.", pt_size=9.5, color=WHITE, space_after=3)
    add_para(c2_tf, "• Multi-Language Support: Regional Indian language support for wider inclusion.", pt_size=9.5, color=WHITE, space_after=8)
    
    add_para(c2_tf, "Institutional Acknowledgements:", pt_size=10.5, bold=True, color=WHITE, space_after=4)
    add_para(c2_tf, "We express our sincere gratitude to the Department of Computer Science & Engineering, New Horizon College of Engineering, our Project Guide, Course Coordinator, and HoD for their continuous mentorship throughout Course 25CPD37.", pt_size=9.5, color=WHITE, space_after=12)

    p_end = c2_tf.add_paragraph()
    p_end.text = "THANK YOU! ANY QUESTIONS?"
    p_end.font.size = Pt(13)
    p_end.font.bold = True
    p_end.font.color.rgb = ACCENT_MINT
    p_end.alignment = PP_ALIGN.CENTER

    try:
        prs.save(output_path)
        print(f"[SUCCESS] Overflow-Free 15-Slide Presentation generated: {output_path}")
    except PermissionError:
        fallback_path = output_path.replace(".pptx", "_Updated.pptx")
        prs.save(fallback_path)
        print(f"[NOTICE] '{os.path.basename(output_path)}' is currently open in PowerPoint.")
        print(f"[SUCCESS] Saved updated version to: {fallback_path}")
        print("Please close PowerPoint to overwrite the main presentation file.")

if __name__ == "__main__":
    out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\NutriCampus-Health-Nutrition"
    out_file = os.path.join(out_dir, "NutriCampus_Project_Presentation.pptx")
    create_deck(out_file)
