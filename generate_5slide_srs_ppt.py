#!/usr/bin/env python3
"""
NutriCampus - Executive Dark Professional 5-Slide SRS Presentation Generator
Style: Dark Executive / Corporate Technology (Deep Slate #0F172A, Refined Cards #1E293B, Precision Borders #334155, Cobalt & Emerald Accents)
Course: 25CPD37 - Community Project using Innovation & Design Thinking
Department of Computer Science & Engineering, New Horizon College of Engineering (NHCE)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_executive_dark_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Executive Dark Palette (Sophisticated, Enterprise Tech Standard)
    BG_DARK = RGBColor(15, 23, 42)          # Deep Midnight Slate (#0F172A)
    HEADER_BG = RGBColor(11, 15, 25)        # Slate 950 (#0B0F19)
    CARD_BG = RGBColor(30, 41, 59)          # Refined Slate (#1E293B)
    CARD_BG_SUBTLE = RGBColor(24, 33, 49)   # Slate 850
    CARD_BORDER = RGBColor(51, 65, 85)      # Slate 700 (#334155)
    CARD_BORDER_ACTIVE = RGBColor(59, 130, 246) # Cobalt Blue (#3B82F6)
    
    PRIMARY_BLUE = RGBColor(59, 130, 246)   # Cobalt Blue (#3B82F6)
    ACCENT_MINT = RGBColor(16, 185, 129)    # Emerald (#10B981)
    ACCENT_AMBER = RGBColor(245, 158, 11)   # Executive Amber / Gold (#F59E0B)
    
    TEXT_WHITE = RGBColor(255, 255, 255)    # High-contrast Pure White
    TEXT_LIGHT = RGBColor(241, 245, 249)    # Slate 100 (#F1F5F9)
    TEXT_BODY = RGBColor(203, 213, 225)     # Slate 300 (#CBD5E1)
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400 (#94A3B8)
    TEXT_DIM = RGBColor(100, 116, 139)      # Slate 500 (#64748B)

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category="SOFTWARE REQUIREMENTS SPECIFICATION • COURSE 25CPD37", slide_num=1):
        # Header container
        hdr_panel = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.18))
        hdr_panel.fill.solid()
        hdr_panel.fill.fore_color.rgb = HEADER_BG
        hdr_panel.line.fill.background()

        # Hairline divider
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.17), Inches(13.333), Inches(0.015))
        div.fill.solid()
        div.fill.fore_color.rgb = CARD_BORDER
        div.line.fill.background()

        # Category metadata
        tx_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.14), Inches(10.5), Inches(0.24))
        tf_cat = tx_cat.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = PRIMARY_BLUE

        # Main Title
        tx_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.40), Inches(10.5), Inches(0.65))
        tf_t = tx_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

        # Slide Number in header corner
        tx_num = slide.shapes.add_textbox(Inches(11.5), Inches(0.40), Inches(1.0), Inches(0.4))
        tf_num = tx_num.text_frame
        tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
        p_num = tf_num.paragraphs[0]
        p_num.text = f"0{slide_num} / 05"
        p_num.font.size = Pt(13)
        p_num.font.bold = True
        p_num.font.color.rgb = TEXT_MUTED
        p_num.alignment = PP_ALIGN.RIGHT

        # Footer
        add_footer(slide)

    def add_footer(slide):
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.015))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = CARD_BORDER
        footer_line.line.fill.background()

        tx_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.12), Inches(11.733), Inches(0.3))
        tf_f = tx_f.text_frame
        tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        p_f.text = "New Horizon College of Engineering  |  Department of Computer Science & Engineering  |  NutriCampus Platform"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = TEXT_DIM

    def setup_card_tf(tf):
        tf.word_wrap = True
        tf.margin_left = Inches(0.24)
        tf.margin_right = Inches(0.24)
        tf.margin_top = Inches(0.24)
        tf.margin_bottom = Inches(0.24)

    def add_para(tf, text, pt_size=11, bold=False, color=TEXT_BODY, space_after=5, bullet=False):
        if len(tf.paragraphs) == 1 and tf.paragraphs[0].text == "":
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = ("•  " + text) if bullet else text
        p.font.size = Pt(pt_size)
        p.font.bold = bold
        p.font.color.rgb = color
        p.space_after = Pt(space_after)
        return p

    def set_speaker_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = notes_text

    card_top = Inches(1.42)
    card_h = Inches(5.32)
    w_half = Inches(5.66)
    left_col = Inches(0.8)
    right_col = Inches(6.86)

    # =========================================================================
    # SLIDE 1: Title & Problem Overview (Executive Dark)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Top Brand Header Panel
    hero = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.85))
    hero.fill.solid()
    hero.fill.fore_color.rgb = HEADER_BG
    hero.line.fill.background()

    div1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.84), Inches(13.333), Inches(0.015))
    div1.fill.solid()
    div1.fill.fore_color.rgb = CARD_BORDER
    div1.line.fill.background()

    tx1 = s1.shapes.add_textbox(Inches(0.8), Inches(0.22), Inches(11.733), Inches(1.5))
    tf1 = tx1.text_frame
    tf1.word_wrap = True
    
    p_meta = tf1.paragraphs[0]
    p_meta.text = "NEW HORIZON COLLEGE OF ENGINEERING  •  DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING"
    p_meta.font.size = Pt(9.5)
    p_meta.font.bold = True
    p_meta.font.color.rgb = PRIMARY_BLUE
    p_meta.space_after = Pt(4)

    p_title = tf1.add_paragraph()
    p_title.text = "NutriCampus: Health & Nutrition Awareness Platform"
    p_title.font.size = Pt(25)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    p_title.space_after = Pt(3)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Software Requirements Specification (SRS) Presentation  •  Course 25CPD37: Community Project"
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = TEXT_MUTED

    # Slide 1 Two Cards
    # Card 1: Problem Definition
    c1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, Inches(2.15), w_half, Inches(4.65))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = CARD_BORDER
    c1.line.width = Pt(1.5)

    tx_c1 = s1.shapes.add_textbox(left_col, Inches(2.15), w_half, Inches(4.65))
    tf_c1 = tx_c1.text_frame
    setup_card_tf(tf_c1)
    add_para(tf_c1, "Problem Definition & Context", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)
    add_para(tf_c1, "CORE PROBLEM STATEMENT", pt_size=10, bold=True, color=PRIMARY_BLUE, space_after=4)
    add_para(tf_c1, "\"Undergraduate students face irregular eating routines, screen fatigue, and heavy reliance on nutrient-poor campus canteen meals without accessible dietary guidance.\"", pt_size=11, color=TEXT_LIGHT, space_after=12)
    
    add_para(tf_c1, "CRITICAL UNDERGRADUATE PAIN POINTS", pt_size=10, bold=True, color=TEXT_MUTED, space_after=5)
    add_para(tf_c1, "Irregular meal timing caused by long lab and lecture cycles", pt_size=10.5, bullet=True, space_after=3.5)
    add_para(tf_c1, "Frequent consumption of high-sodium, ultra-processed canteen snacks", pt_size=10.5, bullet=True, space_after=3.5)
    add_para(tf_c1, "Chronic daytime dehydration leading to cognitive fatigue", pt_size=10.5, bullet=True, space_after=3.5)
    add_para(tf_c1, "Existing clinical health applications are overly complex and intimidating", pt_size=10.5, bullet=True, space_after=4)

    # Card 2: System Objectives
    c2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, Inches(2.15), w_half, Inches(4.65))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = CARD_BORDER_ACTIVE
    c2.line.width = Pt(1.5)

    tx_c2 = s1.shapes.add_textbox(right_col, Inches(2.15), w_half, Inches(4.65))
    tf_c2 = tx_c2.text_frame
    setup_card_tf(tf_c2)
    add_para(tf_c2, "System Vision & Core Objectives", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)
    add_para(tf_c2, "PRIMARY ENGINEERING OBJECTIVE", pt_size=10, bold=True, color=ACCENT_MINT, space_after=4)
    add_para(tf_c2, "\"Develop a lightweight, zero-barrier web application translating evidence-based nutritional science into actionable food swaps, hydration tracking, and non-diagnostic self-screening.\"", pt_size=11, color=TEXT_LIGHT, space_after=12)

    add_para(tf_c2, "STRATEGIC SYSTEM DELIVERABLES", pt_size=10, bold=True, color=TEXT_MUTED, space_after=5)
    add_para(tf_c2, "100% browser-based single-page application requiring zero installation", pt_size=10.5, bullet=True, space_after=3.5)
    add_para(tf_c2, "Scientifically validated 50-25-25 balanced dietary plate model", pt_size=10.5, bullet=True, space_after=3.5)
    add_para(tf_c2, "Fluid intake tracker strictly bounded by a 5.0 Liter safety ceiling", pt_size=10.5, bullet=True, space_after=3.5)
    add_para(tf_c2, "Ethical, non-diagnostic anthropometric BMI screening framework", pt_size=10.5, bullet=True, space_after=4)

    add_footer(s1)

    set_speaker_notes(s1,
        "WHAT TO SAY OUT LOUD:\n"
        "\"Good morning respected evaluators and faculty members. We present the Software Requirements Specification for NutriCampus, "
        "our community engineering project under Course 25CPD37.\n\n"
        "Undergraduate students routinely experience irregular meal routines, long lab hours, and heavy canteen reliance. "
        "NutriCampus addresses this reality through a zero-barrier, mobile-responsive web platform that delivers actionable food alternatives, "
        "safe hydration tracking, and non-diagnostic health self-screening.\""
    )

    # =========================================================================
    # SLIDE 2: Scope & Target Users (Executive Dark)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Scope Boundaries & Target User Profiles", category="PROJECT SCOPE MATRIX • COURSE 25CPD37", slide_num=2)

    # Left: Scope
    s2_l = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s2_l.fill.solid()
    s2_l.fill.fore_color.rgb = CARD_BG
    s2_l.line.color.rgb = CARD_BORDER
    s2_l.line.width = Pt(1.5)

    tx_s2_l = s2.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s2_l = tx_s2_l.text_frame
    setup_card_tf(tf_s2_l)
    add_para(tf_s2_l, "System Scope Specification", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s2_l, "IN-SCOPE DELIVERABLES (VERSION 1.0 RELEASE)", pt_size=10, bold=True, color=ACCENT_MINT, space_after=4)
    add_para(tf_s2_l, "50-25-25 visual balanced meal guidance system", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Campus canteen and hostel food alternative database", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Metric/Imperial anthropometric BMI screening module", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Daily hydration tracker with 5.0 Liter safety ceiling", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Interactive 7-item nutrition myth-busting quiz", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "Phase 6 community usability feedback portal", pt_size=10.5, bullet=True, space_after=8)

    add_para(tf_s2_l, "OUT-OF-SCOPE EXCLUSIONS (SYSTEM BOUNDARIES)", pt_size=10, bold=True, color=ACCENT_AMBER, space_after=4)
    add_para(tf_s2_l, "No clinical medical diagnosis or therapeutic prescription regimens", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "No calorie counting or restrictive dietary prescription models", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s2_l, "No hardware sensors or wearable biometric synchronization", pt_size=10.5, bullet=True, space_after=3)

    # Right: Target Users
    s2_r = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s2_r.fill.solid()
    s2_r.fill.fore_color.rgb = CARD_BG
    s2_r.line.color.rgb = CARD_BORDER
    s2_r.line.width = Pt(1.5)

    tx_s2_r = s2.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s2_r = tx_s2_r.text_frame
    setup_card_tf(tf_s2_r)
    add_para(tf_s2_r, "Stakeholder & Target User Profiles", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s2_r, "PRIMARY STUDENT BENEFICIARIES", pt_size=10, bold=True, color=PRIMARY_BLUE, space_after=4)
    add_para(tf_s2_r, "Hostel Residents & Commuters: Seeking realistic canteen food substitutions.", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s2_r, "Programming Lab Students: Managing digital eye strain (20-20-20 rule) and hydration.", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s2_r, "EVALUATION & ACADEMIC STAKEHOLDERS", pt_size=10, bold=True, color=ACCENT_MINT, space_after=4)
    add_para(tf_s2_r, "Peer Review Cohort: 12+ CSE students testing usability and habit retention.", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s2_r, "Faculty Evaluators: Reviewing Design Thinking adherence and syllabus compliance.", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s2_r, "DEPLOYMENT ENVIRONMENT", pt_size=10, bold=True, color=TEXT_MUTED, space_after=4)
    add_para(tf_s2_r, "Universal web browsers: Chrome, Edge, Safari across mobile and desktop devices.", pt_size=10, bullet=True, space_after=3)

    set_speaker_notes(s2,
        "WHAT TO SAY OUT LOUD:\n"
        "\"In Slide 2, we establish our system boundaries and user profiles.\n\n"
        "In Scope for v1, we provide six core modules: visual meal portioning, practical canteen swaps, metric BMI screening, "
        "a safe hydration tracker capped at 5 liters, educational quizzes, and community feedback.\n\n"
        "Out of Scope, we draw a clear line excluding clinical medical diagnosis, restrictive calorie counting, or hardware sensors. "
        "Our primary stakeholders are undergraduate students, hostel residents, lab programmers, and our peer evaluation cohort.\""
    )

    # =========================================================================
    # SLIDE 3: Functional Requirements & Architecture (Executive Dark)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "System Architecture & Functional Requirements", category="SYSTEM ARCHITECTURE & SPECIFICATIONS • COURSE 25CPD37", slide_num=3)

    # Left: Architecture
    s3_l = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s3_l.fill.solid()
    s3_l.fill.fore_color.rgb = CARD_BG
    s3_l.line.color.rgb = CARD_BORDER
    s3_l.line.width = Pt(1.5)

    tx_s3_l = s3.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s3_l = tx_s3_l.text_frame
    setup_card_tf(tf_s3_l)
    add_para(tf_s3_l, "Architectural Framework & Data Flow", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s3_l, "THREE-TIER SYSTEM DEPLOYMENT", pt_size=10, bold=True, color=PRIMARY_BLUE, space_after=6)

    add_para(tf_s3_l, "Tier 1: Client Presentation Layer", pt_size=10.5, bold=True, color=TEXT_WHITE, space_after=1)
    add_para(tf_s3_l, "Responsive Single-Page Web Application built with HTML5, CSS3, and ES6+.", pt_size=9.5, color=TEXT_MUTED, space_after=5)

    add_para(tf_s3_l, "Tier 2: Business Logic & Controllers", pt_size=10.5, bold=True, color=TEXT_WHITE, space_after=1)
    add_para(tf_s3_l, "Client-side Quetelet BMI computation, 5L fluid clamping, and instant quiz feedback.", pt_size=9.5, color=TEXT_MUTED, space_after=5)

    add_para(tf_s3_l, "Tier 3: Dual-Mode Persistence", pt_size=10.5, bold=True, color=TEXT_WHITE, space_after=1)
    add_para(tf_s3_l, "• Browser localStorage for zero-latency offline hydration logs and theme state.\n• Python/Flask REST API and SQLite (health_nutrition.db) for survey aggregation.", pt_size=9.5, color=TEXT_MUTED, space_after=8)

    add_para(tf_s3_l, "OPERATIONAL ADVANTAGE", pt_size=10, bold=True, color=ACCENT_MINT, space_after=2)
    add_para(tf_s3_l, "Operates completely standalone without active internet; synchronizes when connected.", pt_size=9.5, color=TEXT_LIGHT, space_after=3)

    # Right: Core FRs
    s3_r = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s3_r.fill.solid()
    s3_r.fill.fore_color.rgb = CARD_BG
    s3_r.line.color.rgb = CARD_BORDER_ACTIVE
    s3_r.line.width = Pt(1.5)

    tx_s3_r = s3.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s3_r = tx_s3_r.text_frame
    setup_card_tf(tf_s3_r)
    add_para(tf_s3_r, "Core Functional Specifications", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s3_r, "FR-1: 50-25-25 Balanced Plate Guide", pt_size=11, bold=True, color=PRIMARY_BLUE, space_after=1)
    add_para(tf_s3_r, "Interactive meal ratio guide: 50% fiber/vegetables, 25% complex carbs, 25% protein.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "FR-2: Campus Canteen Food Swaps", pt_size=11, bold=True, color=PRIMARY_BLUE, space_after=1)
    add_para(tf_s3_r, "Nutritional alternatives replacing instant noodles, packaged sodas, and fried snacks.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "FR-3: Anthropometric BMI Calculator", pt_size=11, bold=True, color=PRIMARY_BLUE, space_after=1)
    add_para(tf_s3_r, "Metric/Imperial Quetelet ratio screening tool with visual gauge and medical disclaimer.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "FR-4: Daily Hydration Tracker (5.0 L Limit)", pt_size=11, bold=True, color=PRIMARY_BLUE, space_after=1)
    add_para(tf_s3_r, "Fluid intake simulation with strict 5000 mL daily safety ceiling preventing hyponatremia.", pt_size=9.5, space_after=5)

    add_para(tf_s3_r, "FR-5: Myth-Busting Quiz & Usability Portal", pt_size=11, bold=True, color=PRIMARY_BLUE, space_after=1)
    add_para(tf_s3_r, "Gamified educational quiz with instant scientific rationales and rating-free peer feedback.", pt_size=9.5, space_after=3)

    set_speaker_notes(s3,
        "WHAT TO SAY OUT LOUD:\n"
        "\"Slide 3 outlines our system architecture and primary functional requirements.\n\n"
        "On the left, our three-tier architecture illustrates how user interactions execute within a clean frontend, "
        "persisting data to browser localStorage for offline reliability, with an optional Python SQLite backend for survey aggregation.\n\n"
        "On the right are our top 5 functional requirements: the 50-25-25 plate model, canteen swaps, metric BMI screening, "
        "a safe hydration tracker capped at 5 liters, and our gamified quiz and community survey.\""
    )

    # =========================================================================
    # SLIDE 4: Non-Functional Requirements & Constraints (Executive Dark)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Non-Functional Requirements & Constraints", category="SYSTEM QUALITY STANDARDS • COURSE 25CPD37", slide_num=4)

    # Left: Performance & Security
    s4_l = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s4_l.fill.solid()
    s4_l.fill.fore_color.rgb = CARD_BG
    s4_l.line.color.rgb = CARD_BORDER
    s4_l.line.width = Pt(1.5)

    tx_s4_l = s4.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s4_l = tx_s4_l.text_frame
    setup_card_tf(tf_s4_l)
    add_para(tf_s4_l, "Quality Standards & System Security", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s4_l, "PERFORMANCE BENCHMARKS", pt_size=10, bold=True, color=PRIMARY_BLUE, space_after=4)
    add_para(tf_s4_l, "Page load latency under 1.5 seconds on standard mobile connections", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Lightweight bundle size under 150 KB total uncompressed footprint", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Real-time client computational latency under 16 milliseconds", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Zero external CSS/JS framework dependencies", pt_size=10.5, bullet=True, space_after=8)

    add_para(tf_s4_l, "SECURITY & PRIVACY PROTOCOLS", pt_size=10, bold=True, color=ACCENT_MINT, space_after=4)
    add_para(tf_s4_l, "Zero mandatory personal information collection (privacy by design)", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "No authentication requirements or user account storage", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Parameterized SQL queries eliminating SQL injection risks", pt_size=10.5, bullet=True, space_after=3)
    add_para(tf_s4_l, "Strict DOM text sanitization preventing Cross-Site Scripting (XSS)", pt_size=10.5, bullet=True, space_after=3)

    # Right: Constraints & Ethics
    s4_r = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s4_r.fill.solid()
    s4_r.fill.fore_color.rgb = CARD_BG
    s4_r.line.color.rgb = CARD_BORDER
    s4_r.line.width = Pt(1.5)

    tx_s4_r = s4.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s4_r = tx_s4_r.text_frame
    setup_card_tf(tf_s4_r)
    add_para(tf_s4_r, "System Constraints & Medical Ethics", pt_size=14, bold=True, color=TEXT_WHITE, space_after=10)

    add_para(tf_s4_r, "TECHNICAL & PLATFORM CONSTRAINTS", pt_size=10, bold=True, color=PRIMARY_BLUE, space_after=4)
    add_para(tf_s4_r, "Cross-browser compatibility (Chrome, Safari, Edge, Firefox)", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Responsive layout scaling across 360px mobile to 4K desktop monitors", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Dual execution: zero-dependency local Python server and cloud Vercel edge", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s4_r, "MANDATORY MEDICAL ETHICS BOUNDARY", pt_size=10, bold=True, color=ACCENT_AMBER, space_after=4)
    add_para(tf_s4_r, "Strictly defined as an educational awareness and screening platform", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "BMI defined strictly as an anthropometric ratio, not clinical diagnosis", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Prominent non-diagnostic medical disclaimers displayed on screening views", pt_size=10, bullet=True, space_after=3)
    add_para(tf_s4_r, "Hydration tracking programmatically capped at 5.0 Liters for physical safety", pt_size=10, bullet=True, space_after=3)

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
    # SLIDE 5: Summary & Key Takeaways (Executive Dark)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Executive Summary & Project Deliverables", category="PROJECT CONCLUSION • COURSE 25CPD37", slide_num=5)

    card_w3 = Inches(3.64)
    c1_x = Inches(0.8)
    c2_x = Inches(4.84)
    c3_x = Inches(8.88)
    h_top = Inches(1.42)
    card_h3 = Inches(3.72)

    # Pod 1: Design Thinking
    p1_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x, h_top, card_w3, card_h3)
    p1_box.fill.solid()
    p1_box.fill.fore_color.rgb = CARD_BG
    p1_box.line.color.rgb = CARD_BORDER
    p1_box.line.width = Pt(1.5)

    tx_p1 = s5.shapes.add_textbox(c1_x, h_top, card_w3, card_h3)
    tf_p1 = tx_p1.text_frame
    setup_card_tf(tf_p1)
    add_para(tf_p1, "1. Human-Centered Design", pt_size=13, bold=True, color=TEXT_WHITE, space_after=6)
    add_para(tf_p1, "DESIGN THINKING RIGOR", pt_size=9.5, bold=True, color=PRIMARY_BLUE, space_after=3)
    add_para(tf_p1, "Directly fulfills the 5-stage framework of Course 25CPD37 (Empathize, Define, Ideate, Prototype, Test).", pt_size=10, space_after=6)
    add_para(tf_p1, "CAMPUS RELEVANCE", pt_size=9.5, bold=True, color=TEXT_MUTED, space_after=3)
    add_para(tf_p1, "Tailored for college realities: hostel mess menus, programming lab eye strain, and irregular study hours.", pt_size=10, space_after=2)

    # Pod 2: Zero-Barrier
    p2_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x, h_top, card_w3, card_h3)
    p2_box.fill.solid()
    p2_box.fill.fore_color.rgb = CARD_BG
    p2_box.line.color.rgb = CARD_BORDER_ACTIVE
    p2_box.line.width = Pt(1.5)

    tx_p2 = s5.shapes.add_textbox(c2_x, h_top, card_w3, card_h3)
    tf_p2 = tx_p2.text_frame
    setup_card_tf(tf_p2)
    add_para(tf_p2, "2. Zero-Barrier Accessibility", pt_size=13, bold=True, color=TEXT_WHITE, space_after=6)
    add_para(tf_p2, "FRICTIONLESS ACCESS", pt_size=9.5, bold=True, color=ACCENT_MINT, space_after=3)
    add_para(tf_p2, "Zero app store downloads, accounts, or setup required. Instant execution in any modern web browser.", pt_size=10, space_after=6)
    add_para(tf_p2, "DUAL-TIER DEPLOYMENT", pt_size=9.5, bold=True, color=TEXT_MUTED, space_after=3)
    add_para(tf_p2, "Zero-dependency local Python/SQLite server for offline vivas + production Vercel cloud deployment.", pt_size=10, space_after=2)

    # Pod 3: Validated Impact
    p3_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x, h_top, card_w3, card_h3)
    p3_box.fill.solid()
    p3_box.fill.fore_color.rgb = CARD_BG
    p3_box.line.color.rgb = CARD_BORDER
    p3_box.line.width = Pt(1.5)

    tx_p3 = s5.shapes.add_textbox(c3_x, h_top, card_w3, card_h3)
    tf_p3 = tx_p3.text_frame
    setup_card_tf(tf_p3)
    add_para(tf_p3, "3. Validated Community Impact", pt_size=13, bold=True, color=TEXT_WHITE, space_after=6)
    add_para(tf_p3, "PEER USABILITY EVALUATION", pt_size=9.5, bold=True, color=PRIMARY_BLUE, space_after=3)
    add_para(tf_p3, "12+ CSE Semester III volunteer student testers completed structured Phase 6 usability testing.", pt_size=10, space_after=6)
    add_para(tf_p3, "MEASURABLE OUTCOMES", pt_size=9.5, bold=True, color=TEXT_MUTED, space_after=3)
    add_para(tf_p3, "100% reported adopting healthier habits with zero unhandled client exceptions or crashes.", pt_size=10, space_after=2)

    # Executive Bottom Callout
    term_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.32), Inches(11.733), Inches(1.48))
    term_box.fill.solid()
    term_box.fill.fore_color.rgb = HEADER_BG
    term_box.line.color.rgb = CARD_BORDER
    term_box.line.width = Pt(1.5)

    tx_term = s5.shapes.add_textbox(Inches(0.8), Inches(5.32), Inches(11.733), Inches(1.48))
    tf_term = tx_term.text_frame
    setup_card_tf(tf_term)

    p_term_q = tf_term.paragraphs[0]
    p_term_q.text = "QUESTIONS & EVALUATION DISCUSSION"
    p_term_q.font.size = Pt(14)
    p_term_q.font.bold = True
    p_term_q.font.color.rgb = PRIMARY_BLUE
    p_term_q.alignment = PP_ALIGN.CENTER
    p_term_q.space_after = Pt(4)

    p_term_lnk = tf_term.add_paragraph()
    p_term_lnk.text = "Live Deployment: https://nutri-campus-health-nutrition.vercel.app  |  Source Code: github.com/Prapulcode/NutriCampus-Health-Nutrition"
    p_term_lnk.font.size = Pt(10)
    p_term_lnk.font.color.rgb = TEXT_BODY
    p_term_lnk.alignment = PP_ALIGN.CENTER

    set_speaker_notes(s5,
        "WHAT TO SAY OUT LOUD:\n"
        "\"To wrap up our presentation in 20 seconds:\n"
        "1. NutriCampus demonstrates human-centered Design Thinking tailored specifically for undergraduate student wellness.\n"
        "2. It delivers zero-barrier accessibility, functioning offline and in the cloud with zero downloads.\n"
        "3. It has been empirically validated through our pilot study with 12 peer evaluators.\n\n"
        "Thank you respected faculty and evaluators. We now open the floor for your questions!\""
    )

    try:
        prs.save(output_path)
        print(f"[SUCCESS] Executive Dark Professional 5-Slide Presentation generated: {output_path}")
    except PermissionError:
        fallback_path = output_path.replace(".pptx", "_Updated.pptx")
        prs.save(fallback_path)
        print(f"[NOTICE] '{os.path.basename(output_path)}' is currently open in PowerPoint.")
        print(f"[SUCCESS] Saved updated version to: {fallback_path}")
        print("Please close PowerPoint to replace the main presentation file directly.")

    # Also save an executive standalone copy
    exec_path = os.path.join(os.path.dirname(output_path), "NutriCampus_Executive_Dark_Deck.pptx")
    try:
        prs.save(exec_path)
        print(f"[SUCCESS] Executive Dark Copy generated: {exec_path}")
    except Exception:
        pass

if __name__ == "__main__":
    out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\NutriCampus-Health-Nutrition"
    out_file = os.path.join(out_dir, "NutriCampus_5Slide_SRS_Deck.pptx")
    create_executive_dark_deck(out_file)
