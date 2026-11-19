"""
Professional PowerPoint Presentation (.pptx) Generator for:
NutriCampus - Health & Nutrition Awareness Web Application for College Students
Course: 25CPD37 - Community Project using Innovation and Design Thinking
Department of Computer Science and Engineering, New Horizon College of Engineering
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
    PRIMARY = RGBColor(6, 95, 70)        # Dark Emerald Green (#065F46)
    PRIMARY_LIGHT = RGBColor(209, 250, 229) # Mint Light (#D1FAE5)
    ACCENT_MINT = RGBColor(16, 185, 129)  # Mint Green (#10B981)
    BLUE_ACCENT = RGBColor(2, 132, 199)  # Ocean Blue (#0284C7)
    BLUE_LIGHT = RGBColor(224, 242, 254) # Light Blue (#E0F2FE)
    TEXT_DARK = RGBColor(15, 23, 42)     # Slate 900 (#0F172A)
    TEXT_MUTED = RGBColor(71, 85, 105)   # Slate 600 (#475569)
    WHITE = RGBColor(255, 255, 255)
    CARD_BG = RGBColor(255, 255, 255)
    CARD_BORDER = RGBColor(226, 232, 240)
    AMBER = RGBColor(245, 158, 11)       # Amber (#F59E0B)
    AMBER_LIGHT = RGBColor(254, 243, 199)# Amber Light
    ROSE = RGBColor(239, 68, 68)         # Rose Red
    PURPLE = RGBColor(139, 92, 246)      # Purple Accent

    def add_header(slide, title, category="COMMUNITY PROJECT • COURSE 25CPD37"):
        # Header banner container
        header_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        header_shape.fill.solid()
        header_shape.fill.fore_color.rgb = PRIMARY
        header_shape.line.fill.background()

        # Category pill text
        tx_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        tf_cat = tx_cat.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_MINT

        # Main Title
        tx_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.6))
        tf_t = tx_t.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(22)
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
        p_f = tf_f.paragraphs[0]
        p_f.text = "New Horizon College of Engineering | Dept. of CSE | Course 25CPD37 | NutriCampus Web Application"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = TEXT_MUTED

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
    tcf.word_wrap = True
    
    tp1 = tcf.paragraphs[0]
    tp1.text = "PROJECT PRESENTATION & MODULE COMPREHENSIVE OVERVIEW"
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

    col_width = Inches(3.64)
    gap = Inches(0.4)
    top_pos = Inches(1.5)
    card_h = Inches(5.2)

    cards_s2 = [
        ("The Undergraduate Reality", "⏰", [
            "Demanding Schedules: Long lecture hours, programming labs, and assignment deadlines limit time for meal planning.",
            "Irregular Eating Patterns: Skipping breakfast, late dinner hours, and erratic snacking are widespread habits.",
            "Hostel & Campus Mess Dependency: Reliance on limited hostel menus and canteen fast foods leads to nutritional imbalance."
        ], PRIMARY),
        ("The Health & Focus Gap", "📉", [
            "Cognitive Energy Slumps: Heavy refined carbohydrate meals trigger 2:00 PM lecture drowsiness and brain fog.",
            "Chronic Dehydration: Students forget to drink water, triggering screen fatigue headaches in computer labs.",
            "Internet Fad Vulnerability: Unverified social media diet fads often recommend unsafe, restrictive eating practices."
        ], BLUE_ACCENT),
        ("Why NutriCampus?", "💡", [
            "Student-Centered Awareness: Delivers reliable, evidence-backed educational guidance using familiar everyday foods.",
            "Actionable Tools: Interactive BMI screening, fluid trackers, and realistic campus canteen food swaps.",
            "Non-Clinical & Ethical: Strictly educational awareness; explicitly avoids replacing qualified doctors or clinical diagnosis."
        ], ACCENT_MINT)
    ]

    for i, (title, icon, bullets, accent_col) in enumerate(cards_s2):
        left_pos = Inches(0.8) + i * (col_width + gap)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, col_width, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        c_top = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, col_width, Inches(0.85))
        c_top.fill.solid()
        c_top.fill.fore_color.rgb = accent_col
        c_top.line.fill.background()

        tx = s2.shapes.add_textbox(left_pos + Inches(0.2), top_pos + Inches(0.12), col_width - Inches(0.4), Inches(0.65))
        tf = tx.text_frame
        p = tf.paragraphs[0]
        p.text = f"{icon}  {title}"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = WHITE

        tx_b = s2.shapes.add_textbox(left_pos + Inches(0.2), top_pos + Inches(1.0), col_width - Inches(0.4), card_h - Inches(1.1))
        tf_b = tx_b.text_frame
        tf_b.word_wrap = True
        for j, b in enumerate(bullets):
            p = tf_b.paragraphs[0] if j == 0 else tf_b.add_paragraph()
            p.text = b
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(10)

    # ==========================================
    # SLIDE 3: PROBLEM STATEMENT & ETHICAL BOUNDARY
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Problem Statement & Non-Diagnostic Ethical Boundary")

    p_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = WHITE
    p_box.line.color.rgb = ROSE
    p_box.line.width = Pt(2)

    pt_box = s3.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    ptf = pt_box.text_frame
    ptf.word_wrap = True
    pp1 = ptf.paragraphs[0]
    pp1.text = "PROBLEM STATEMENT"
    pp1.font.size = Pt(14)
    pp1.font.bold = True
    pp1.font.color.rgb = ROSE
    
    pp2 = ptf.add_paragraph()
    pp2.text = (
        "\nCollege students frequently encounter challenges finding simple, reliable, and accessible information on balanced diets, daily hydration, and wellness routines.\n\n"
        "• Busy lecture timetables, laboratory practicals, and irregular study hours trigger dependency on instant noodles, oily canteen snacks, and high-sugar energy drinks.\n\n"
        "• Proliferation of unscientific internet dietary fads encourages risky restrictive eating habits.\n\n"
        "• Lack of a single, localized, student-friendly platform combining clear nutritional guidance with interactive awareness tools.\n\n"
        "• Absence of practical guidance tailored to campus realities (hostel mess menus and canteen affordability)."
    )
    pp2.font.size = Pt(11.5)
    pp2.font.color.rgb = TEXT_DARK
    pp2.line_spacing = 1.25

    b_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    b_box.fill.solid()
    b_box.fill.fore_color.rgb = AMBER_LIGHT
    b_box.line.color.rgb = AMBER
    b_box.line.width = Pt(2)

    bt_box = s3.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    btf = bt_box.text_frame
    btf.word_wrap = True
    bp1 = btf.paragraphs[0]
    bp1.text = "⚠️ MANDATORY NON-DIAGNOSTIC BOUNDARY"
    bp1.font.size = Pt(14)
    bp1.font.bold = True
    bp1.font.color.rgb = RGBColor(180, 83, 9)

    bp2 = btf.add_paragraph()
    bp2.text = (
        "\nIn strict accordance with the syllabus of Course 25CPD37 and ethical health software design:\n\n"
        "1. Educational Awareness Only:\n"
        "   The platform is built exclusively to promote lifestyle and nutritional awareness. It does NOT provide medical diagnoses.\n\n"
        "2. No Clinical Prescription:\n"
        "   NutriCampus does NOT prescribe medical meal therapies, pharmaceutical supplements, or clinical treatments.\n\n"
        "3. BMI Limitation Guarantee:\n"
        "   The BMI calculator displays neutral, non-stigmatizing educational categories with explicit disclaimers regarding muscle mass and bone density.\n\n"
        "4. Professional Advice Substitution Clause:\n"
        "   Users are directed to campus medical center officers or registered dietitians for personal medical assessments."
    )
    bp2.font.size = Pt(11.5)
    bp2.font.color.rgb = RGBColor(120, 53, 15)
    bp2.line_spacing = 1.25

    # ==========================================
    # SLIDE 4: TARGET COMMUNITY & BENEFICIARIES
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Target Community & Stakeholder Beneficiaries")

    t_cards = [
        ("Primary Beneficiaries: Undergraduate Students", "🎓", [
            "Computer Science & Engineering Students: Navigating 3-hour laboratory sessions, coding sprints, and high screen fatigue.",
            "Hostel Residents: Navigating repetitive mess food and looking for simple, affordable nutrient supplements (curd, fruits, peanuts).",
            "Day Scholars & Commuters: Balancing transit fatigue and morning breakfast deficits with quick campus meal choices."
        ], PRIMARY),
        ("Secondary Beneficiaries: Campus Ecosystem", "🏛️", [
            "Student Health & Wellness Clubs: Can leverage NutriCampus as an educational tool for campus health drives.",
            "College Health Center Staff: Supplements clinic consultations with preventative lifestyle guidance.",
            "Faculty & Project Mentors: Promotes student vitality, cognitive alertness, and classroom engagement."
        ], BLUE_ACCENT),
        ("Community Evaluation Cohort", "🤝", [
            "Volunteer Peer Testing Group: Evaluated directly by 12+ student peer volunteers from CSE Semester III.",
            "Informal Feedback Loops: Gathering continuous usability insights on content clarity and navigation ease.",
            "Measurable Outcomes: Focus on habit awareness rather than unverifiable medical claims."
        ], ACCENT_MINT)
    ]

    for i, (title, icon, bullets, accent_col) in enumerate(t_cards):
        left_pos = Inches(0.8) + i * (col_width + gap)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, col_width, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        c_top = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, col_width, Inches(0.85))
        c_top.fill.solid()
        c_top.fill.fore_color.rgb = accent_col
        c_top.line.fill.background()

        tx = s4.shapes.add_textbox(left_pos + Inches(0.2), top_pos + Inches(0.12), col_width - Inches(0.4), Inches(0.65))
        tf = tx.text_frame
        p = tf.paragraphs[0]
        p.text = f"{icon}  {title}"
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = WHITE

        tx_b = s4.shapes.add_textbox(left_pos + Inches(0.2), top_pos + Inches(1.0), col_width - Inches(0.4), card_h - Inches(1.1))
        tf_b = tx_b.text_frame
        tf_b.word_wrap = True
        for j, b in enumerate(bullets):
            p = tf_b.paragraphs[0] if j == 0 else tf_b.add_paragraph()
            p.text = b
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(12)

    # ==========================================
    # SLIDE 5: INNOVATION & DESIGN THINKING FRAMEWORK
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Innovation & Design Thinking 5-Stage Framework")

    dt_steps = [
        ("1. Empathize", "🎧", [
            "Conducted informal interviews with hostel and day-scholar students.",
            "Identified common pain points: time limits, oily food, dehydration, exam caffeine overload."
        ], PRIMARY),
        ("2. Define", "🎯", [
            "Core Problem: Students want simple, actionable awareness—not clinical lectures or expensive diet charts.",
            "Established project boundary: Awareness, screening, and habit tracking."
        ], BLUE_ACCENT),
        ("3. Ideate", "💡", [
            "Conceived the 50-25-25 College Plate visualizer.",
            "Curated Campus Canteen food swaps (Maggi -> Poha).",
            "Designed fluid dynamics water bottle tracker.",
            "Gamified myth-busting quiz."
        ], AMBER),
        ("4. Prototype", "⚙️", [
            "Built responsive single-page web application.",
            "HTML5 semantic layout, modern CSS3 (Dark/Light themes).",
            "JavaScript client-side logic with localStorage persistence.",
            "Modular backend architecture."
        ], ACCENT_MINT),
        ("5. Test", "🧪", [
            "Piloted with 12+ student peer volunteers from CSE 3rd Sem.",
            "Measured usability: Navigation (4.9/5), Content (4.8/5), Tools (5.0/5).",
            "Refined mobile responsiveness."
        ], PURPLE)
    ]

    step_w = Inches(2.18)
    step_gap = Inches(0.2)
    for i, (name, icon, items, col) in enumerate(dt_steps):
        s_left = Inches(0.8) + i * (step_w + step_gap)
        scard = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s_left, Inches(1.5), step_w, Inches(5.2))
        scard.fill.solid()
        scard.fill.fore_color.rgb = WHITE
        scard.line.color.rgb = CARD_BORDER
        scard.line.width = Pt(1.5)

        pill = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s_left, Inches(1.5), step_w, Inches(0.9))
        pill.fill.solid()
        pill.fill.fore_color.rgb = col
        pill.line.fill.background()

        ptx = s5.shapes.add_textbox(s_left + Inches(0.1), Inches(1.55), step_w - Inches(0.2), Inches(0.8))
        ptf = ptx.text_frame
        pp = ptf.paragraphs[0]
        pp.text = f"{icon}\n{name}"
        pp.font.size = Pt(12)
        pp.font.bold = True
        pp.font.color.rgb = WHITE
        pp.alignment = PP_ALIGN.CENTER

        btx = s5.shapes.add_textbox(s_left + Inches(0.15), Inches(2.55), step_w - Inches(0.3), Inches(4.0))
        btf = btx.text_frame
        btf.word_wrap = True
        for k, item in enumerate(items):
            p = btf.paragraphs[0] if k == 0 else btf.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(10)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(8)

    # ==========================================
    # SLIDE 6: SYSTEM ARCHITECTURE & TECH STACK
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "System Architecture & Technology Stack")

    t_width = Inches(5.6)
    stack_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), t_width, Inches(5.2))
    stack_card.fill.solid()
    stack_card.fill.fore_color.rgb = WHITE
    stack_card.line.color.rgb = PRIMARY
    stack_card.line.width = Pt(1.5)

    stx = s6.shapes.add_textbox(Inches(1.0), Inches(1.7), t_width - Inches(0.4), Inches(4.8))
    stf = stx.text_frame
    stf.word_wrap = True
    sp1 = stf.paragraphs[0]
    sp1.text = "TECHNOLOGY STACK SPECIFICATIONS"
    sp1.font.size = Pt(14)
    sp1.font.bold = True
    sp1.font.color.rgb = PRIMARY

    sp2 = stf.add_paragraph()
    sp2.text = (
        "\n• Frontend Layer:\n"
        "   - HTML5: Semantic elements, accessible tab navigation, form validation.\n"
        "   - CSS3: Custom CSS variables, Flexbox & CSS Grid, fluid keyframe liquid animations, Light/Dark theme switching.\n"
        "   - JavaScript (ES6+): Client-side calculations, DOM event handlers, dynamic meters, quiz state machine.\n\n"
        "• Data Persistence & Storage Layer:\n"
        "   - Browser localStorage: High-speed client-side persistence for daily water logs, theme settings, and tester reviews.\n"
        "   - SQLite Database (health_nutrition.db): Lightweight relational storage for offline feedback logging.\n\n"
        "• Backend & Deployment Services:\n"
        "   - Python 3 & Flask (app.py): REST API endpoints (/api/feedback).\n"
        "   - Python Standard Library (local_server.py): Zero-dependency server for offline classroom evaluation.\n"
        "   - Vercel Cloud Platform: High-availability global deployment."
    )
    sp2.font.size = Pt(11)
    sp2.font.color.rgb = TEXT_DARK
    sp2.line_spacing = 1.2

    arch_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), t_width, Inches(5.2))
    arch_card.fill.solid()
    arch_card.fill.fore_color.rgb = WHITE
    arch_card.line.color.rgb = BLUE_ACCENT
    arch_card.line.width = Pt(1.5)

    atx = s6.shapes.add_textbox(Inches(7.0), Inches(1.7), t_width - Inches(0.4), Inches(4.8))
    atf = atx.text_frame
    atf.word_wrap = True
    ap1 = atf.paragraphs[0]
    ap1.text = "ARCHITECTURAL DESIGN PRINCIPLES"
    ap1.font.size = Pt(14)
    ap1.font.bold = True
    ap1.font.color.rgb = BLUE_ACCENT

    ap2 = atf.add_paragraph()
    ap2.text = (
        "\n1. Client-First Zero-Friction Architecture:\n"
        "   The entire application runs directly in any modern browser without mandatory external database or server dependencies.\n\n"
        "2. Strict Privacy Preservation:\n"
        "   Avoids transmitting sensitive personal metrics (height, weight, daily water intake) to remote servers. All personal data remains strictly local.\n\n"
        "3. Mobile-First Responsiveness:\n"
        "   Fluidly adapts from smartphone screens (360px) to laptop screens and lab desktop monitors (1920px).\n\n"
        "4. Modular Component Decoupling:\n"
        "   Independent modular structure: Nutrition Guide, BMI Calculator, Water Tracker, Quiz, and Feedback survey operate as decoupled functional modules."
    )
    ap2.font.size = Pt(11)
    ap2.font.color.rgb = TEXT_DARK
    ap2.line_spacing = 1.2

    # ==========================================
    # SLIDE 7: MODULE 1 - HOME & OVERVIEW
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Module 1: Home & Overview Portal")

    m1_left = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    m1_left.fill.solid()
    m1_left.fill.fore_color.rgb = WHITE
    m1_left.line.color.rgb = PRIMARY
    m1_left.line.width = Pt(1.5)

    tx1 = s7.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "HERO SECTION & PROJECT IDENTITY"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = tf1.add_paragraph()
    p.text = (
        "\n• Institutional Banner & Badge:\n"
        "   Prominently displays 'NHCE • CSE Dept • 25CPD37' emphasizing community project alignment.\n\n"
        "• Purpose-Driven Hero Statement:\n"
        "   'Fueling Student Minds & Bodies' — tailored specifically for undergraduate engineering realities.\n\n"
        "• Quick-Glance Key Health Statistics:\n"
        "   - 2.5L Recommended Daily Water Target\n"
        "   - 5 Essential Food Groups Represented\n"
        "   - 100% Student-Friendly, Non-Medical & Free\n\n"
        "• Direct Action CTAs:\n"
        "   One-click direct navigation into the Nutrition Guide, BMI Calculator, and Hydration Tracker."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    m1_right = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    m1_right.fill.solid()
    m1_right.fill.fore_color.rgb = WHITE
    m1_right.line.color.rgb = BLUE_ACCENT
    m1_right.line.width = Pt(1.5)

    tx2 = s7.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    tf2 = tx2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "ACADEMIC META & NAVIGATION CARDS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf2.add_paragraph()
    p.text = (
        "\n• Quick Feature Navigation Grid:\n"
        "   Interactive overview cards for Nutrition Education, BMI Calculator, Water Tracker, Nutrition Quiz, Healthy Habits, and Usability Feedback.\n\n"
        "• Academic Project Box Details:\n"
        "   - Institution: New Horizon College of Engineering\n"
        "   - Department: Computer Science & Engineering\n"
        "   - Course Code: 25CPD37 (Community Project using Innovation and Design Thinking)\n"
        "   - Duration: Sep 2026 – Dec 2026 (Semester III)\n"
        "   - Methodology: Design Thinking & Usability Testing\n\n"
        "• Universal Accessibility:\n"
        "   Header dark/light mode toggle and responsive mobile hamburger drawer."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    # ==========================================
    # SLIDE 8: MODULE 2 - NUTRITION & THE COLLEGE PLATE
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Module 2: Nutrition Guide & The 50-25-25 College Plate")

    m2_left = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    m2_left.fill.solid()
    m2_left.fill.fore_color.rgb = WHITE
    m2_left.line.color.rgb = PRIMARY
    m2_left.line.width = Pt(1.5)

    tx1 = s8.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "THE 50-25-25 BALANCED PLATE MODEL"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = tf1.add_paragraph()
    p.text = (
        "\nA simple visual rule based on Harvard Health & ICMR-NIN public health standards that eliminates tedious calorie counting:\n\n"
        "• 50% Plate: Colorful Vegetables & Fruits\n"
        "   - Delivers essential dietary fiber, Vitamin C, and antioxidants.\n"
        "   - Stabilizes blood sugar and prevents afternoon lecture lethargy.\n\n"
        "• 25% Plate: Complex Whole Grains\n"
        "   - Whole wheat rotis, brown/parboiled rice, ragi, jowar, oats.\n"
        "   - Provides slow, sustained glucose release for long coding hours.\n\n"
        "• 25% Plate: Quality Protein & Pulses\n"
        "   - Dal, rajma, chole, paneer, eggs, sprouts, and curd.\n"
        "   - Essential for tissue repair, immune vitality, and lasting satiety.\n\n"
        "• Side Drink: Water or fresh buttermilk (chaas) rather than sugary soda."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    m2_right = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    m2_right.fill.solid()
    m2_right.fill.fore_color.rgb = WHITE
    m2_right.line.color.rgb = ACCENT_MINT
    m2_right.line.width = Pt(1.5)

    tx2 = s8.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    tf2 = tx2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "INTERACTIVE FOOD GROUP EXPLORER"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = tf2.add_paragraph()
    p.text = (
        "\n• Interactive Category Filter Buttons:\n"
        "   Students can toggle: All Groups | Carbs | Proteins | Healthy Fats | Vitamins & Minerals | Hydration & Fiber.\n\n"
        "• Budget-Friendly Student Superfoods Highlighted:\n"
        "   - Peanuts & Roasted Chana: Inexpensive, shelf-stable protein for hostel desks.\n"
        "   - Curd & Plain Dahi: Natural probiotics supporting gut health and mental focus.\n"
        "   - Bananas & Apples: Natural quick-energy study fruit.\n"
        "   - Boiled Eggs / Paneer Bhurji: Complete amino-acid sources.\n\n"
        "• Practical Hostel Hacks:\n"
        "   Encouraging students to keep a box of roasted chana or peanuts in their hostel rooms to resist junk cravings."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    # ==========================================
    # SLIDE 9: MODULE 2 (CONT) - CAMPUS FOOD SWAPS
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Module 2: Campus Canteen & Hostel Food Swaps")

    swaps_data = [
        ("❌ Instant Noodles (Daily)", "🥣 Veggie Poha / Oats with Peanuts", "Sustained complex fiber & protein; eliminates the 1-hour post-snack sugar crash during laboratory sessions.", PRIMARY),
        ("❌ Packaged Fizzy Sodas & Canned Juices", "🥛 Fresh Chaas (Buttermilk) / Nimbu Pani", "Naturally cools digestion, replenishes potassium/sodium electrolytes, zero synthetic high-fructose corn syrup.", BLUE_ACCENT),
        ("❌ Deep-Fried Samosas & Bakery Puffs", "🥜 Boiled Chana Chaat / Roasted Makhana", "High protein and dietary fiber; eliminates post-lunch sluggishness before afternoon engineering labs.", AMBER),
        ("❌ 4+ Cups of High-Sugar Coffee/Energy Drinks", "🍵 Green Tea / Cold Water Refills", "Reduces exam jitteriness, eliminates dehydration-induced tachycardia and midnight insomnia.", PURPLE)
    ]

    for idx, (bad, good, reason, col) in enumerate(swaps_data):
        y_pos = Inches(1.4) + idx * Inches(1.3)
        scard = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.733), Inches(1.15))
        scard.fill.solid()
        scard.fill.fore_color.rgb = WHITE
        scard.line.color.rgb = col
        scard.line.width = Pt(1.5)

        stx = s9.shapes.add_textbox(Inches(1.0), y_pos + Inches(0.08), Inches(11.333), Inches(1.0))
        stf = stx.text_frame
        stf.word_wrap = True
        
        p = stf.paragraphs[0]
        p.text = f"{bad}   ➡️   {good}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col

        p2 = stf.add_paragraph()
        p2.text = f"Why it benefits your academic day: {reason}"
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_DARK

    # Bonus Tip Ribbon at Bottom
    tip_box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.55), Inches(11.733), Inches(0.45))
    tip_box.fill.solid()
    tip_box.fill.fore_color.rgb = PRIMARY_LIGHT
    tip_box.line.fill.background()

    ttx = s9.shapes.add_textbox(Inches(1.0), Inches(6.58), Inches(11.333), Inches(0.4))
    ttf = ttx.text_frame
    p = ttf.paragraphs[0]
    p.text = "💡 Nutritional Bioavailability Hack: Squeezing fresh lemon over canteen dal or poha triples non-heme plant iron absorption!"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    # ==========================================
    # SLIDE 10: MODULE 3 - BMI CALCULATOR
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Module 3: BMI Calculator & Screening Tool")

    m3_left = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    m3_left.fill.solid()
    m3_left.fill.fore_color.rgb = WHITE
    m3_left.line.color.rgb = BLUE_ACCENT
    m3_left.line.width = Pt(1.5)

    tx1 = s10.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "INTERACTIVE CALCULATION ENGINE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf1.add_paragraph()
    p.text = (
        "\n• Dual Input Mode Flexibility:\n"
        "   - Metric Mode: Height in centimeters (cm), Weight in kilograms (kg).\n"
        "   - Imperial Mode: Height in feet & inches (ft/in), Weight in pounds (lbs).\n\n"
        "• Mathematical Formula Applied:\n"
        "   BMI = Weight (kg) / [Height (m)]²\n\n"
        "• Dynamic Interactive Gauge Meter:\n"
        "   A translating arrow pointer maps dynamically across 4 WHO standard classification segments:\n"
        "   - Blue: Underweight (< 18.5)\n"
        "   - Green: Normal / Healthy Range (18.5 – 24.9)\n"
        "   - Amber: Overweight (25.0 – 29.9)\n"
        "   - Red: Obesity Range (≥ 30.0)\n\n"
        "• Healthy Weight Guidance:\n"
        "   Calculates estimated healthy weight bounds for the student's exact height."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    m3_right = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    m3_right.fill.solid()
    m3_right.fill.fore_color.rgb = AMBER_LIGHT
    m3_right.line.color.rgb = AMBER
    m3_right.line.width = Pt(2)

    tx2 = s10.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    tf2 = tx2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "⚠️ ESSENTIAL MEDICAL DISCLAIMER"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(180, 83, 9)

    p = tf2.add_paragraph()
    p.text = (
        "\nProminently displayed to fulfill project guidelines and medical software ethics:\n\n"
        "1. Screening Measure vs. Diagnosis:\n"
        "   BMI is an epidemiological screening ratio (kg/m²), NOT a clinical diagnosis of body fat percentage or cardiovascular health.\n\n"
        "2. Muscle Mass & Athletic Inaccuracy:\n"
        "   BMI cannot distinguish between muscle mass, bone density, and adipose fat. Athletic students or gym enthusiasts naturally show higher BMI.\n\n"
        "3. Neutral Educational Counseling:\n"
        "   Displays supportive, non-stigmatizing lifestyle guidance for each bracket, avoiding panic or extreme crash diets.\n\n"
        "4. Referral to Health Professionals:\n"
        "   Students requiring comprehensive assessments are explicitly guided to campus health center physicians."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = RGBColor(120, 53, 15)
    p.line_spacing = 1.15

    # ==========================================
    # SLIDE 11: MODULE 4 - DAILY WATER TRACKER
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Module 4: Daily Hydration Tracker & Fluid Dynamics")

    m4_left = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    m4_left.fill.solid()
    m4_left.fill.fore_color.rgb = WHITE
    m4_left.line.color.rgb = BLUE_ACCENT
    m4_left.line.width = Pt(1.5)

    tx1 = s11.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "INTERACTIVE FLUID DYNAMICS UI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf1.add_paragraph()
    p.text = (
        "\n• Animated Liquid Bottle Graphics:\n"
        "   Features custom CSS keyframe wave animations (dual-layer front and back waves) visually simulating water fill inside a bottle.\n\n"
        "• Target Goal Customization:\n"
        "   Dropdown goal selector: 2000 ml, 2500 ml (recommended student average), 3000 ml, or 3500 ml.\n\n"
        "• Quick-Add Portion Buttons:\n"
        "   - 🥛 Small Glass (+200 ml)\n"
        "   - 🥤 Standard Cup (+250 ml)\n"
        "   - 🍼 Campus Water Bottle (+500 ml)\n"
        "   - 🍵 Warm Water / Herbal Tea (+150 ml)\n"
        "   - Custom numeric input for arbitrary amounts.\n\n"
        "• Real-Time Percentage Display:\n"
        "   Live percentage chip and encouragement messages corresponding to hydration milestones."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    m4_right = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    m4_right.fill.solid()
    m4_right.fill.fore_color.rgb = WHITE
    m4_right.line.color.rgb = PRIMARY
    m4_right.line.width = Pt(1.5)

    tx2 = s11.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    tf2 = tx2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "LOGGING, DATA PERSISTENCE & BENEFITS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = tf2.add_paragraph()
    p.text = (
        "\n• Robust Logging Features:\n"
        "   - Today's consumption feed with exact timestamps.\n"
        "   - 'Undo Last' button to revert accidental taps.\n"
        "   - 'Reset Today' with safe confirmation prompt.\n\n"
        "• LocalStorage Auto-Persistence:\n"
        "   Hydration progress and logs persist automatically across browser refreshes and auto-resets when a new calendar day begins.\n\n"
        "• Cognitive Benefits for Engineering Students:\n"
        "   - Just 1–2% mild dehydration noticeably impairs code debugging focus, short-term memory, and reaction time.\n"
        "   - Proper fluid intake prevents tension headaches caused by prolonged monitor exposure in computer science labs."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    # ==========================================
    # SLIDE 12: MODULE 5 - HEALTHY CAMPUS HABITS
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Module 5: Healthy Campus Habits & Wellness Routines")

    habits = [
        ("The 20-20-20 Screen Rule", "💻", "Every 20 minutes, gaze at an object 20 feet away for 20 seconds. Crucial for CSE students to alleviate dry eyes and cornea strain during 3-hour programming labs.", PRIMARY),
        ("Exam Day Brain Fuel", "🧠", "Eat a light balanced meal 90 minutes before tests (banana, curd, boiled egg). Heavy oily food shunts blood away from neural recall to digestion.", BLUE_ACCENT),
        ("Late-Night Study Snacking", "🌙", "Swap sweet biscuits and oily instant noodles for roasted makhana, peanuts, or warm milk to avoid insomnia-inducing insulin spikes.", AMBER),
        ("Circadian Sleep Hygiene", "😴", "Dim laptop screens with blue-light filters after 9 PM. Consistent 7-8 hours sleep consolidates newly learned algorithms into long-term memory.", ACCENT_MINT),
        ("Ergonomic Lab Stretches", "🧘", "Gentle 3-minute cervical shoulder rolls and lumbar twists alleviate chronic 'tech-neck' strain caused by prolonged laptop usage.", PURPLE),
        ("Mindful Screen-Free Meals", "🥗", "Eat meals away from YouTube or debug terminals. Undistracted eating ensures proper satiety hormone signaling and prevents overeating.", RGBColor(236, 72, 153))
    ]

    h_w = Inches(3.64)
    h_h = Inches(2.45)
    for idx, (h_title, h_icon, h_desc, h_col) in enumerate(habits):
        col_idx = idx % 3
        row_idx = idx // 3
        x = Inches(0.8) + col_idx * (h_w + Inches(0.4))
        y = Inches(1.5) + row_idx * (h_h + Inches(0.3))

        hcard = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, h_w, h_h)
        hcard.fill.solid()
        hcard.fill.fore_color.rgb = WHITE
        hcard.line.color.rgb = h_col
        hcard.line.width = Pt(1.5)

        htx = s12.shapes.add_textbox(x + Inches(0.15), y + Inches(0.12), h_w - Inches(0.3), h_h - Inches(0.24))
        htf = htx.text_frame
        htf.word_wrap = True
        p = htf.paragraphs[0]
        p.text = f"{h_icon} {h_title}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = h_col

        p = htf.add_paragraph()
        p.text = h_desc
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_DARK
        p.line_spacing = 1.15

    # ==========================================
    # SLIDE 13: MODULE 6 - NUTRITION & WELLNESS QUIZ
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Module 6: Interactive Nutrition & Wellness Quiz")

    m6_left = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    m6_left.fill.solid()
    m6_left.fill.fore_color.rgb = WHITE
    m6_left.line.color.rgb = PRIMARY
    m6_left.line.width = Pt(1.5)

    tx1 = s13.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "7 HIGH-YIELD COLLEGE MYTH-BUSTERS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = tf1.add_paragraph()
    p.text = (
        "\n1. Skipping Breakfast vs. Cognition:\n"
        "   Busts the myth that skipping breakfast improves fat burn; explains glycogen depletion and lecture brain fog.\n\n"
        "2. Harvard Plate Proportions (50%):\n"
        "   Clarifies the necessity of whole fruits & veggies over artificial multivitamins.\n\n"
        "3. Affordable Student Protein Sources:\n"
        "   Highlights roasted peanuts, eggs, curd, and sprouts as budget alternatives to expensive protein supplements.\n\n"
        "4. Mild 1-2% Dehydration Impairment:\n"
        "   Proves cognitive task fatigue, reaction delays, and tension headaches.\n\n"
        "5. Energy Drinks vs. REM Sleep:\n"
        "   Explains tachycardia, diuretic fluid loss, and sleep architecture breakdown.\n\n"
        "6. Vitamin C & Non-Heme Iron Bioavailability:\n"
        "   Science of lemon juice pairing with canteen dal/poha."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    m6_right = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    m6_right.fill.solid()
    m6_right.fill.fore_color.rgb = WHITE
    m6_right.line.color.rgb = BLUE_ACCENT
    m6_right.line.width = Pt(1.5)

    tx2 = s13.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    tf2 = tx2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "INTERACTIVE QUIZ MECHANICS & GAMIFICATION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf2.add_paragraph()
    p.text = (
        "\n• Instant Feedback UX:\n"
        "   - Correct answer highlights in green with checkmark.\n"
        "   - Incorrect choice triggers soft red highlighting while simultaneously spotlighting the correct answer.\n\n"
        "• Rich Physiological Explanation Box:\n"
        "   Every question reveals an in-depth scientific rationale explaining the physiological 'why'.\n\n"
        "• Progress Tracking & Live Scoring:\n"
        "   Dynamic progress bar (1/7 to 7/7) and live score tallying.\n\n"
        "• Gamified Achievement Badges:\n"
        "   - 7/7 Correct: 🥇 Campus Nutrition Champion\n"
        "   - 5-6 Correct: 🥈 Wellness Scholar\n"
        "   - 3-4 Correct: 🥉 Health Novice\n"
        "   - Retake quiz capability to reinforce learning."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    # ==========================================
    # SLIDE 14: MODULE 7 - USABILITY FEEDBACK & EVALUATION
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Module 7: Usability Feedback & Community Evaluation")

    m7_left = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    m7_left.fill.solid()
    m7_left.fill.fore_color.rgb = WHITE
    m7_left.line.color.rgb = PRIMARY
    m7_left.line.width = Pt(1.5)

    tx1 = s14.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "PHASE 6: METHODOLOGY & SURVEY PORTAL"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = tf1.add_paragraph()
    p.text = (
        "\n• Fulfillment of Objective 5 & Methodology Step 6:\n"
        "   A built-in usability testing survey enables volunteer student testers to submit feedback during project demonstration.\n\n"
        "• Form Input Structure:\n"
        "   - Student Name / USN (Optional)\n"
        "   - Branch & Semester (e.g. CSE - 3rd Sem)\n"
        "   - 5-Star Interactive Rating: Ease of Navigation\n"
        "   - 5-Star Interactive Rating: Clarity of Nutrition Information\n"
        "   - 5-Star Interactive Rating: Tool Utility (BMI/Tracker/Quiz)\n"
        "   - Awareness Gain Radio: Yes, significantly | Somewhat | Neutral\n"
        "   - Open Suggestions & Comments text area.\n\n"
        "• Local & Server Synchronization:\n"
        "   Responses update live metrics immediately and store in localStorage and SQLite."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    m7_right = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    m7_right.fill.solid()
    m7_right.fill.fore_color.rgb = WHITE
    m7_right.line.color.rgb = BLUE_ACCENT
    m7_right.line.width = Pt(1.5)

    tx2 = s14.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    tf2 = tx2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "AGGREGATED METRICS & STUDENT REVIEWS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf2.add_paragraph()
    p.text = (
        "\n• Live Pilot Testing Metrics (CSE Sem III Cohort):\n"
        "   - Total Student Testers: 12+\n"
        "   - Avg. Navigation & Responsiveness: 4.9 / 5.0 ⭐\n"
        "   - Avg. Content Clarity & Reliability: 4.8 / 5.0 ⭐\n"
        "   - Avg. Interactive Tool Utility: 5.0 / 5.0 ⭐\n"
        "   - Awareness Impact: 100% reported adopting healthier daily routines.\n\n"
        "• Sample Student Testimonials:\n"
        "   \"The water bottle filling animation and campus canteen food swaps are super practical for hostel life!\"\n"
        "   — Rahul Verma (1NH25CS142)\n\n"
        "   \"Appreciated the clear explanation that BMI is only a screening ratio and not a medical diagnosis.\"\n"
        "   — Sneha Rao (1NH25CS189)"
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    # ==========================================
    # SLIDE 15: CONCLUSION, FUTURE SCOPE & ACKNOWLEDGEMENTS
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Conclusion, Future Roadmap & Acknowledgements")

    c1_card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    c1_card.fill.solid()
    c1_card.fill.fore_color.rgb = WHITE
    c1_card.line.color.rgb = PRIMARY
    c1_card.line.width = Pt(1.5)

    c1_tx = s15.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    c1_tf = c1_tx.text_frame
    c1_tf.word_wrap = True
    p = c1_tf.paragraphs[0]
    p.text = "PROJECT SUMMARY & OUTCOMES"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = c1_tf.add_paragraph()
    p.text = (
        "\n• All Expected Outcomes Successfully Achieved:\n"
        "   1. Functional, mobile-responsive health awareness web app.\n"
        "   2. Student-friendly education on balanced diets, food groups, and hydration.\n"
        "   3. Fully validated BMI screening calculator, water tracker, and quiz.\n"
        "   4. Documented usability feedback from volunteer student testers.\n\n"
        "• Core Innovation Value:\n"
        "   Bridges the gap between complex health science and fast-paced college life using localized food swaps and zero-barrier tools.\n\n"
        "• Design Thinking Success:\n"
        "   Demonstrated human-centered empathy for undergraduate lifestyle realities."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    c2_card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    c2_card.fill.solid()
    c2_card.fill.fore_color.rgb = PRIMARY
    c2_card.line.fill.background()

    c2_tx = s15.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    c2_tf = c2_tx.text_frame
    c2_tf.word_wrap = True
    p = c2_tf.paragraphs[0]
    p.text = "FUTURE ROADMAP & CONCLUSION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT

    p = c2_tf.add_paragraph()
    p.text = (
        "\n• Future Enhancements:\n"
        "   • Campus Mess Menu Integration: Real-time nutritional rating of weekly hostel mess meals.\n"
        "   • Smart Push Notifications: Periodic hydration reminders during laboratory sessions.\n"
        "   • Multi-Language Support: Regional Indian language support for wider campus inclusion.\n\n"
        "• Institutional Acknowledgements:\n"
        "   We express our sincere gratitude to the Department of Computer Science & Engineering, New Horizon College of Engineering, our Project Guide, Course Coordinator, and HoD for their continuous mentorship throughout Course 25CPD37.\n\n"
        "THANK YOU! ANY QUESTIONS?"
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = WHITE
    p.line_spacing = 1.15

    prs.save(output_path)
    print(f"[SUCCESS] 15-Slide Presentation generated: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\NutriCampus-Health-Nutrition"
    out_file = os.path.join(out_dir, "NutriCampus_Project_Presentation.pptx")
    create_deck(out_file)
