"""
NLP-Based Hospital Service Quality Analysis in Warangal
Professional Academic PowerPoint Presentation Generator (16:9 Widescreen).
Department of Computer Science & Engineering.
Authors: KATAKAM PRIYA (2303A51194) & CH. HARSHINI (2303A51185)
Supervisor: Mr. Rupesh Mishra, Assistant Professor, Dept. of CSE
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

OUTPUT_DIR = "Project_Presentation"
ASSETS_DIR = os.path.join(OUTPUT_DIR, "Presentation_Assets")
PPTX_PATH = os.path.join(OUTPUT_DIR, "Project_Presentation.pptx")

# 16:9 Widescreen Dimensions
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Color Palette: Modern Healthcare & AI Theme
C_NAVY = RGBColor(15, 23, 42)      # #0F172A Primary Dark
C_TEAL = RGBColor(2, 132, 199)     # #0284C7 Brand Blue/Teal
C_GREEN = RGBColor(16, 185, 129)   # #10B981 Accent Green
C_AMBER = RGBColor(217, 119, 6)    # #D97706 Warning/Benchmark
C_PURPLE = RGBColor(124, 58, 237)  # #7C3AED AI/ML
C_SLATE = RGBColor(100, 116, 139)  # #64748B Secondary Text
C_BODY = RGBColor(51, 65, 85)      # #334155 Body Text
C_BG_CARD = RGBColor(248, 250, 252)# #F8FAFC Card BG
C_BORDER = RGBColor(226, 232, 240) # #E2E8F0 Subtle Border
C_WHITE = RGBColor(255, 255, 255)  # White

def set_slide_background(slide, color=C_WHITE):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, badge_text, title_text, subtitle_text=""):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    # Badge
    p_badge = tf.paragraphs[0]
    p_badge.space_after = Pt(2)
    r_b = p_badge.add_run()
    r_b.text = f"■  {badge_text.upper()}"
    r_b.font.name = "Arial"
    r_b.font.size = Pt(9.5)
    r_b.font.bold = True
    r_b.font.color.rgb = C_TEAL

    # Main Title
    p_title = tf.add_paragraph()
    p_title.space_after = Pt(2)
    r_t = p_title.add_run()
    r_t.text = title_text
    r_t.font.name = "Arial"
    r_t.font.size = Pt(22)
    r_t.font.bold = True
    r_t.font.color.rgb = C_NAVY

    # Subtitle
    if subtitle_text:
        p_sub = tf.add_paragraph()
        r_s = p_sub.add_run()
        r_s.text = subtitle_text
        r_s.font.name = "Arial"
        r_s.font.size = Pt(11)
        r_s.font.italic = True
        r_s.font.color.rgb = C_SLATE

    # Subtle horizontal line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.58), Inches(11.733), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = C_BORDER
    line.line.color.rgb = C_BORDER

def add_footer(slide, current_slide, total_slides=18):
    # Left: Project Title
    tb_l = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(5.5), Inches(0.35))
    tf_l = tb_l.text_frame
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
    p_l = tf_l.paragraphs[0]
    r_l = p_l.add_run()
    r_l.text = "NLP-Based Hospital Service Quality Analysis in Warangal"
    r_l.font.name = "Arial"
    r_l.font.size = Pt(8.5)
    r_l.font.bold = True
    r_l.font.color.rgb = C_SLATE

    # Center: College / Dept
    tb_c = slide.shapes.add_textbox(Inches(6.0), Inches(7.0), Inches(4.5), Inches(0.35))
    tf_c = tb_c.text_frame
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    p_c = tf_c.paragraphs[0]
    p_c.alignment = PP_ALIGN.CENTER
    r_c = p_c.add_run()
    r_c.text = "Dept. of Computer Science & Engineering | Warangal, Telangana"
    r_c.font.name = "Arial"
    r_c.font.size = Pt(8.5)
    r_c.font.color.rgb = C_SLATE

    # Right: Slide Number
    tb_r = slide.shapes.add_textbox(Inches(10.533), Inches(7.0), Inches(2.0), Inches(0.35))
    tf_r = tb_r.text_frame
    tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0
    p_r = tf_r.paragraphs[0]
    p_r.alignment = PP_ALIGN.RIGHT
    r_r = p_r.add_run()
    r_r.text = f"Slide {current_slide} of {total_slides}"
    r_r.font.name = "Arial"
    r_r.font.size = Pt(9)
    r_r.font.bold = True
    r_r.font.color.rgb = C_TEAL

def add_card(slide, left, top, width, height, title, items, accent_color=C_TEAL, bg_color=C_BG_CARD):
    # Background Box
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = C_BORDER
    card.line.width = Pt(1.2)

    # Accent Top Strip
    strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Inches(0.08))
    strip.fill.solid()
    strip.fill.fore_color.rgb = accent_color
    strip.line.fill.background()

    # Content Box
    tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), height - Inches(0.28))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    # Title
    p_title = tf.paragraphs[0]
    p_title.space_after = Pt(8)
    r_t = p_title.add_run()
    r_t.text = title
    r_t.font.name = "Arial"
    r_t.font.size = Pt(13)
    r_t.font.bold = True
    r_t.font.color.rgb = accent_color

    # Items
    for item in items:
        p = tf.add_paragraph()
        p.space_after = Pt(5)
        r = p.add_run()
        if isinstance(item, tuple):
            r_bold = p.add_run()
            r_bold.text = item[0] + " "
            r_bold.font.name = "Arial"
            r_bold.font.size = Pt(10)
            r_bold.font.bold = True
            r_bold.font.color.rgb = C_NAVY
            r.text = item[1]
        else:
            r.text = "• " + item
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = C_BODY

def add_metric_pill(slide, left, top, width, height, value, label, accent_color=C_TEAL):
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    box.fill.solid()
    box.fill.fore_color.rgb = C_BG_CARD
    box.line.color.rgb = accent_color
    box.line.width = Pt(1.5)

    tb = slide.shapes.add_textbox(left, top + Inches(0.1), width, height - Inches(0.2))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p_val = tf.paragraphs[0]
    p_val.alignment = PP_ALIGN.CENTER
    r_v = p_val.add_run()
    r_v.text = value
    r_v.font.name = "Arial"
    r_v.font.size = Pt(20)
    r_v.font.bold = True
    r_v.font.color.rgb = accent_color

    p_lbl = tf.add_paragraph()
    p_lbl.alignment = PP_ALIGN.CENTER
    r_l = p_lbl.add_run()
    r_l.text = label
    r_l.font.name = "Arial"
    r_l.font.size = Pt(8.5)
    r_l.font.color.rgb = C_SLATE

print("Helper functions for PPTX initialized.")
