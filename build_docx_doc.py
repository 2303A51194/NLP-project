"""
MediSense NLP - Complete University-Level Academic Thesis & Project Documentation Generator (DOCX).
Target: Department of Computer Science & Engineering, Final-Year Project Evaluation.
Authors: K. Priya (2303A51194) & CH. Harshini (2303A51185)
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

OUTPUT_DIR = "Project_Documentation"
os.makedirs(OUTPUT_DIR, exist_ok=True)
DOCX_PATH = os.path.join(OUTPUT_DIR, "Complete_Project_Documentation.docx")

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def add_header_footer(doc):
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        s.page_width = Inches(8.27)
        s.page_height = Inches(11.69)
        
        # Header
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("MediSense NLP: Hospital Service Quality & Report Simplification")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(100, 116, 139)

        # Footer
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Department of Computer Science & Engineering | Academic Project Report")
        frun.font.name = "Times New Roman"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(100, 116, 139)

def format_paragraph(p, space_after=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

def add_body_paragraph(doc, text, bold_prefix=None, space_after=6):
    p = doc.add_paragraph()
    format_paragraph(p, space_after=space_after)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_chapter_title(doc, chapter_num, chapter_title):
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(4)
    r1 = p.add_run(f"CHAPTER {chapter_num}\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(14)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(2, 132, 199) # Blue accent
    
    r2 = p.add_run(chapter_title.upper())
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(16)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(15, 23, 42) # Slate dark

    # Horizontal divider rule
    p_rule = doc.add_paragraph()
    p_rule.paragraph_format.space_after = Pt(14)
    p_rule_run = p_rule.add_run("—" * 55)
    p_rule_run.font.name = "Times New Roman"
    p_rule_run.font.color.rgb = RGBColor(203, 213, 225)

def add_subheading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(15, 23, 42)

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.italic = True
    r.font.color.rgb = RGBColor(30, 41, 59)

def add_figure(doc, img_path, fig_num, caption):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(10)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(12)
        r_num = p_cap.add_run(f"Figure {fig_num}: ")
        r_num.font.name = "Times New Roman"
        r_num.font.size = Pt(10.5)
        r_num.font.bold = True
        r_num.font.color.rgb = RGBColor(15, 23, 42)
        
        r_txt = p_cap.add_run(caption)
        r_txt.font.name = "Times New Roman"
        r_txt.font.size = Pt(10.5)
        r_txt.font.italic = True
        r_txt.font.color.rgb = RGBColor(71, 85, 105)

def add_code_block(doc, code_str, title="Source Code"):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(2)
    r_t = p_title.add_run(f"Snippet: {title}")
    r_t.font.name = "Consolas"
    r_t.font.size = Pt(9.5)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(3, 105, 161)

    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    cp = cell.paragraphs[0]
    cp.paragraph_format.line_spacing = 1.15
    cp.paragraph_format.space_after = Pt(0)
    r = cp.add_run(code_str)
    r.font.name = "Consolas"
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(30, 41, 59)
    
    p_end = doc.add_paragraph()
    p_end.paragraph_format.space_after = Pt(6)

def add_custom_table(doc, headers, rows_data, table_num, caption):
    p_cap = doc.add_paragraph()
    p_cap.paragraph_format.space_before = Pt(10)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_num = p_cap.add_run(f"Table {table_num}: ")
    r_num.font.name = "Times New Roman"
    r_num.font.size = Pt(10.5)
    r_num.font.bold = True
    r_num.font.color.rgb = RGBColor(15, 23, 42)
    r_txt = p_cap.add_run(caption)
    r_txt.font.name = "Times New Roman"
    r_txt.font.size = Pt(10.5)
    r_txt.font.italic = True

    table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    # Style Header
    for col_idx, header_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_background(cell, "1E3A8A") # Navy Blue
        set_cell_margins(cell, top=140, bottom=140, left=150, right=150)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(header_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    # Style Data Rows
    for row_idx, row_data in enumerate(rows_data):
        bg_hex = "FFFFFF" if row_idx % 2 == 0 else "F1F5F9"
        for col_idx, cell_value in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_background(cell, bg_hex)
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            p = cell.paragraphs[0]
            # Align left for strings, center for numbers/short codes
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if len(str(cell_value)) > 20 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(str(cell_value))
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(30, 41, 59)

    p_post = doc.add_paragraph()
    p_post.paragraph_format.space_after = Pt(8)

print("Writing complete document structure...")
