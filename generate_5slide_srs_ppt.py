#!/usr/bin/env python3
"""
NutriCampus - Executive Dark Professional Presentation Deck
Course: 25CPD37 - Community Project using Innovation & Design Thinking
Department of Computer Science & Engineering, New Horizon College of Engineering (NHCE)

Slide 1: Proper Title Cover Page with College, Department, Project Title, and Student/Guide Details.
Slide 2: Problem Overview & Scope Boundaries.
Slide 3: System Architecture & Core Functional Requirements.
Slide 4: Non-Functional Requirements, Security & Medical Ethics.
Slide 5: Executive Summary, Key Takeaways & Q&A (Completely Clean, Zero URLs).
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_executive_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Executive Dark Palette (Deep Midnight Slate, Refined Cards, Cobalt & Emerald Accents)
    BG_DARK = RGBColor(15, 23, 42)          # Deep Midnight Slate (#0F172A)
    HEADER_BG = RGBColor(11, 15, 25)        # Slate 950 (#0B0F19)
    CARD_BG = RGBColor(30, 41, 59)          # Refined Slate (#1E293B)
    CARD_BG_SUBTLE = RGBColor(24, 33, 49)   # Slate 850
    CARD_BORDER = RGBColor(51, 65, 85)      # Slate 700 (#334155)
    CARD_BORDER_BLUE = RGBColor(59, 130, 246) # Cobalt Blue (#3B82F6)
    
    PRIMARY_BLUE = RGBColor(59, 130, 246)   # Cobalt Blue (#3B82F6)
    ACCENT_MINT = RGBColor(16, 185, 129)    # Emerald (#10B981)
    ACCENT_AMBER = RGBColor(245, 158, 11)   # Executive Amber (#F59E0B)
    
    TEXT_WHITE = RGBColor(255, 255, 255)    # High-contrast White
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

    def add_header(slide, title, category="COMMUNITY PROJECT • COURSE 25CPD37", slide_num=1):
        hdr_panel = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.18))
        hdr_panel.fill.solid()
        hdr_panel.fill.fore_color.rgb = HEADER_BG
        hdr_panel.line.fill.background()

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

        # Slide Number
        tx_num = slide.shapes.add_textbox(Inches(11.5), Inches(0.40), Inches(1.0), Inches(0.4))
        tf_num = tx_num.text_frame
        tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
        p_num = tf_num.paragraphs[0]
        p_num.text = f"0{slide_num} / 05"
        p_num.font.size = Pt(13)
        p_num.font.bold = True
        p_num.font.color.rgb = TEXT_MUTED
        p_num.alignment = PP_ALIGN.RIGHT

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
    # SLIDE 1: PROPER EXECUTIVE COVER / TITLE PAGE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Top Institutional Header Box
    inst_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(11.733), Inches(1.15))
    inst_box.fill.solid()
    inst_box.fill.fore_color.rgb = HEADER_BG
    inst_box.line.color.rgb = CARD_BORDER
    inst_box.line.width = Pt(1.5)

    tx_inst = s1.shapes.add_textbox(Inches(0.8), Inches(0.48), Inches(11.733), Inches(1.1))
    tf_inst = tx_inst.text_frame
    setup_card_tf(tf_inst)
    
    p_inst1 = tf_inst.paragraphs[0]
    p_inst1.text = "NEW HORIZON COLLEGE OF ENGINEERING"
    p_inst1.font.size = Pt(17)
    p_inst1.font.bold = True
    p_inst1.font.color.rgb = TEXT_WHITE
    p_inst1.alignment = PP_ALIGN.CENTER
    p_inst1.space_after = Pt(2)

    p_inst2 = tf_inst.add_paragraph()
    p_inst2.text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING"
    p_inst2.font.size = Pt(12)
    p_inst2.font.bold = True
    p_inst2.font.color.rgb = PRIMARY_BLUE
    p_inst2.alignment = PP_ALIGN.CENTER
    p_inst2.space_after = Pt(2)

    p_inst3 = tf_inst.add_paragraph()
    p_inst3.text = "Course: Community Project using Innovation and Design Thinking (25CPD37 • Semester III)"
    p_inst3.font.size = Pt(9.5)
    p_inst3.font.color.rgb = TEXT_MUTED
    p_inst3.alignment = PP_ALIGN.CENTER

    # Center Hero Title Box
    title_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(11.733), Inches(2.35))
    title_box.fill.solid()
    title_box.fill.fore_color.rgb = CARD_BG
    title_box.line.color.rgb = CARD_BORDER_BLUE
    title_box.line.width = Pt(2)

    tx_tb = s1.shapes.add_textbox(Inches(0.8), Inches(1.95), Inches(11.733), Inches(2.15))
    tf_tb = tx_tb.text_frame
    setup_card_tf(tf_tb)

    p_badge = tf_tb.paragraphs[0]
    p_badge.text = "PROJECT PRESENTATION • REQUIREMENTS & ARCHITECTURE"
    p_badge.font.size = Pt(10)
    p_badge.font.bold = True
    p_badge.font.color.rgb = ACCENT_MINT
    p_badge.alignment = PP_ALIGN.CENTER
    p_badge.space_after = Pt(6)

    p_maint = tf_tb.add_paragraph()
    p_maint.text = "Health and Nutrition Awareness Web Application\nfor College Students"
    p_maint.font.size = Pt(24)
    p_maint.font.bold = True
    p_maint.font.color.rgb = TEXT_WHITE
    p_maint.alignment = PP_ALIGN.CENTER
    p_maint.space_after = Pt(6)

    p_subt = tf_tb.add_paragraph()
    p_subt.text = "NutriCampus: A Student-Friendly Nutrition, Hydration & Wellness Platform"
    p_subt.font.size = Pt(12.5)
    p_subt.font.bold = True
    p_subt.font.color.rgb = PRIMARY_BLUE
    p_subt.alignment = PP_ALIGN.CENTER

    # Bottom Two Info Cards (Presenters & Mentors)
    # Presenters Card
    pres_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.45), Inches(5.66), Inches(2.3))
    pres_box.fill.solid()
    pres_box.fill.fore_color.rgb = CARD_BG
    pres_box.line.color.rgb = CARD_BORDER
    pres_box.line.width = Pt(1.5)

    tx_pres = s1.shapes.add_textbox(Inches(0.8), Inches(4.5), Inches(5.66), Inches(2.2))
    tf_pres = tx_pres.text_frame
    setup_card_tf(tf_pres)
    add_para(tf_pres, "PRESENTED BY (STUDENT TEAM):", pt_size=11, bold=True, color=PRIMARY_BLUE, space_after=6)
    add_para(tf_pres, "Student Team Member 1  (USN: 1NH25CS___)", pt_size=11, bold=True, color=TEXT_WHITE, space_after=3)
    add_para(tf_pres, "Student Team Member 2  (USN: 1NH25CS___)", pt_size=11, bold=True, color=TEXT_WHITE, space_after=5)
    add_para(tf_pres, "Department: Computer Science & Engineering", pt_size=10, color=TEXT_BODY, space_after=2)
    add_para(tf_pres, "Batch & Academic Term: 3rd Semester B.E. (2026–2027)", pt_size=10, color=TEXT_MUTED, space_after=2)

    # Mentors Card
    ment_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.86), Inches(4.45), Inches(5.66), Inches(2.3))
    ment_box.fill.solid()
    ment_box.fill.fore_color.rgb = CARD_BG
    ment_box.line.color.rgb = CARD_BORDER
    ment_box.line.width = Pt(1.5)

    tx_ment = s1.shapes.add_textbox(Inches(6.86), Inches(4.5), Inches(5.66), Inches(2.2))
    tf_ment = tx_ment.text_frame
    setup_card_tf(tf_ment)
    add_para(tf_ment, "ACADEMIC MENTORSHIP & GUIDANCE:", pt_size=11, bold=True, color=ACCENT_MINT, space_after=6)
    add_para(tf_ment, "Project Guide & Mentor: Faculty Member, Dept. of CSE", pt_size=10.5, color=TEXT_WHITE, space_after=3)
    add_para(tf_ment, "Course Coordinator: 25CPD37 Faculty Committee", pt_size=10.5, color=TEXT_WHITE, space_after=3)
    add_para(tf_ment, "Head of Department: Department of CSE, NHCE", pt_size=10.5, color=TEXT_WHITE, space_after=5)
    add_para(tf_ment, "Institutional Affiliation: Visvesvaraya Technological University (VTU)", pt_size=9.5, color=TEXT_MUTED, space_after=2)

    # Slide 1 Footer
    div_f1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.95), Inches(11.733), Inches(0.015))
    div_f1.fill.solid()
    div_f1.fill.fore_color.rgb = CARD_BORDER
    div_f1.line.fill.background()

    tx_f1 = s1.shapes.add_textbox(Inches(0.8), Inches(7.02), Inches(11.733), Inches(0.3))
    tf_f1 = tx_f1.text_frame
    p_f1 = tf_f1.paragraphs[0]
    p_f1.text = "New Horizon College of Engineering  |  Autonomous College Affiliated to VTU  |  Accredited by NAAC with 'A' Grade"
    p_f1.font.size = Pt(9)
    p_f1.font.color.rgb = TEXT_DIM
    p_f1.alignment = PP_ALIGN.CENTER

    set_speaker_notes(s1,
        "WHAT TO SAY OUT LOUD:\n"
        "\"Good morning respected evaluators, project guide, and faculty members. "
        "We are pleased to present NutriCampus, our Community Engineering Project developed under Course 25CPD37 "
        "in the Department of Computer Science and Engineering at New Horizon College of Engineering.\n\n"
        "Our project addresses the vital health, hydration, and nutritional realities faced by undergraduate college students.\""
    )

    # =========================================================================
    # SLIDE 2: Problem Overview & Scope Boundaries
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Problem Overview & System Scope Boundaries", category="PROJECT SCOPE MATRIX • COURSE 25CPD37", slide_num=2)

    # Left: Problem Overview
    s2_l = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_col, card_top, w_half, card_h)
    s2_l.fill.solid()
    s2_l.fill.fore_color.rgb = CARD_BG
    s2_l.line.color.rgb = CARD_BORDER
    s2_l.line.width = Pt(1.5)

    tx_s2_l = s2.shapes.add_textbox(left_col, card_top, w_half, card_h)
    tf_s2_l = tx_s2_l.text_frame
    setup_card_tf(tf_s2_l)
    add_para(tf_s2_l, "Problem Definition & Need", pt_size=14, bold=True, color=TEXT_WHITE, space_after=8)

    add_para(tf_s2_l, "CORE PROBLEM STATEMENT", pt_size=10, bold=True, color=PRIMARY_BLUE, space_after=3)
    add_para(tf_s2_l, "\"Undergraduate students face irregular eating schedules, chronic lab fatigue, and heavy reliance on low-nutrient canteen snacks with zero accessible guidance.\"", pt_size=10.5, color=TEXT_LIGHT, space_after=10)

    add_para(tf_s2_l, "CRITICAL STUDENT PAIN POINTS", pt_size=10, bold=True, color=TEXT_MUTED, space_after=4)
    add_para(tf_s2_l, "Irregular meal hours caused by demanding lab schedules", pt_size=10, bullet=True, space_after=2.5)
    add_para(tf_s2_l, "Heavy intake of ultra-processed, fried canteen snacks", pt_size=10, bullet=True, space_after=2.5)
    add_para(tf_s2_l, "Daytime dehydration leading to afternoon lecture fatigue", pt_size=10, bullet=True, space_after=2.5)
    add_para(tf_s2_l, "Clinical health applications are overly complex and intimidating", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s2_l, "PRIMARY SYSTEM OBJECTIVE", pt_size=10, bold=True, color=ACCENT_MINT, space_after=3)
    add_para(tf_s2_l, "Deliver an accessible, zero-barrier web tool translating nutritional science into realistic canteen food swaps, safe hydration tracking, and screening.", pt_size=10, color=TEXT_BODY, space_after=2)

    # Right: Scope Matrix
    s2_r = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_col, card_top, w_half, card_h)
    s2_r.fill.solid()
    s2_r.fill.fore_color.rgb = CARD_BG
    s2_r.line.color.rgb = CARD_BORDER
    s2_r.line.width = Pt(1.5)

    tx_s2_r = s2.shapes.add_textbox(right_col, card_top, w_half, card_h)
    tf_s2_r = tx_s2_r.text_frame
    setup_card_tf(tf_s2_r)
    add_para(tf_s2_r, "System Scope & Target Users", pt_size=14, bold=True, color=TEXT_WHITE, space_after=8)

    add_para(tf_s2_r, "IN-SCOPE DELIVERABLES (VERSION 1.0)", pt_size=10, bold=True, color=ACCENT_MINT, space_after=3)
    add_para(tf_s2_r, "50-25-25 balanced dietary guidance plate model", pt_size=10, bullet=True, space_after=2)
    add_para(tf_s2_r, "Campus canteen and hostel food alternative database", pt_size=10, bullet=True, space_after=2)
    add_para(tf_s2_r, "Metric/Imperial anthropometric BMI screening module", pt_size=10, bullet=True, space_after=2)
    add_para(tf_s2_r, "Daily fluid tracker with 5.0 Liter safety ceiling", pt_size=10, bullet=True, space_after=2)
    add_para(tf_s2_r, "Interactive 7-item nutrition myth-busting quiz", pt_size=10, bullet=True, space_after=2)
    add_para(tf_s2_r, "Community feedback portal for pilot evaluation", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s2_r, "OUT-OF-SCOPE EXCLUSIONS (BOUNDARIES)", pt_size=10, bold=True, color=ACCENT_AMBER, space_after=3)
    add_para(tf_s2_r, "No clinical medical diagnosis or therapeutic prescription regimens", pt_size=10, bullet=True, space_after=2)
    add_para(tf_s2_r, "No calorie counting or restrictive dietary prescription models", pt_size=10, bullet=True, space_after=2)
    add_para(tf_s2_r, "No hardware sensors or wearable biometric synchronization", pt_size=10, bullet=True, space_after=8)

    add_para(tf_s2_r, "TARGET STAKEHOLDERS", pt_size=10, bold=True, color=PRIMARY_BLUE, space_after=3)
    add_para(tf_s2_r, "Undergraduate students, hostelites, lab programmers, and 12+ peer testers.", pt_size=10, color=TEXT_BODY, space_after=2)

    set_speaker_notes(s2,
        "WHAT TO SAY OUT LOUD:\n"
        "\"In Slide 2, we establish our core problem definition and system boundaries.\n\n"
        "Undergraduate students routinely experience irregular meal routines, long lab hours, and heavy canteen reliance. "
        "In Scope for v1, we provide six core modules: visual meal portioning, practical canteen swaps, metric BMI screening, "
        "a safe hydration tracker capped at 5 liters, educational quizzes, and community feedback.\n\n"
        "Out of Scope, we draw a clear line excluding clinical medical diagnosis, restrictive calorie counting, or hardware sensors.\""
    )

    # =========================================================================
    # SLIDE 3: System Architecture & Core Functional Requirements
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
    s3_r.line.color.rgb = CARD_BORDER_BLUE
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
    # SLIDE 4: Non-Functional Requirements, Security & Medical Ethics
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Non-Functional Requirements & Medical Ethics", category="SYSTEM QUALITY STANDARDS • COURSE 25CPD37", slide_num=4)

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
    # SLIDE 5: Executive Summary & Evaluation Discussion (Completely Clean)
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
    p2_box.line.color.rgb = CARD_BORDER_BLUE
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

    # Clean Executive Conclusion Banner (NO URLs)
    term_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.32), Inches(11.733), Inches(1.48))
    term_box.fill.solid()
    term_box.fill.fore_color.rgb = HEADER_BG
    term_box.line.color.rgb = CARD_BORDER
    term_box.line.width = Pt(1.5)

    tx_term = s5.shapes.add_textbox(Inches(0.8), Inches(5.32), Inches(11.733), Inches(1.48))
    tf_term = tx_term.text_frame
    setup_card_tf(tf_term)

    p_term_q = tf_term.paragraphs[0]
    p_term_q.text = "THANK YOU!"
    p_term_q.font.size = Pt(18)
    p_term_q.font.bold = True
    p_term_q.font.color.rgb = TEXT_WHITE
    p_term_q.alignment = PP_ALIGN.CENTER
    p_term_q.space_after = Pt(3)

    p_term_sub = tf_term.add_paragraph()
    p_term_sub.text = "Questions, Feedback & Evaluation Discussion"
    p_term_sub.font.size = Pt(13)
    p_term_sub.font.bold = True
    p_term_sub.font.color.rgb = PRIMARY_BLUE
    p_term_sub.alignment = PP_ALIGN.CENTER
    p_term_sub.space_after = Pt(4)

    p_term_ack = tf_term.add_paragraph()
    p_term_ack.text = "Department of Computer Science & Engineering  |  New Horizon College of Engineering, Bengaluru"
    p_term_ack.font.size = Pt(9.5)
    p_term_ack.font.color.rgb = TEXT_MUTED
    p_term_ack.alignment = PP_ALIGN.CENTER

    set_speaker_notes(s5,
        "WHAT TO SAY OUT LOUD:\n"
        "\"To wrap up our presentation in 20 seconds:\n"
        "1. NutriCampus demonstrates human-centered Design Thinking tailored specifically for undergraduate student wellness.\n"
        "2. It delivers zero-barrier accessibility, functioning offline and in the cloud with zero downloads.\n"
        "3. It has been empirically validated through our pilot study with 12 peer evaluators.\n\n"
        "Thank you respected faculty and evaluators. We now open the floor for your questions!\""
    )

    target_files = [
        output_path,
        os.path.join(os.path.dirname(output_path), "NutriCampus_Professional_Dark_Presentation.pptx"),
        os.path.join(os.path.dirname(output_path), "NutriCampus_SRS_Presentation.pptx"),
        os.path.join(os.path.dirname(output_path), "NutriCampus_Executive_Deck_Final.pptx")
    ]
    
    saved_paths = []
    for p in target_files:
        try:
            prs.save(p)
            print(f"[SUCCESS] Saved presentation to: {p}")
            saved_paths.append(p)
        except PermissionError:
            print(f"[NOTICE] {os.path.basename(p)} is currently open in PowerPoint. Skipping...")
        except Exception as e:
            print(f"[ERROR] Could not save {p}: {e}")

    if not saved_paths:
        import time
        ts_path = os.path.join(os.path.dirname(output_path), f"NutriCampus_Deck_{int(time.time())}.pptx")
        prs.save(ts_path)
        print(f"[SUCCESS] Saved with timestamp fallback: {ts_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hi\.gemini\antigravity\scratch\NutriCampus-Health-Nutrition"
    out_file = os.path.join(out_dir, "NutriCampus_5Slide_SRS_Deck.pptx")
    build_executive_deck(out_file)
