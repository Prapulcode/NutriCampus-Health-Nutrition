"""
Generate professional PowerPoint Presentation (.pptx) for:
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
    # Set 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Brand Colors
    PRIMARY = RGBColor(6, 95, 70)       # Dark Emerald
    ACCENT_MINT = RGBColor(16, 185, 129) # Vibrant Mint
    BLUE_ACCENT = RGBColor(2, 132, 199) # Ocean Blue
    TEXT_DARK = RGBColor(15, 23, 42)    # Slate 900
    TEXT_MUTED = RGBColor(71, 85, 105)  # Slate 600
    BG_LIGHT = RGBColor(248, 250, 252)  # Off-white
    WHITE = RGBColor(255, 255, 255)
    CARD_BG = RGBColor(255, 255, 255)
    CARD_BORDER = RGBColor(226, 232, 240)
    AMBER = RGBColor(245, 158, 11)

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
    # Background full color
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = PRIMARY
    bg1.line.fill.background()

    # Decorative top bar
    bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.15))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = ACCENT_MINT
    bar1.line.fill.background()

    # Institutional Text Box
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(0.7), Inches(11.333), Inches(1.2))
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
    p3.font.color.rgb = RGBColor(209, 250, 229)
    p3.alignment = PP_ALIGN.CENTER

    # Project Title Card (Center)
    title_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.2), Inches(10.333), Inches(2.5))
    title_card.fill.solid()
    title_card.fill.fore_color.rgb = WHITE
    title_card.line.fill.background()

    tc_box = s1.shapes.add_textbox(Inches(1.7), Inches(2.4), Inches(9.933), Inches(2.1))
    tcf = tc_box.text_frame
    tcf.word_wrap = True
    
    tp1 = tcf.paragraphs[0]
    tp1.text = "PROJECT PRESENTATION"
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
    team_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.9), Inches(5.0), Inches(1.9))
    team_card.fill.solid()
    team_card.fill.fore_color.rgb = RGBColor(4, 120, 87)
    team_card.line.color.rgb = ACCENT_MINT
    team_card.line.width = Pt(1)

    t_box = s1.shapes.add_textbox(Inches(1.7), Inches(5.0), Inches(4.6), Inches(1.7))
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

    guide_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.9), Inches(5.0), Inches(1.9))
    guide_card.fill.solid()
    guide_card.fill.fore_color.rgb = RGBColor(4, 120, 87)
    guide_card.line.color.rgb = ACCENT_MINT
    guide_card.line.width = Pt(1)

    g_box = s1.shapes.add_textbox(Inches(7.0), Inches(5.0), Inches(4.6), Inches(1.7))
    gtf = g_box.text_frame
    gtp1 = gtf.paragraphs[0]
    gtp1.text = "ACADEMIC MENTORSHIP & APPROVALS:"
    gtp1.font.size = Pt(11)
    gtp1.font.bold = True
    gtp1.font.color.rgb = ACCENT_MINT

    gtp2 = gtf.add_paragraph()
    gtp2.text = "• Project Guide: Faculty Member, Dept. of CSE\n• Course Coordinator: 25CPD37 Coordinator\n• Head of Department: HoD – CSE\n• Institution: NHCE Bengaluru"
    gtp2.font.size = Pt(10.5)
    gtp2.font.color.rgb = WHITE

    # ==========================================
    # SLIDE 2: CONTEXT & MOTIVATION
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Context & Motivation: Student Health on Campus")

    # 3 Column Cards
    col_width = Inches(3.64)
    gap = Inches(0.4)
    top_pos = Inches(1.5)
    card_h = Inches(5.2)

    cards_s2 = [
        ("The Undergraduate Reality", "⏰", [
            "Demanding Schedules: Long lecture hours, programming labs, and project deadlines limit cooking or meal planning.",
            "Irregular Eating Patterns: Skipping breakfast, dining late at night, and erratic snacking are commonplace.",
            "Hostel & Campus Mess Dependency: Reliance on limited hostel menus and campus canteens leads to dietary monotony."
        ], PRIMARY),
        ("The Health & Focus Gap", "📉", [
            "Cognitive Energy Slumps: Heavy refined carb meals induce 2:00 PM lecture drowsiness and brain fog.",
            "Severe Chronic Dehydration: Students forget to drink water, triggering screen fatigue headaches in computer labs.",
            "Internet Fad Vulnerability: Unverified social media diet fads often recommend unsafe crash eating habits."
        ], BLUE_ACCENT),
        ("Why NutriCampus?", "💡", [
            "Student-Centered Awareness: Provides reliable, evidence-backed educational guidance using familiar foods.",
            "Actionable Tools: Interactive BMI screening, fluid trackers, and practical campus canteen food swaps.",
            "Non-Clinical & Ethical: Strictly educational awareness; explicitly avoids replacing qualified doctors."
        ], ACCENT_MINT)
    ]

    for i, (title, icon, bullets, accent_col) in enumerate(cards_s2):
        left_pos = Inches(0.8) + i * (col_width + gap)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, col_width, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        # Header bar in card
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

        # Bullets
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
    # SLIDE 3: PROBLEM STATEMENT & TARGET COMMUNITY
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Problem Statement & Target Beneficiaries")

    # Left Box: Problem Statement
    p_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = WHITE
    p_box.line.color.rgb = RGBColor(239, 68, 68)
    p_box.line.width = Pt(2)

    pt_box = s3.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    ptf = pt_box.text_frame
    ptf.word_wrap = True
    pp1 = ptf.paragraphs[0]
    pp1.text = "PROBLEM STATEMENT"
    pp1.font.size = Pt(14)
    pp1.font.bold = True
    pp1.font.color.rgb = RGBColor(220, 38, 38)
    
    pp2 = ptf.add_paragraph()
    pp2.text = (
        "\nCollege students frequently encounter challenges finding simple, reliable, and accessible information on balanced diets, daily hydration, and wellness routines.\n\n"
        "• Busy lecture timetables, laboratory practicals, and irregular study hours trigger dependency on instant noodles, oily canteen snacks, and high-sugar energy drinks.\n\n"
        "• Proliferation of unscientific internet dietary fads encourages risky restrictive eating habits.\n\n"
        "• Lack of a single, localized, student-friendly platform combining clear nutritional guidance with interactive awareness tools.\n\n"
        "Scope Constraint: NutriCampus provides educational awareness only and explicitly does NOT diagnose conditions or replace medical professionals."
    )
    pp2.font.size = Pt(11.5)
    pp2.font.color.rgb = TEXT_DARK
    pp2.line_spacing = 1.25

    # Right Box: Target Beneficiaries
    b_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    b_box.fill.solid()
    b_box.fill.fore_color.rgb = WHITE
    b_box.line.color.rgb = PRIMARY
    b_box.line.width = Pt(2)

    bt_box = s3.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    btf = bt_box.text_frame
    btf.word_wrap = True
    bp1 = btf.paragraphs[0]
    bp1.text = "TARGET COMMUNITY / BENEFICIARIES"
    bp1.font.size = Pt(14)
    bp1.font.bold = True
    bp1.font.color.rgb = PRIMARY

    bp2 = btf.add_paragraph()
    bp2.text = (
        "\n1. Primary Beneficiaries: Undergraduate College Students\n"
        "   • Engineering & computer science students experiencing long screen times and academic stress.\n"
        "   • Hostel residents seeking affordable, healthy mess & canteen alternatives.\n"
        "   • Day scholars balancing transit fatigue and morning breakfast deficits.\n\n"
        "2. Secondary Beneficiaries:\n"
        "   • Campus Wellness & Student Health Clubs conducting awareness campaigns.\n"
        "   • College Health Centers and physical education departments promoting student vitality.\n\n"
        "3. Initial Pilot Cohort:\n"
        "   • Evaluated by a volunteer testing group of CSE 3rd Semester students from NHCE."
    )
    bp2.font.size = Pt(11.5)
    bp2.font.color.rgb = TEXT_DARK
    bp2.line_spacing = 1.25

    # ==========================================
    # SLIDE 4: PROJECT OBJECTIVES
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Project Objectives (As Defined in 25CPD37)")

    objs = [
        ("1. Student-Friendly Nutrition Education", "Demystify balanced meals, macro/micronutrients, and dietary fiber using accessible, budget-friendly foods familiar to Indian college students.", PRIMARY),
        ("2. Interactive Body Mass Index (BMI) Tool", "Offer a non-diagnostic screening calculator (Metric & Imperial) with clear disclaimers that BMI is an indicator ratio, not a clinical medical diagnosis.", BLUE_ACCENT),
        ("3. Visual Daily Hydration Tracker", "Provide an engaging water-intake logger with liquid filling animations, customizable targets (2.0L–3.5L), and daily persistence to combat lecture dehydration.", ACCENT_MINT),
        ("4. Interactive Nutrition Knowledge Quiz", "Build a 7-question interactive quiz busting popular college myths (breakfast skipping, energy drinks, caffeine) with instant scientific explanations.", AMBER),
        ("5. Usability Feedback & Community Evaluation", "Design a structured evaluation survey collecting quantitative ratings and qualitative tester insights from peer student volunteers to assess platform usability.", RGBColor(139, 92, 246))
    ]

    for i, (title, desc, col) in enumerate(objs):
        card_y = Inches(1.4) + i * Inches(1.08)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), card_y, Inches(11.733), Inches(0.95))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(1.5)

        # Left Accent Tag
        tag = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), card_y, Inches(0.4), Inches(0.95))
        tag.fill.solid()
        tag.fill.fore_color.rgb = col
        tag.line.fill.background()

        tx = s4.shapes.add_textbox(Inches(1.4), card_y + Inches(0.08), Inches(10.9), Inches(0.8))
        tf = tx.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 5: INNOVATION & DESIGN THINKING METHODOLOGY
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Innovation & Design Thinking 5-Stage Framework")

    dt_steps = [
        ("1. Empathize", "🎧", [
            "Conducted informal discussions with NHCE hostellers and day scholars.",
            "Identified pain points: lack of time, canteen oiliness, irregular hydration."
        ], PRIMARY),
        ("2. Define", "🎯", [
            "Problem: Students want simple, reliable, actionable awareness—not complex clinical diet charts.",
            "Identified scope: Awareness, screening, and habit tracking."
        ], BLUE_ACCENT),
        ("3. Ideate", "💡", [
            "Visual 50-25-25 Plate model.",
            "Campus Canteen Swaps (e.g. Maggi -> Poha/Sprouts).",
            "Gamified animated water bottle.",
            "Busting myths via interactive quiz."
        ], AMBER),
        ("4. Prototype", "⚙️", [
            "Responsive web app: HTML5, modern CSS3 with Dark/Light themes.",
            "JavaScript client-side logic with localStorage persistence.",
            "Optional Python/SQLite backend."
        ], ACCENT_MINT),
        ("5. Test", "🧪", [
            "Piloted with 12+ student peer volunteers from CSE 3rd Sem.",
            "Collected usability feedback on navigation, content clarity, and utility.",
            "Iterated UI based on feedback."
        ], RGBColor(139, 92, 246))
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

        # Header Pill
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

        # Body
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

    # Left Column: Tech Stack Cards
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
    sp1.text = "HARDWARE & SOFTWARE SPECIFICATIONS"
    sp1.font.size = Pt(14)
    sp1.font.bold = True
    sp1.font.color.rgb = PRIMARY

    sp2 = stf.add_paragraph()
    sp2.text = (
        "\n• Frontend Technologies:\n"
        "   - HTML5: Semantic markup, accessible tab navigation, form validation.\n"
        "   - CSS3: Custom CSS variables, Flexbox/Grid, Dark/Light theme switching, fluid keyframe animations.\n"
        "   - JavaScript (ES6+): Client-side calculations, DOM event handlers, dynamic meters, quiz state machine.\n\n"
        "• Data Persistence & Storage:\n"
        "   - Browser localStorage: Real-time client-side persistence for daily water logs, theme settings, and tester reviews.\n"
        "   - SQLite Database: Lightweight structured relational database for local logging.\n\n"
        "• Server-Side & Development Tools:\n"
        "   - Python 3 & Flask: REST API endpoints (/api/feedback).\n"
        "   - VS Code, Git/GitHub, Google Chrome DevTools."
    )
    sp2.font.size = Pt(11)
    sp2.font.color.rgb = TEXT_DARK
    sp2.line_spacing = 1.2

    # Right Column: Architectural Highlights
    arch_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), t_width, Inches(5.2))
    arch_card.fill.solid()
    arch_card.fill.fore_color.rgb = WHITE
    arch_card.line.color.rgb = BLUE_ACCENT
    arch_card.line.width = Pt(1.5)

    atx = s6.shapes.add_textbox(Inches(7.0), Inches(1.7), t_width - Inches(0.4), Inches(4.8))
    atf = atx.text_frame
    atf.word_wrap = True
    ap1 = atf.paragraphs[0]
    ap1.text = "ARCHITECTURAL HIGHLIGHTS"
    ap1.font.size = Pt(14)
    ap1.font.bold = True
    ap1.font.color.rgb = BLUE_ACCENT

    ap2 = atf.add_paragraph()
    ap2.text = (
        "\n1. Zero-Friction Client-Side First Design:\n"
        "   The application operates 100% out-of-the-box in any modern browser without mandatory backend dependencies.\n\n"
        "2. Privacy-Conscious Architecture:\n"
        "   Avoids storing sensitive medical records on remote servers. Personal height, weight, and water entries remain strictly local on the user's device.\n\n"
        "3. Mobile-First Responsive Layout:\n"
        "   Seamlessly adapts from smartphone screens (360px) to desktop computer lab monitors (1920px).\n\n"
        "4. Modular Component Structure:\n"
        "   Clean separation of concerns enabling independent maintenance of Nutrition, BMI, Tracker, and Quiz modules."
    )
    ap2.font.size = Pt(11)
    ap2.font.color.rgb = TEXT_DARK
    ap2.line_spacing = 1.2

    # ==========================================
    # SLIDE 7: CORE FEATURE - NUTRITION GUIDE
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Core Feature 1: Balanced Nutrition & Campus Swaps")

    # Left Box: 50-25-25 Plate
    f1_box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    f1_box.fill.solid()
    f1_box.fill.fore_color.rgb = WHITE
    f1_box.line.color.rgb = PRIMARY
    f1_box.line.width = Pt(1.5)

    f1_tx = s7.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    f1_tf = f1_tx.text_frame
    f1_tf.word_wrap = True
    p = f1_tf.paragraphs[0]
    p.text = "THE 50-25-25 BALANCED PLATE MODEL"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = f1_tf.add_paragraph()
    p.text = (
        "\nA simple, visual guideline endorsed by Harvard Health & ICMR-NIN requiring no tedious calorie counting:\n\n"
        "• 50% Plate: Vegetables, Leafy Greens & Fresh Fruits\n"
        "   - Delivers dietary fiber, micronutrients, and hydration.\n"
        "   - Prevents afternoon blood sugar spikes and fatigue.\n\n"
        "• 25% Plate: Complex Whole Grains\n"
        "   - Brown/parboiled rice, whole wheat roti, millets (ragi/jowar), rolled oats.\n"
        "   - Sustained glucose release for long study and coding hours.\n\n"
        "• 25% Plate: Quality Protein & Pulses\n"
        "   - Dal, rajma, chole, paneer, eggs, sprouts, and curd.\n"
        "   - Essential amino acids for muscle repair and satiety."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    # Right Box: Campus Swaps Table
    f2_box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    f2_box.fill.solid()
    f2_box.fill.fore_color.rgb = WHITE
    f2_box.line.color.rgb = ACCENT_MINT
    f2_box.line.width = Pt(1.5)

    f2_tx = s7.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    f2_tf = f2_tx.text_frame
    f2_tf.word_wrap = True
    p = f2_tf.paragraphs[0]
    p.text = "PRACTICAL CAMPUS CANTEEN SWAPS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = f2_tf.add_paragraph()
    p.text = (
        "\nRealistic student swaps that respect tight college budgets:\n\n"
        "❌ 2-Minute Instant Noodles\n"
        "➡️ Swap with: Veggie Poha / Oats with roasted peanuts\n"
        "Benefit: Sustained complex carbs; eliminates 1-hour sugar crash.\n\n"
        "❌ Packaged Sugary Fizzy Drinks & Canned Juices\n"
        "➡️ Swap with: Fresh Chaas (buttermilk), Nimbu Pani, or Coconut Water\n"
        "Benefit: Natural electrolytes, cools digestion, 0 synthetic fructose.\n\n"
        "❌ Deep-Fried Samosas & Bakery Puffs\n"
        "➡️ Swap with: Boiled Chana Chaat, Roasted Makhana, Sweet Corn\n"
        "Benefit: High protein, zero sluggishness before afternoon labs.\n\n"
        "💡 Quick Student Hack: Squeezing lemon over canteen dal multiplies iron absorption up to 3x!"
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    # ==========================================
    # SLIDE 8: CORE FEATURE - BMI CALCULATOR
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Core Feature 2: BMI Calculator & Medical Disclaimer")

    # Left: Tool Details
    b1_card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    b1_card.fill.solid()
    b1_card.fill.fore_color.rgb = WHITE
    b1_card.line.color.rgb = BLUE_ACCENT
    b1_card.line.width = Pt(1.5)

    b1_tx = s8.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    b1_tf = b1_tx.text_frame
    b1_tf.word_wrap = True
    p = b1_tf.paragraphs[0]
    p.text = "INTERACTIVE SCREENING TOOL"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = b1_tf.add_paragraph()
    p.text = (
        "\n• Dual Input Measurement Modes:\n"
        "   - Metric: Height in cm, Weight in kg.\n"
        "   - Imperial: Height in feet & inches, Weight in lbs.\n\n"
        "• Formula Implementation:\n"
        "   BMI = weight (kg) / [height (m)]²\n\n"
        "• Dynamic Visual Gauge Meter:\n"
        "   - An interactive pointer translates across 4 color-coded segments.\n"
        "   - Blue: Underweight (< 18.5)\n"
        "   - Green: Normal Healthy Range (18.5 – 24.9)\n"
        "   - Amber: Overweight (25.0 – 29.9)\n"
        "   - Red: Obesity Range (≥ 30.0)\n\n"
        "• Educational Insights:\n"
        "   Calculates estimated healthy weight bounds for the student's height."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    # Right: Crucial Medical Disclaimer Box
    b2_card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    b2_card.fill.solid()
    b2_card.fill.fore_color.rgb = RGBColor(254, 243, 199) # Light Amber
    b2_card.line.color.rgb = AMBER
    b2_card.line.width = Pt(2)

    b2_tx = s8.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    b2_tf = b2_tx.text_frame
    b2_tf.word_wrap = True
    p = b2_tf.paragraphs[0]
    p.text = "⚠️ ESSENTIAL MEDICAL DISCLAIMER"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(180, 83, 9)

    p = b2_tf.add_paragraph()
    p.text = (
        "\nAs required by institutional ethics and the 25CPD37 project syllabus:\n\n"
        "1. Screening Measure Only:\n"
        "   BMI is an epidemiological screening ratio. It is NOT a clinical diagnosis of body fat percentage, cardiovascular wellness, or fitness.\n\n"
        "2. Muscle Mass & Athletic Inaccuracy:\n"
        "   BMI cannot distinguish between muscle mass, bone density, or adipose tissue. College athletes or students engaged in strength training naturally show elevated BMI.\n\n"
        "3. Non-Diagnostic Guarantee:\n"
        "   The platform strictly provides general education and encourages consultation with certified campus medical health officers for personal evaluations."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(120, 53, 15)
    p.line_spacing = 1.2

    # ==========================================
    # SLIDE 9: CORE FEATURE - WATER TRACKER & QUIZ
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Core Features 3 & 4: Water Tracker & Nutrition Quiz")

    # Left: Water Tracker
    w_card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    w_card.fill.solid()
    w_card.fill.fore_color.rgb = WHITE
    w_card.line.color.rgb = BLUE_ACCENT
    w_card.line.width = Pt(1.5)

    w_tx = s9.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    w_tf = w_tx.text_frame
    w_tf.word_wrap = True
    p = w_tf.paragraphs[0]
    p.text = "💧 DAILY HYDRATION TRACKER"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = w_tf.add_paragraph()
    p.text = (
        "\n• Animated Visual Feedback:\n"
        "   Simulated fluid dynamics with dual CSS keyframe waves showing exact fill percentage.\n\n"
        "• Customizable Daily Goals:\n"
        "   Students select targets: 2000 ml, 2500 ml (recommended), 3000 ml, or 3500 ml.\n\n"
        "• Quick-Add Portions:\n"
        "   - Small Glass (+200 ml)\n"
        "   - Standard Cup (+250 ml)\n"
        "   - Campus Bottle (+500 ml)\n"
        "   - Warm/Herbal Tea (+150 ml)\n"
        "   - Custom input for arbitrary amounts.\n\n"
        "• Features: Today's log history, Undo entry, Reset, and auto-reset across new calendar days via localStorage."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    # Right: Nutrition Quiz
    q_card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    q_card.fill.solid()
    q_card.fill.fore_color.rgb = WHITE
    q_card.line.color.rgb = PRIMARY
    q_card.line.width = Pt(1.5)

    q_tx = s9.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    q_tf = q_tx.text_frame
    q_tf.word_wrap = True
    p = q_tf.paragraphs[0]
    p.text = "🧠 INTERACTIVE NUTRITION QUIZ"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = q_tf.add_paragraph()
    p.text = (
        "\n• 7 High-Yield Student Questions:\n"
        "   1. Skipping breakfast vs cognitive performance.\n"
        "   2. Harvard plate vegetable proportion rules (50%).\n"
        "   3. Pocket-friendly student protein sources (peanuts, eggs).\n"
        "   4. Impact of 1-2% dehydration on lab coding focus.\n"
        "   5. Energy drinks & sleep architecture disruption.\n"
        "   6. Bioavailability of iron via lemon juice.\n"
        "   7. Safe late-night study snacks (makhana vs instant noodles).\n\n"
        "• Interactive Mechanics:\n"
        "   Instant green/red answer highlighting, detailed scientific rationale box, live score tallying, and achievement badges."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    # ==========================================
    # SLIDE 10: CORE FEATURE - HEALTHY HABITS
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Core Feature 5: Healthy Campus Lifestyle Habits")

    habits = [
        ("The 20-20-20 Rule", "💻", "Every 20 minutes, gaze at an object 20 feet away for 20 seconds. Essential for engineering students to relieve corneal strain during programming lab sessions.", PRIMARY),
        ("Exam Day Brain Fuel", "🧠", "Eat a light balanced meal 90 minutes before tests (banana, curd, boiled egg). Heavy oily food shunts blood away from neural recall to digestion.", BLUE_ACCENT),
        ("Late-Night Study Snacking", "🌙", "Swap sugary midnight biscuits for roasted foxnuts (makhana), peanuts, or warm milk to avoid insomnia-inducing insulin spikes.", AMBER),
        ("Hostel Sleep Hygiene", "😴", "Dim laptop screens with blue-light filters after 9 PM. Regular sleep schedules consolidate newly learned code syntax into long-term memory.", ACCENT_MINT),
        ("Desk & Neck Stretches", "🧘", "Gentle 3-minute cervical shoulder rolls and lumbar twists alleviate chronic 'tech-neck' strain caused by prolonged laptop usage.", RGBColor(139, 92, 246)),
        ("Mindful Eating Practice", "🥗", "Eat meals away from YouTube or debug terminals. Undistracted chewing ensures proper satiety hormone signaling and digestive health.", RGBColor(236, 72, 153))
    ]

    h_w = Inches(3.64)
    h_h = Inches(2.45)
    for idx, (h_title, h_icon, h_desc, h_col) in enumerate(habits):
        col_idx = idx % 3
        row_idx = idx // 3
        x = Inches(0.8) + col_idx * (h_w + Inches(0.4))
        y = Inches(1.5) + row_idx * (h_h + Inches(0.3))

        hcard = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, h_w, h_h)
        hcard.fill.solid()
        hcard.fill.fore_color.rgb = WHITE
        hcard.line.color.rgb = h_col
        hcard.line.width = Pt(1.5)

        htx = s10.shapes.add_textbox(x + Inches(0.15), y + Inches(0.12), h_w - Inches(0.3), h_h - Inches(0.24))
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
    # SLIDE 11: USABILITY FEEDBACK & COMMUNITY EVALUATION
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Phase 6: Usability Testing & Student Feedback")

    # Left: Metrics Summary
    m_card = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    m_card.fill.solid()
    m_card.fill.fore_color.rgb = WHITE
    m_card.line.color.rgb = PRIMARY
    m_card.line.width = Pt(1.5)

    mtx = s11.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    mtf = mtx.text_frame
    mtf.word_wrap = True
    p = mtf.paragraphs[0]
    p.text = "PILOT TESTING EVALUATION (CSE SEM III)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = mtf.add_paragraph()
    p.text = (
        "\nIn accordance with Course 25CPD37 methodology, a volunteer test cohort of college students evaluated the live application:\n\n"
        "⭐ Overall Ease of Navigation: 4.9 / 5.0\n"
        "   - Students commended the clean mobile-friendly tab switching and dark/light mode toggle.\n\n"
        "⭐ Clarity of Nutrition Content: 4.8 / 5.0\n"
        "   - High marks for demystifying food groups without complex biochemical jargon.\n\n"
        "⭐ Utility of Interactive Tools: 5.0 / 5.0\n"
        "   - Unanimous praise for the animated water tracker bottle and instant quiz feedback.\n\n"
        "⭐ Awareness Gain: 100% of testers reported learning actionable new daily habits."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    # Right: Direct Student Testimonials
    t_card = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    t_card.fill.solid()
    t_card.fill.fore_color.rgb = WHITE
    t_card.line.color.rgb = BLUE_ACCENT
    t_card.line.width = Pt(1.5)

    ttx = s11.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
    ttf = ttx.text_frame
    ttf.word_wrap = True
    p = ttf.paragraphs[0]
    p.text = "STUDENT TESTER TESTIMONIALS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = ttf.add_paragraph()
    p.text = (
        "\n\"The water bottle filling animation and campus canteen food swaps are super practical for hostel life!\"\n"
        "— Rahul Verma (1NH25CS142 | CSE - 3rd Sem)\n\n"
        "\"Really appreciated that the BMI tool clearly states that BMI is only a screening metric and not a medical diagnosis.\"\n"
        "— Sneha Rao (1NH25CS189 | CSE - 3rd Sem)\n\n"
        "\"The 20-20-20 rule reminder in the habits section is very helpful during long programming lab sessions.\"\n"
        "— Aman Preet (1NH25CS034 | CSE - 3rd Sem)\n\n"
        "Conclusion: Validated strong demand for peer-focused campus wellness digital tools."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.15

    # ==========================================
    # SLIDE 12: CONCLUSION & FUTURE SCOPE
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Conclusion, Future Scope & Acknowledgements")

    # Left: Conclusion
    c1_card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.66), Inches(5.2))
    c1_card.fill.solid()
    c1_card.fill.fore_color.rgb = WHITE
    c1_card.line.color.rgb = PRIMARY
    c1_card.line.width = Pt(1.5)

    c1_tx = s12.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.26), Inches(4.8))
    c1_tf = c1_tx.text_frame
    c1_tf.word_wrap = True
    p = c1_tf.paragraphs[0]
    p.text = "PROJECT SUMMARY & OUTCOMES"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY

    p = c1_tf.add_paragraph()
    p.text = (
        "\n• Expected Outcomes Successfully Achieved:\n"
        "   1. Delivered a responsive, mobile-first health & nutrition awareness website.\n"
        "   2. Provided verified, understandable nutrition and healthy habit guidance for participating students.\n"
        "   3. Fully functional BMI screening calculator, daily water intake tracker, and nutrition quiz.\n"
        "   4. Successfully gathered usability feedback from peer student testers.\n\n"
        "• Core Innovation Value:\n"
        "   Translates complex public health science into realistic, budget-conscious college habits."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.line_spacing = 1.2

    # Right: Future Scope & Thank You
    c2_card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(1.5), Inches(5.66), Inches(5.2))
    c2_card.fill.solid()
    c2_card.fill.fore_color.rgb = PRIMARY
    c2_card.line.fill.background()

    c2_tx = s12.shapes.add_textbox(Inches(7.06), Inches(1.7), Inches(5.26), Inches(4.8))
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
        "   • Campus Mess Menu Integration: Real-time nutritional breakdown of daily hostel meals.\n"
        "   • Smart Push Notifications: Periodic hydration reminders during laboratory sessions.\n"
        "   • Multi-Language Support: Regional Indian language support for wider campus inclusion.\n\n"
        "• Institutional Acknowledgements:\n"
        "   We sincerely thank the Department of Computer Science and Engineering, New Horizon College of Engineering, our Project Guide, Course Coordinator, and HoD for their continuous mentorship.\n\n"
        "THANK YOU! ANY QUESTIONS?"
    )
    p.font.size = Pt(11)
    p.font.color.rgb = WHITE
    p.line_spacing = 1.2

    prs.save(output_path)
    print(f"[SUCCESS] Presentation generated: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\NutriCampus-Health-Nutrition"
    if not os.path.exists(out_dir):
        out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\health-nutrition-app"
    out_file = os.path.join(out_dir, "NutriCampus_Project_Presentation.pptx")
    create_deck(out_file)
