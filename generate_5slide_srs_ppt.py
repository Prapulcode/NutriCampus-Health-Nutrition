#!/usr/bin/env python3
"""
NutriCampus - Dark Tech / Cyber Minimalist 5-Slide SRS Presentation Generator
Aesthetic: Linear / Vercel / Apple Dark Mode (Deep Charcoal #0B0F19, Glass Cards #131C2E, Neon Emerald #10B981 & Cyber Cyan #06B6D4)
Course: 25CPD37 - Community Project using Innovation & Design Thinking
Department of Computer Science & Engineering, New Horizon College of Engineering (NHCE)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_dark_tech_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Dark Tech / Cyber Minimalist Color Palette
    BG_DARK = RGBColor(11, 15, 25)          # Deep Charcoal Midnight (#0B0F19)
    CARD_BG = RGBColor(19, 28, 46)          # Dark Slate Glass (#131C2E)
    CARD_BG_ALT = RGBColor(15, 23, 42)      # Slate 900 (#0F172A)
    CARD_BORDER = RGBColor(30, 41, 59)      # Slate 800 (#1E293B)
    
    NEON_EMERALD = RGBColor(16, 185, 129)   # Neon Mint (#10B981)
    NEON_CYAN = RGBColor(6, 182, 212)       # Cyber Cyan (#06B6D4)
    NEON_VIOLET = RGBColor(139, 92, 246)    # Electric Violet (#8B5CF6)
    AMBER_ACCENT = RGBColor(245, 158, 11)   # Warning Amber (#F59E0B)
    
    TEXT_WHITE = RGBColor(255, 255, 255)    # High-contrast White
    TEXT_LIGHT = RGBColor(226, 232, 240)    # Slate 200 (#E2E8F0)
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400 (#94A3B8)
    TEXT_DIM = RGBColor(100, 116, 139)      # Slate 500 (#64748B)

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category="SRS DECK • COURSE 25CPD37 (NHCE CSE)", accent_color=NEON_EMERALD):
        # Subtle header container
        hdr_panel = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
        hdr_panel.fill.solid()
        hdr_panel.fill.fore_color.rgb = CARD_BG_ALT
        hdr_panel.line.fill.background()

        # Neon accent bar under header
        accent_strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.13), Inches(13.333), Inches(0.02))
        accent_strip.fill.solid()
        accent_strip.fill.fore_color.rgb = accent_color
        accent_strip.line.fill.background()

        # Category pill
        tx_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.26))
        tf_cat = tx_cat.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = f"// {category.upper()}"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = accent_color

        # Main Title
        tx_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(11.5), Inches(0.65))
        tf_t = tx_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

        # Footer
        add_footer(slide)

    def add_footer(slide):
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.015))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = CARD_BORDER
        footer_line.line.fill.background()

        tx_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.733), Inches(0.3))
        tf_f = tx_f.text_frame
        tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        p_f.text = "NutriCampus • Department of Computer Science & Engineering • New Horizon College of Engineering"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = TEXT_DIM

    def setup_card_tf(tf):
        tf.word_wrap = True
        tf.margin_left = Inches(0.22)
        tf.margin_right = Inches(0.22)
        tf.margin_top = Inches(0.22)
        tf.margin_bottom = Inches(0.22)

    def add_para(tf, text, pt_size=11.5, bold=False, color=TEXT_LIGHT, space_after=5, bullet=False):
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
    # SLIDE 1: Title & Problem Overview (Cyber Minimalist Hero)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Sleek Hero Banner
    hero = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.85))
    hero.fill.solid()
    hero.fill.fore_color.rgb = CARD_BG_ALT
    hero.line.fill.background()

    # Glowing bottom strip
    strip1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.83), Inches(13.333), Inches(0.025))
    strip1.fill.solid()
    strip1.fill.fore_color.rgb = NEON_EMERALD
    strip1.line.fill.background()

    tx1 = s1.shapes.add_textbox(Inches(0.8), Inches(0.22), Inches(11.733), Inches(1.5))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    
    p_meta = tf1.paragraphs[0]
    p_meta.text = "// NEW HORIZON COLLEGE OF ENGINEERING • DEPT OF CSE • COURSE 25CPD37"
    p_meta.font.size = Pt(10)
    p_meta.font.bold = True
    p_meta.font.color.rgb = NEON_EMERALD
    p_meta.space_after = Pt(3)

    p_title = tf1.add_paragraph()
    p_title.text = "NutriCampus: Health & Nutrition Web Application"
    p_title.font.size = Pt(25)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    p_title.space_after = Pt(3)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Software Requirements Specification (SRS) Deck • Innovation & Design Thinking Community Project"
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = NEON_CYAN

    # Two Glass Cards on Slide 1
    # Card 1: Problem Overview
    c1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, Inches(2.15), w_half, Inches(4.65))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = NEON_EMERALD
    c1.line.width = Pt(1.5)

    # Top highlight strip on card
    t_strip1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, Inches(2.15), w_half, Inches(0.08))
    t_strip1.fill.solid()
    t_strip1.fill.fore_color.rgb = NEON_EMERALD
    t_strip1.line.fill.background()

    tx_c1 = s1.shapes.add_textbox(left_col, Inches(2.25), w_half, Inches(4.5))
    tf_c1 = tx_c1.text_frame
    setup_card_tf(tf_c1)
    add_para(tf_c1, "🚨 Real-World Problem Overview", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)
    add_para(tf_c1, "1-Sentence Problem Statement:", pt_size=11, bold=True, color=NEON_EMERALD, space_after=3)
    add_para(tf_c1, "\"Undergraduate students face irregular eating routines, lab dehydration, and high reliance on nutrient-poor canteen snacks with zero accessible guidance.\"", pt_size=11, color=TEXT_LIGHT, space_after=12)
    
    add_para(tf_c1, "Core Pain Points Identified:", pt_size=11, bold=True, color=NEON_CYAN, space_after=5)
    add_para(tf_c1, "Irregular meal hours during programming labs", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_c1, "Excessive canteen fried snacks and sugary sodas", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_c1, "Afternoon brain fog and low daily hydration", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_c1, "Clinical nutrition tools are complex and intimidating", pt_size=10.5, bullet=True, space_after=5)

    # Card 2: Core System Goal
    c2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, Inches(2.15), w_half, Inches(4.65))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = NEON_CYAN
    c2.line.width = Pt(1.5)

    t_strip2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, Inches(2.15), w_half, Inches(0.08))
    t_strip2.fill.solid()
    t_strip2.fill.fore_color.rgb = NEON_CYAN
    t_strip2.line.fill.background()

    tx_c2 = s1.shapes.add_textbox(right_col, Inches(2.25), w_half, Inches(4.5))
    tf_c2 = tx_c2.text_frame
    setup_card_tf(tf_c2)
    add_para(tf_c2, "🎯 Core System Goal & Value", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)
    add_para(tf_c2, "System Vision:", pt_size=11, bold=True, color=NEON_CYAN, space_after=3)
    add_para(tf_c2, "\"Deliver a lightweight, zero-barrier responsive web tool translating complex nutrition into realistic food swaps, hydration tracking, and screening.\"", pt_size=11, color=TEXT_LIGHT, space_after=12)

    add_para(tf_c2, "Key Solution Highlights:", pt_size=11, bold=True, color=NEON_EMERALD, space_after=5)
    add_para(tf_c2, "100% Zero-install single page web architecture", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_c2, "Intuitive 50-25-25 balanced visual plate guide", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_c2, "Safe hydration tracking capped at 5.0 Liters", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_c2, "Validated non-diagnostic medical screening boundary", pt_size=10.5, bullet=True, space_after=5)

    add_footer(s1)

    set_speaker_notes(s1,
        "WHAT TO SAY OUT LOUD:\n"
        "\"Good morning respected evaluators and faculty. We present the Software Requirements Specification for NutriCampus, "
        "developed under Course 25CPD37.\n\n"
        "Undergraduate students at NHCE routinely encounter irregular eating schedules, afternoon fatigue, and heavy canteen snack reliance. "
        "Our system provides a zero-barrier, mobile-responsive web tool that translates complex health science into practical food swaps, "
        "safe hydration tracking, and non-diagnostic health screening.\""
    )

    # =========================================================================
    # SLIDE 2: Scope & Target Users
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Slide 2: Scope & Target Users", accent_color=NEON_EMERALD)

    # Left: Scope
    s2_l = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s2_l.fill.solid()
    s2_l.fill.fore_color.rgb = CARD_BG
    s2_l.line.color.rgb = NEON_EMERALD
    s2_l.line.width = Pt(1.5)

    tx_s2_l = s2.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s2_l = tx_s2_l.text_frame
    setup_card_tf(tf_s2_l)
    add_para(tf_s2_l, "📌 Project Scope Boundaries", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s2_l, "In Scope (Version 1.0 Release):", pt_size=11.5, bold=True, color=NEON_EMERALD, space_after=4)
    add_para(tf_s2_l, "50-25-25 visual balanced meal guide", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Practical Indian canteen food swaps", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Anthropometric BMI screening calculator", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Fluid water tracker with 5.0 L safety limit", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "7-question gamified myth-busting quiz", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Usability survey & community evaluation portal", pt_size=10.5, bullet=True, space_after=8)

    add_para(tf_s2_l, "Out of Scope (Explicit Exclusions):", pt_size=11.5, bold=True, color=AMBER_ACCENT, space_after=4)
    add_para(tf_s2_l, "No clinical medical diagnosis or prescriptions", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "No calorie counting or strict diet regimes", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "No external hardware or wearable sensors", pt_size=10.5, bullet=True, space_after=3)

    # Right: Target Users
    s2_r = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s2_r.fill.solid()
    s2_r.fill.fore_color.rgb = CARD_BG
    s2_r.line.color.rgb = NEON_CYAN
    s2_r.line.width = Pt(1.5)

    tx_s2_r = s2.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s2_r = tx_s2_r.text_frame
    setup_card_tf(tf_s2_r)
    add_para(tf_s2_r, "👥 Target Users & Key Roles", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s2_r, "Primary Student Roles:", pt_size=11.5, bold=True, color=NEON_CYAN, space_after=4)
    add_para(tf_s2_r, "Hostel Residents & Commuters: Budget food swaps and meal portioning.", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s2_r, "Engineering Lab Students: Screen fatigue relief (20-20-20 rule) and hydration.", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s2_r, "Evaluation & Governance Roles:", pt_size=11.5, bold=True, color=NEON_EMERALD, space_after=4)
    add_para(tf_s2_r, "Peer Reviewers: 12+ CSE students testing usability and logging reviews.", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s2_r, "Faculty Evaluators: Reviewing Design Thinking steps and requirements compliance.", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s2_r, "Deployment Environment:", pt_size=11.5, bold=True, color=TEXT_WHITE, space_after=4)
    add_para(tf_s2_r, "Universal web browsers: Chrome, Edge, Safari on mobile and desktop.", pt_size=10, bullet=True, space_after=3)

    set_speaker_notes(s2,
        "WHAT TO SAY OUT LOUD:\n"
        "\"In Slide 2, we define who uses our system and draw a clear boundary around v1 capabilities.\n\n"
        "In Scope, we implement six core awareness modules: visual meal ratios, canteen swaps, metric BMI screening, "
        "a hydration tracker strictly limited to 5 liters, interactive quizzes, and community feedback.\n\n"
        "Out of Scope, we strictly exclude clinical medical diagnoses, calorie counting, or hardware sensors. "
        "Our target users are undergraduate students, hostelites, lab programmers, and our peer evaluation cohort.\""
    )

    # =========================================================================
    # SLIDE 3: Functional Requirements & Architecture
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Slide 3: Functional Requirements & Architecture", accent_color=NEON_CYAN)

    # Left: Architecture Flow
    s3_l = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s3_l.fill.solid()
    s3_l.fill.fore_color.rgb = CARD_BG
    s3_l.line.color.rgb = NEON_CYAN
    s3_l.line.width = Pt(1.5)

    tx_s3_l = s3.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s3_l = tx_s3_l.text_frame
    setup_card_tf(tf_s3_l)
    add_para(tf_s3_l, "🏗️ Use-Case & System Architecture", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s3_l, "Full-Stack System Pipeline:", pt_size=11.5, bold=True, color=NEON_CYAN, space_after=6)

    add_para(tf_s3_l, "[01] USER INTERACTION (Student / Peer Reviewer)", pt_size=10.5, bold=True, color=NEON_EMERALD, space_after=1)
    add_para(tf_s3_l, "     Responsive Single-Page Web UI (HTML5 / Modern CSS3)", pt_size=9.5, color=TEXT_MUTED, space_after=5)

    add_para(tf_s3_l, "[02] CLIENT CONTROLLER (Vanilla ES6+ JavaScript)", pt_size=10.5, bold=True, color=NEON_CYAN, space_after=1)
    add_para(tf_s3_l, "     Quetelet BMI Engine • 5L Fluid Clamping • Instant Quiz Engine", pt_size=9.5, color=TEXT_MUTED, space_after=5)

    add_para(tf_s3_l, "[03] STORAGE & DUAL-TIER PERSISTENCE", pt_size=10.5, bold=True, color=NEON_VIOLET, space_after=1)
    add_para(tf_s3_l, "     • Browser localStorage: Zero-latency offline logs & theme", pt_size=9.5, color=TEXT_MUTED, space_after=1)
    add_para(tf_s3_l, "     • Python/Flask REST API: Asynchronous JSON sync", pt_size=9.5, color=TEXT_MUTED, space_after=1)
    add_para(tf_s3_l, "     • SQLite (health_nutrition.db): Centralized feedback store", pt_size=9.5, color=TEXT_MUTED, space_after=8)

    add_para(tf_s3_l, "Core Architectural Advantage:", pt_size=11, bold=True, color=TEXT_WHITE, space_after=2)
    add_para(tf_s3_l, "Works 100% offline in any browser; seamlessly syncs when connected.", pt_size=9.5, color=NEON_EMERALD, space_after=3)

    # Right: Top Core Features
    s3_r = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s3_r.fill.solid()
    s3_r.fill.fore_color.rgb = CARD_BG
    s3_r.line.color.rgb = NEON_EMERALD
    s3_r.line.width = Pt(1.5)

    tx_s3_r = s3.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s3_r = tx_s3_r.text_frame
    setup_card_tf(tf_s3_r)
    add_para(tf_s3_r, "⚡ Top 5 Core Functional Requirements", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s3_r, "1. FR-1: 50-25-25 Balanced Plate Visualizer", pt_size=11, bold=True, color=NEON_EMERALD, space_after=1)
    add_para(tf_s3_r, "Portions: 50% fiber/veggies, 25% complex carbs, 25% lean protein.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "2. FR-2: Campus Canteen & Food Swaps", pt_size=11, bold=True, color=NEON_CYAN, space_after=1)
    add_para(tf_s3_r, "Evidence-based swaps for instant noodles, sugary sodas, and fried snacks.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "3. FR-3: Anthropometric BMI Screening", pt_size=11, bold=True, color=NEON_EMERALD, space_after=1)
    add_para(tf_s3_r, "Metric/Imperial calculation with color gauge & mandatory medical disclaimer.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "4. FR-4: Hydration Tracker with 5.0 L Limit", pt_size=11, bold=True, color=NEON_CYAN, space_after=1)
    add_para(tf_s3_r, "Animated fluid bottle with strict 5000 mL daily safety cap to prevent hyponatremia.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "5. FR-5: Quiz & Community Feedback Portal", pt_size=11, bold=True, color=NEON_EMERALD, space_after=1)
    add_para(tf_s3_r, "Gamified myth-busting badges and rating-free peer usability evaluation.", pt_size=9.5, space_after=3)

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
    set_slide_background(s4)
    add_header(s4, "Slide 4: Non-Functional Requirements & Constraints", accent_color=NEON_VIOLET)

    # Left: Performance & Security
    s4_l = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s4_l.fill.solid()
    s4_l.fill.fore_color.rgb = CARD_BG
    s4_l.line.color.rgb = NEON_CYAN
    s4_l.line.width = Pt(1.5)

    tx_s4_l = s4.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s4_l = tx_s4_l.text_frame
    setup_card_tf(tf_s4_l)
    add_para(tf_s4_l, "🛡️ Quality Standards & Security", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s4_l, "Performance Standards:", pt_size=11.5, bold=True, color=NEON_CYAN, space_after=4)
    add_para(tf_s4_l, "Page load under 1.5 seconds on 4G networks", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Lightweight bundle under 150 KB total assets", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Instant client calculations under 16 milliseconds", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Zero external CSS/JS framework dependencies", pt_size=10.5, bullet=True, space_after=8)

    add_para(tf_s4_l, "Security & Privacy Standards:", pt_size=11.5, bold=True, color=NEON_EMERALD, space_after=4)
    add_para(tf_s4_l, "Zero mandatory personal information collection", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "No passwords or user accounts required", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Parameterized SQL statements prevent injection", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Strict HTML sanitization blocks XSS attacks", pt_size=10.5, bullet=True, space_after=3)

    # Right: Constraints & Ethics
    s4_r = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s4_r.fill.solid()
    s4_r.fill.fore_color.rgb = CARD_BG
    s4_r.line.color.rgb = AMBER_ACCENT
    s4_r.line.width = Pt(1.5)

    tx_s4_r = s4.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s4_r = tx_s4_r.text_frame
    setup_card_tf(tf_s4_r)
    add_para(tf_s4_r, "⚙️ Constraints & Ethical Boundary", pt_size=15, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s4_r, "Technical & Platform Constraints:", pt_size=11.5, bold=True, color=NEON_CYAN, space_after=4)
    add_para(tf_s4_r, "Cross-browser execution (Chrome, Safari, Edge, Firefox)", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Responsive viewports: 360px mobile to 4K desktop", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Dual deployment: zero-dependency local server & Vercel edge", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s4_r, "Mandatory Medical Ethics Boundary:", pt_size=11.5, bold=True, color=AMBER_ACCENT, space_after=4)
    add_para(tf_s4_r, "Strictly educational health awareness platform", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "BMI defined as screening ratio, not diagnostic tool", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Prominent amber disclaimers visible on all screening views", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Water tracker enforces 5.0 L daily safety limit", pt_size=10, bullet=True, space_after=3)

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
    # SLIDE 5: Summary & Key Takeaways
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Slide 5: Summary & Key Takeaways", category="PROJECT CONCLUSION • COURSE 25CPD37", accent_color=NEON_EMERALD)

    card_w3 = Inches(3.64)
    c1_x = Inches(0.8)
    c2_x = Inches(4.84)
    c3_x = Inches(8.88)
    h_top = Inches(1.4)
    card_h3 = Inches(3.75)

    # Pod 1: Design Thinking
    p1_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x, h_top, card_w3, card_h3)
    p1_box.fill.solid()
    p1_box.fill.fore_color.rgb = CARD_BG
    p1_box.line.color.rgb = NEON_EMERALD
    p1_box.line.width = Pt(1.5)

    tx_p1 = s5.shapes.add_textbox(c1_x, h_top, card_w3, card_h3)
    tf_p1 = tx_p1.text_frame
    setup_card_tf(tf_p1)
    add_para(tf_p1, "💡 1. Human-Centered", pt_size=13.5, bold=True, color=TEXT_WHITE, space_after=6)
    add_para(tf_p1, "Design Thinking:", pt_size=11, bold=True, color=NEON_EMERALD, space_after=3)
    add_para(tf_p1, "Directly fulfills Course 25CPD37 5-stage framework (Empathize, Define, Ideate, Prototype, Test).", pt_size=10, space_after=6)
    add_para(tf_p1, "Undergraduate Reality:", pt_size=11, bold=True, color=NEON_CYAN, space_after=3)
    add_para(tf_p1, "Built specifically for hostel schedules, coding lab eye strain, and campus meals.", pt_size=10, space_after=2)

    # Pod 2: Zero-Barrier
    p2_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x, h_top, card_w3, card_h3)
    p2_box.fill.solid()
    p2_box.fill.fore_color.rgb = CARD_BG
    p2_box.line.color.rgb = NEON_CYAN
    p2_box.line.width = Pt(1.5)

    tx_p2 = s5.shapes.add_textbox(c2_x, h_top, card_w3, card_h3)
    tf_p2 = tx_p2.text_frame
    setup_card_tf(tf_p2)
    add_para(tf_p2, "🚀 2. Zero-Barrier Access", pt_size=13.5, bold=True, color=TEXT_WHITE, space_after=6)
    add_para(tf_p2, "Accessible Anywhere:", pt_size=11, bold=True, color=NEON_CYAN, space_after=3)
    add_para(tf_p2, "No app stores, no signups, no installations. Immediate access via any mobile or PC browser.", pt_size=10, space_after=6)
    add_para(tf_p2, "Dual Deployment:", pt_size=11, bold=True, color=NEON_EMERALD, space_after=3)
    add_para(tf_p2, "Zero-dependency local Python server + production cloud deployment on Vercel.", pt_size=10, space_after=2)

    # Pod 3: Validated Impact
    p3_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x, h_top, card_w3, card_h3)
    p3_box.fill.solid()
    p3_box.fill.fore_color.rgb = CARD_BG
    p3_box.line.color.rgb = NEON_VIOLET
    p3_box.line.width = Pt(1.5)

    tx_p3 = s5.shapes.add_textbox(c3_x, h_top, card_w3, card_h3)
    tf_p3 = tx_p3.text_frame
    setup_card_tf(tf_p3)
    add_para(tf_p3, "📈 3. Validated Impact", pt_size=13.5, bold=True, color=TEXT_WHITE, space_after=6)
    add_para(tf_p3, "Peer Review Testing:", pt_size=11, bold=True, color=NEON_VIOLET, space_after=3)
    add_para(tf_p3, "12+ CSE 3rd Sem volunteer student testers completed Phase 6 usability study.", pt_size=10, space_after=6)
    add_para(tf_p3, "Empirical Outcomes:", pt_size=11, bold=True, color=NEON_CYAN, space_after=3)
    add_para(tf_p3, "100% reported positive awareness adoption; 0 crashes or unhandled client exceptions.", pt_size=10, space_after=2)

    # Terminal Callout Banner
    term_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.45))
    term_box.fill.solid()
    term_box.fill.fore_color.rgb = CARD_BG_ALT
    term_box.line.color.rgb = NEON_EMERALD
    term_box.line.width = Pt(1.5)

    tx_term = s5.shapes.add_textbox(Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.45))
    tf_term = tx_term.text_frame
    setup_card_tf(tf_term)

    p_term_q = tf_term.paragraphs[0]
    p_term_q.text = "❓ THANK YOU! ANY QUESTIONS OR EVALUATOR FEEDBACK?"
    p_term_q.font.size = Pt(15)
    p_term_q.font.bold = True
    p_term_q.font.color.rgb = NEON_EMERALD
    p_term_q.alignment = PP_ALIGN.CENTER
    p_term_q.space_after = Pt(4)

    p_term_lnk = tf_term.add_paragraph()
    p_term_lnk.text = "Live Demo: https://nutri-campus-health-nutrition.vercel.app  •  GitHub: github.com/Prapulcode/NutriCampus-Health-Nutrition"
    p_term_lnk.font.size = Pt(10.5)
    p_term_lnk.font.color.rgb = TEXT_WHITE
    p_term_lnk.alignment = PP_ALIGN.CENTER

    set_speaker_notes(s5,
        "WHAT TO SAY OUT LOUD:\n"
        "\"To wrap up our presentation in 20 seconds:\n"
        "1. NutriCampus demonstrates human-centered Design Thinking for undergraduate student wellness.\n"
        "2. It provides zero-barrier accessibility, functioning offline and in the cloud with zero downloads.\n"
        "3. It has been empirically validated through our pilot study with 12 peer evaluators.\n\n"
        "Thank you respected faculty and evaluators. We now open the floor for your questions!\""
    )

    prs.save(output_path)
    print(f"[SUCCESS] Dark Tech / Cyber Minimalist 5-Slide Presentation generated: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\NutriCampus-Health-Nutrition"
    out_file = os.path.join(out_dir, "NutriCampus_5Slide_SRS_Deck.pptx")
    create_dark_tech_deck(out_file)
