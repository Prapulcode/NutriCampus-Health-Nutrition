#!/usr/bin/env python3
"""
NutriCampus - Compact 5-Slide SRS Presentation Generator
Standard: Formatted strictly according to the 5-Slide SRS Presentation Deck Structure
Course: 25CPD37 - Community Project using Innovation & Design Thinking
Department of Computer Science & Engineering, New Horizon College of Engineering (NHCE)
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_5slide_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    PRIMARY = RGBColor(6, 95, 70)          # Emerald Green (#065F46)
    PRIMARY_LIGHT = RGBColor(209, 250, 229) # Mint 100 (#D1FAE5)
    ACCENT_MINT = RGBColor(16, 185, 129)    # Mint 500 (#10B981)
    BLUE_ACCENT = RGBColor(2, 132, 199)    # Ocean Blue (#0284C7)
    BLUE_LIGHT = RGBColor(224, 242, 254)   # Sky 100 (#E0F2FE)
    TEXT_DARK = RGBColor(15, 23, 42)       # Slate 900 (#0F172A)
    TEXT_MUTED = RGBColor(71, 85, 105)     # Slate 600 (#475569)
    WHITE = RGBColor(255, 255, 255)
    CARD_BG = RGBColor(255, 255, 255)
    CARD_BORDER = RGBColor(226, 232, 240)  # Slate 200
    AMBER = RGBColor(217, 119, 6)          # Amber (#D97706)
    AMBER_LIGHT = RGBColor(254, 243, 199)  # Amber 100 (#FEF3C7)

    def add_header(slide, title, category="SRS DECK • COURSE 25CPD37 (NHCE CSE)"):
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
        tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        p_f.text = "New Horizon College of Engineering | Dept of CSE | Course 25CPD37 | NutriCampus Web Application"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = TEXT_MUTED

    def setup_card_tf(tf):
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)
        tf.margin_bottom = Inches(0.2)

    def add_para(tf, text, pt_size=12, bold=False, color=TEXT_DARK, space_after=6, bullet=False):
        if len(tf.paragraphs) == 1 and tf.paragraphs[0].text == "":
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = ("• " + text) if bullet else text
        p.font.size = Pt(pt_size)
        p.font.bold = bold
        p.font.color.rgb = color
        p.space_after = Pt(space_after)
        return p

    def set_speaker_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = notes_text

    card_top = Inches(1.4)
    card_h = Inches(5.35)
    w_half = Inches(5.66)
    left_col = Inches(0.8)
    right_col = Inches(6.86)

    # =========================================================================
    # SLIDE 1: Title & Problem Overview
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)

    # Top Banner
    b1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.8))
    b1.fill.solid()
    b1.fill.fore_color.rgb = PRIMARY
    b1.line.fill.background()

    tx1 = s1.shapes.add_textbox(Inches(0.8), Inches(0.25), Inches(11.733), Inches(0.4))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "NEW HORIZON COLLEGE OF ENGINEERING • DEPARTMENT OF CSE"
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_MINT

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "NutriCampus: Health & Nutrition Web Application"
    p1_sub.font.size = Pt(26)
    p1_sub.font.bold = True
    p1_sub.font.color.rgb = WHITE
    p1_sub.space_after = Pt(4)

    p1_desc = tf1.add_paragraph()
    p1_desc.text = "Software Requirements Specification (SRS) Deck • Course 25CPD37: Community Project using Innovation & Design Thinking"
    p1_desc.font.size = Pt(11)
    p1_desc.font.color.rgb = PRIMARY_LIGHT

    # Two Cards on Slide 1
    # Card 1: Problem Overview
    c1_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, Inches(2.1), w_half, Inches(4.7))
    c1_shape.fill.solid()
    c1_shape.fill.fore_color.rgb = WHITE
    c1_shape.line.color.rgb = CARD_BORDER
    c1_shape.line.width = Pt(1.5)

    tx_c1 = s1.shapes.add_textbox(left_col, Inches(2.1), w_half, Inches(4.7))
    tf_c1 = tx_c1.text_frame
    setup_card_tf(tf_c1)
    add_para(tf_c1, "🚨 Real-World Problem Overview", pt_size=16, bold=True, color=PRIMARY, space_after=12)
    add_para(tf_c1, "1-Sentence Problem Statement:", pt_size=12, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_c1, "\"Undergraduate students face irregular eating schedules, chronic lab dehydration, and high reliance on nutrient-poor canteen snacks with zero accessible guidance.\"", pt_size=12, bold=False, color=TEXT_MUTED, space_after=14)
    add_para(tf_c1, "Core Pain Points Identified:", pt_size=12, bold=True, color=TEXT_DARK, space_after=6)
    add_para(tf_c1, "Irregular meal hours during coding labs", pt_size=11.5, bullet=True, space_after=4)
    add_para(tf_c1, "Heavy canteen fried snacks and sodas", pt_size=11.5, bullet=True, space_after=4)
    add_para(tf_c1, "Afternoon brain fog and low daily hydration", pt_size=11.5, bullet=True, space_after=4)
    add_para(tf_c1, "Clinical nutrition tools are complex and intimidating", pt_size=11.5, bullet=True, space_after=6)

    # Card 2: Core System Goal
    c2_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, Inches(2.1), w_half, Inches(4.7))
    c2_shape.fill.solid()
    c2_shape.fill.fore_color.rgb = WHITE
    c2_shape.line.color.rgb = BLUE_ACCENT
    c2_shape.line.width = Pt(1.5)

    tx_c2 = s1.shapes.add_textbox(right_col, Inches(2.1), w_half, Inches(4.7))
    tf_c2 = tx_c2.text_frame
    setup_card_tf(tf_c2)
    add_para(tf_c2, "🎯 Core System Goal & Value", pt_size=16, bold=True, color=BLUE_ACCENT, space_after=12)
    add_para(tf_c2, "System Vision:", pt_size=12, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_c2, "\"Deliver a lightweight, zero-barrier responsive web application translating complex nutrition into realistic food swaps, hydration tracking, and screening.\"", pt_size=12, bold=False, color=TEXT_MUTED, space_after=14)
    add_para(tf_c2, "Key Solution Highlights:", pt_size=12, bold=True, color=TEXT_DARK, space_after=6)
    add_para(tf_c2, "100% Zero-install single page web architecture", pt_size=11.5, bullet=True, space_after=4)
    add_para(tf_c2, "Intuitive 50-25-25 balanced visual plate guide", pt_size=11.5, bullet=True, space_after=4)
    add_para(tf_c2, "Safe hydration tracking capped at 5.0 Liters", pt_size=11.5, bullet=True, space_after=4)
    add_para(tf_c2, "Validated non-diagnostic medical screening boundary", pt_size=11.5, bullet=True, space_after=6)

    # Slide 1 Footer
    f1_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.02))
    f1_line.fill.solid()
    f1_line.fill.fore_color.rgb = CARD_BORDER
    f1_line.line.fill.background()
    tx_f1 = s1.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.733), Inches(0.3))
    tx_f1.text_frame.paragraphs[0].text = "Project Team: CSE 3rd Sem Cohort | Guide & Evaluators: Department of Computer Science & Engineering, NHCE"
    tx_f1.text_frame.paragraphs[0].font.size = Pt(9)
    tx_f1.text_frame.paragraphs[0].font.color.rgb = TEXT_MUTED

    set_speaker_notes(s1,
        "WHAT TO SAY OUT LOUD:\n"
        "\"Good morning respected evaluators and faculty. We are presenting the Software Requirements Specification for NutriCampus, "
        "our community project under Course 25CPD37.\n\n"
        "Undergraduate students at NHCE routinely encounter irregular eating routines, afternoon fatigue, and heavy canteen snack reliance. "
        "Our system provides a zero-barrier, mobile-responsive web tool that translates complex health science into practical food swaps, "
        "safe hydration tracking, and non-diagnostic health screening.\""
    )

    # =========================================================================
    # SLIDE 2: Scope & Target Users
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Slide 2: Scope & Target Users")

    # Left Column: Scope Boundaries
    s2_left = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s2_left.fill.solid()
    s2_left.fill.fore_color.rgb = WHITE
    s2_left.line.color.rgb = PRIMARY
    s2_left.line.width = Pt(1.5)

    tx_s2_l = s2.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s2_l = tx_s2_l.text_frame
    setup_card_tf(tf_s2_l)
    add_para(tf_s2_l, "📌 Project Scope Boundaries", pt_size=15, bold=True, color=PRIMARY, space_after=10)

    add_para(tf_s2_l, "In Scope (Version 1.0 Release):", pt_size=12, bold=True, color=PRIMARY, space_after=4)
    add_para(tf_s2_l, "50-25-25 visual balanced meal guide", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s2_l, "Practical Indian canteen food swaps", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s2_l, "Anthropometric BMI screening calculator", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s2_l, "Fluid water tracker with 5.0 L safety limit", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s2_l, "7-question gamified myth-busting quiz", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s2_l, "Usability survey & community evaluation portal", pt_size=11, bullet=True, space_after=8)

    add_para(tf_s2_l, "Out of Scope (Explicit Exclusions):", pt_size=12, bold=True, color=AMBER, space_after=4)
    add_para(tf_s2_l, "No clinical medical diagnosis or prescriptions", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s2_l, "No calorie counting or strict diet regimes", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s2_l, "No external hardware or wearable sensors", pt_size=11, bullet=True, space_after=3)

    # Right Column: Target Users & Roles
    s2_right = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s2_right.fill.solid()
    s2_right.fill.fore_color.rgb = WHITE
    s2_right.line.color.rgb = BLUE_ACCENT
    s2_right.line.width = Pt(1.5)

    tx_s2_r = s2.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s2_r = tx_s2_r.text_frame
    setup_card_tf(tf_s2_r)
    add_para(tf_s2_r, "👥 Target Users & Key Roles", pt_size=15, bold=True, color=BLUE_ACCENT, space_after=10)

    add_para(tf_s2_r, "Primary Users:", pt_size=12, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_s2_r, "Hostel Residents & Commuter Students: Budget food swaps and meal portioning.", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_r, "Engineering Lab Students: Screen fatigue relief (20-20-20 rule) and hydration.", pt_size=10.5, bullet=True, space_after=8)

    add_para(tf_s2_r, "Evaluation Roles:", pt_size=12, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_s2_r, "Peer Student Reviewers: 12+ CSE students testing usability and logging reviews.", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_r, "Faculty Evaluators: Reviewing Design Thinking steps and requirements compliance.", pt_size=10.5, bullet=True, space_after=8)

    add_para(tf_s2_r, "User Environment:", pt_size=12, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_s2_r, "Mobile smartphones (Android/iOS) & desktop browsers (Chrome, Edge, Firefox).", pt_size=10.5, bullet=True, space_after=3)

    set_speaker_notes(s2,
        "WHAT TO SAY OUT LOUD:\n"
        "\"In Slide 2, we define who uses our system and draw a clear boundary around v1 capabilities.\n\n"
        "In Scope, we implement six core awareness modules: visual meal ratios, canteen swaps, metric BMI screening, "
        "a hydration tracker strictly limited to 5 liters, interactive quizzes, and community feedback.\n\n"
        "Out of Scope, we strictly exclude clinical medical diagnoses, calorie counting, or hardware sensors. "
        "Our target users are undergraduate students, hostelites, lab programmers, and our peer evaluation cohort.\""
    )

    # =========================================================================
    # SLIDE 3: Functional Requirements & Diagram
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Slide 3: Functional Requirements & Architecture")

    # Left Column: Use-Case & Flow Architecture
    s3_left = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s3_left.fill.solid()
    s3_left.fill.fore_color.rgb = WHITE
    s3_left.line.color.rgb = BLUE_ACCENT
    s3_left.line.width = Pt(1.5)

    tx_s3_l = s3.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s3_l = tx_s3_l.text_frame
    setup_card_tf(tf_s3_l)
    add_para(tf_s3_l, "🏗️ Use-Case & System Architecture", pt_size=15, bold=True, color=BLUE_ACCENT, space_after=10)

    # Visual Flow Diagram Blocks
    add_para(tf_s3_l, "System Architecture Pipeline:", pt_size=12, bold=True, color=TEXT_DARK, space_after=6)
    
    # Flow Box 1
    add_para(tf_s3_l, "1. USER INTERACTION (Student / Peer Reviewer)", pt_size=10.5, bold=True, color=PRIMARY, space_after=1)
    add_para(tf_s3_l, "   Responsive Web UI: Navigation, Calculators, Tracker, Quiz", pt_size=9.5, color=TEXT_MUTED, space_after=5)

    # Flow Box 2
    add_para(tf_s3_l, "2. CLIENT-SIDE CONTROLLER (Vanilla JavaScript)", pt_size=10.5, bold=True, color=BLUE_ACCENT, space_after=1)
    add_para(tf_s3_l, "   Quetelet BMI Engine • 5L Fluid Clamping • Instant Quiz Logic", pt_size=9.5, color=TEXT_MUTED, space_after=5)

    # Flow Box 3
    add_para(tf_s3_l, "3. STORAGE & DUAL-TIER PERSISTENCE", pt_size=10.5, bold=True, color=PRIMARY, space_after=1)
    add_para(tf_s3_l, "   • Browser localStorage: Offline hydration logs & state", pt_size=9.5, color=TEXT_MUTED, space_after=1)
    add_para(tf_s3_l, "   • Python/Flask REST API: Asynchronous feedback sync", pt_size=9.5, color=TEXT_MUTED, space_after=1)
    add_para(tf_s3_l, "   • SQLite Database (health_nutrition.db): Pilot evaluations", pt_size=9.5, color=TEXT_MUTED, space_after=8)

    add_para(tf_s3_l, "Key Architecture Advantage:", pt_size=11, bold=True, color=TEXT_DARK, space_after=2)
    add_para(tf_s3_l, "Works 100% offline in any browser; seamlessly syncs when connected.", pt_size=10, color=PRIMARY, space_after=3)

    # Right Column: Top Core Features
    s3_right = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s3_right.fill.solid()
    s3_right.fill.fore_color.rgb = WHITE
    s3_right.line.color.rgb = PRIMARY
    s3_right.line.width = Pt(1.5)

    tx_s3_r = s3.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s3_r = tx_s3_r.text_frame
    setup_card_tf(tf_s3_r)
    add_para(tf_s3_r, "⚡ Top 5 Core Functional Requirements", pt_size=15, bold=True, color=PRIMARY, space_after=10)

    add_para(tf_s3_r, "1. FR-1: 50-25-25 Balanced Plate Visualizer", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=2)
    add_para(tf_s3_r, "Interactive meal portions: 50% fiber/veggies, 25% complex carbs, 25% lean protein.", pt_size=10, space_after=5)

    add_para(tf_s3_r, "2. FR-2: Campus Canteen & Food Swaps", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=2)
    add_para(tf_s3_r, "Evidence-based swaps for instant noodles, sugary sodas, and fried snacks.", pt_size=10, space_after=5)

    add_para(tf_s3_r, "3. FR-3: Anthropometric BMI Screening", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=2)
    add_para(tf_s3_r, "Metric/Imperial Quetelet calculation with color gauge & mandatory medical disclaimer.", pt_size=10, space_after=5)

    add_para(tf_s3_r, "4. FR-4: Hydration Tracker with 5.0 L Limit", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=2)
    add_para(tf_s3_r, "Animated fluid bottle with strict 5000 mL daily safety cap to prevent hyponatremia.", pt_size=10, space_after=5)

    add_para(tf_s3_r, "5. FR-5: Quiz & Community Feedback Portal", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=2)
    add_para(tf_s3_r, "Gamified myth-busting badges and rating-free peer usability evaluation.", pt_size=10, space_after=3)

    set_speaker_notes(s3,
        "WHAT TO SAY OUT LOUD:\n"
        "\"Slide 3 presents our system architecture and primary functional requirements.\n\n"
        "On the left, the architecture flow shows our dual-tier structure: user interactions run in a pure HTML/JS frontend, "
        "persisting data to browser localStorage for offline reliability, with an optional Python SQLite backend for survey aggregation.\n\n"
        "On the right are our top 5 functional requirements: the 50-25-25 plate model, canteen swaps, metric BMI screening, "
        "a safe hydration tracker capped at 5 liters, and our gamified quiz and community survey.\""
    )

    # =========================================================================
    # SLIDE 4: Non-Functional Requirements & Constraints
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Slide 4: Non-Functional Requirements & Constraints")

    # Left Column: Performance & Security
    s4_left = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s4_left.fill.solid()
    s4_left.fill.fore_color.rgb = WHITE
    s4_left.line.color.rgb = PRIMARY
    s4_left.line.width = Pt(1.5)

    tx_s4_l = s4.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s4_l = tx_s4_l.text_frame
    setup_card_tf(tf_s4_l)
    add_para(tf_s4_l, "🛡️ Quality Standards & Security", pt_size=15, bold=True, color=PRIMARY, space_after=10)

    add_para(tf_s4_l, "Performance Standards:", pt_size=12, bold=True, color=PRIMARY, space_after=4)
    add_para(tf_s4_l, "Page load under 1.5 seconds on 4G", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s4_l, "Lightweight bundle under 150 KB total", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s4_l, "Instant client calculations under 16 ms", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s4_l, "Zero external CSS/JS framework bloat", pt_size=11, bullet=True, space_after=8)

    add_para(tf_s4_l, "Security & Privacy Standards:", pt_size=12, bold=True, color=BLUE_ACCENT, space_after=4)
    add_para(tf_s4_l, "Zero mandatory personal information collection", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s4_l, "No passwords or user accounts required", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s4_l, "Parameterized SQL statements prevent injection", pt_size=11, bullet=True, space_after=3)
    add_para(tf_s4_l, "Strict HTML sanitization blocks XSS attacks", pt_size=11, bullet=True, space_after=3)

    # Right Column: Constraints & Medical Ethics
    s4_right = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s4_right.fill.solid()
    s4_right.fill.fore_color.rgb = WHITE
    s4_right.line.color.rgb = AMBER
    s4_right.line.width = Pt(1.5)

    tx_s4_r = s4.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s4_r = tx_s4_r.text_frame
    setup_card_tf(tf_s4_r)
    add_para(tf_s4_r, "⚙️ Constraints & Ethical Boundary", pt_size=15, bold=True, color=AMBER, space_after=10)

    add_para(tf_s4_r, "Technical & Platform Constraints:", pt_size=12, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_s4_r, "Cross-browser execution (Chrome, Safari, Edge, Firefox)", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_r, "Responsive viewports: 360px mobile to 4K desktop", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_r, "Dual deployment: zero-dependency local server & Vercel edge", pt_size=10.5, bullet=True, space_after=8)

    add_para(tf_s4_r, "Mandatory Medical Ethics Boundary:", pt_size=12, bold=True, color=AMBER, space_after=4)
    add_para(tf_s4_r, "Strictly educational health awareness platform", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_r, "BMI defined as screening ratio, not diagnostic tool", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_r, "Prominent amber disclaimers visible on all screening views", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_r, "Water tracker enforces 5.0 L daily safety limit", pt_size=10.5, bullet=True, space_after=3)

    set_speaker_notes(s4,
        "WHAT TO SAY OUT LOUD:\n"
        "\"Slide 4 highlights our Non-Functional Requirements and system constraints.\n\n"
        "On performance and security: NutriCampus loads in under 1.5 seconds with an asset footprint under 150 KB. "
        "We collect zero sensitive user data, require no passwords, and use parameterized SQL to guarantee security.\n\n"
        "On constraints and ethics: The application is cross-browser compliant and works without installation. "
        "Most importantly, we maintain a strict medical boundary—prominently displaying disclaimers so users understand "
        "that NutriCampus provides educational awareness and screening, not medical diagnoses.\""
    )

    # =========================================================================
    # SLIDE 5: Summary & Q&A
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Slide 5: Summary & Key Takeaways", category="PROJECT WRAP-UP • COURSE 25CPD37")

    # 3 Summary Cards
    card_w3 = Inches(3.64)
    c1_x = Inches(0.8)
    c2_x = Inches(4.84)
    c3_x = Inches(8.88)
    h_top = Inches(1.4)
    card_h3 = Inches(3.8)

    # Card 1: Design Thinking
    box1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x, h_top, card_w3, card_h3)
    box1.fill.solid()
    box1.fill.fore_color.rgb = WHITE
    box1.line.color.rgb = PRIMARY
    box1.line.width = Pt(1.5)

    tx_b1 = s5.shapes.add_textbox(c1_x, h_top, card_w3, card_h3)
    tf_b1 = tx_b1.text_frame
    setup_card_tf(tf_b1)
    add_para(tf_b1, "💡 1. Human-Centered", pt_size=14, bold=True, color=PRIMARY, space_after=8)
    add_para(tf_b1, "Design Thinking:", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_b1, "Directly fulfills Course 25CPD37 5-stage framework (Empathize, Define, Ideate, Prototype, Test).", pt_size=10.5, space_after=8)
    add_para(tf_b1, "Undergraduate Reality:", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_b1, "Built specifically for hostel schedules, coding lab eye strain, and campus meals.", pt_size=10.5, space_after=2)

    # Card 2: Zero-Barrier
    box2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x, h_top, card_w3, card_h3)
    box2.fill.solid()
    box2.fill.fore_color.rgb = WHITE
    box2.line.color.rgb = BLUE_ACCENT
    box2.line.width = Pt(1.5)

    tx_b2 = s5.shapes.add_textbox(c2_x, h_top, card_w3, card_h3)
    tf_b2 = tx_b2.text_frame
    setup_card_tf(tf_b2)
    add_para(tf_b2, "🚀 2. Zero-Barrier Access", pt_size=14, bold=True, color=BLUE_ACCENT, space_after=8)
    add_para(tf_b2, "Accessible Anywhere:", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_b2, "No app stores, no signups, no installations. Immediate access via any mobile or PC browser.", pt_size=10.5, space_after=8)
    add_para(tf_b2, "Dual Deployment:", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_b2, "Zero-dependency local Python server + production cloud deployment on Vercel.", pt_size=10.5, space_after=2)

    # Card 3: Validated Community Impact
    box3 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x, h_top, card_w3, card_h3)
    box3.fill.solid()
    box3.fill.fore_color.rgb = WHITE
    box3.line.color.rgb = PRIMARY
    box3.line.width = Pt(1.5)

    tx_b3 = s5.shapes.add_textbox(c3_x, h_top, card_w3, card_h3)
    tf_b3 = tx_b3.text_frame
    setup_card_tf(tf_b3)
    add_para(tf_b3, "📈 3. Validated Impact", pt_size=14, bold=True, color=PRIMARY, space_after=8)
    add_para(tf_b3, "Peer Review Testing:", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_b3, "12+ CSE 3rd Sem volunteer student testers completed Phase 6 usability evaluation.", pt_size=10.5, space_after=8)
    add_para(tf_b3, "Empirical Outcomes:", pt_size=11.5, bold=True, color=TEXT_DARK, space_after=4)
    add_para(tf_b3, "100% reported positive awareness adoption; 0 crashes or unhandled client exceptions.", pt_size=10.5, space_after=2)

    # Bottom Callout: Questions & Live Link
    bottom_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.4), Inches(11.733), Inches(1.4))
    bottom_box.fill.solid()
    bottom_box.fill.fore_color.rgb = PRIMARY
    bottom_box.line.fill.background()

    tx_bottom = s5.shapes.add_textbox(Inches(0.8), Inches(5.4), Inches(11.733), Inches(1.4))
    tf_bottom = tx_bottom.text_frame
    setup_card_tf(tf_bottom)
    
    p_q = tf_bottom.paragraphs[0]
    p_q.text = "❓ THANK YOU! ANY QUESTIONS OR FEEDBACK?"
    p_q.font.size = Pt(16)
    p_q.font.bold = True
    p_q.font.color.rgb = ACCENT_MINT
    p_q.alignment = PP_ALIGN.CENTER
    p_q.space_after = Pt(4)

    p_link = tf_bottom.add_paragraph()
    p_link.text = "Live Demo: https://nutri-campus-health-nutrition.vercel.app  •  GitHub: github.com/Prapulcode/NutriCampus-Health-Nutrition"
    p_link.font.size = Pt(11)
    p_link.font.color.rgb = WHITE
    p_link.alignment = PP_ALIGN.CENTER

    set_speaker_notes(s5,
        "WHAT TO SAY OUT LOUD:\n"
        "\"To wrap up our presentation in 20 seconds:\n"
        "1. NutriCampus demonstrates human-centered Design Thinking for undergraduate student wellness.\n"
        "2. It provides zero-barrier accessibility, functioning offline and in the cloud with zero downloads.\n"
        "3. It has been empirically validated through our pilot study with 12 peer evaluators.\n\n"
        "Thank you respected faculty and evaluators. We now open the floor for your questions!\""
    )

    prs.save(output_path)
    print(f"[SUCCESS] Compact 5-Slide SRS Presentation generated: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\NutriCampus-Health-Nutrition"
    out_file = os.path.join(out_dir, "NutriCampus_5Slide_SRS_Deck.pptx")
    create_5slide_deck(out_file)
