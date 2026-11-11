"""
MediSense NLP - Master Final Document Assembler.
Compiles both:
1. Project_Documentation/Complete_Project_Documentation.docx
2. Project_Documentation/Complete_Project_Documentation.pdf
"""

import os
import sys
import docx
from docx import Document

from build_complete_report import build_docx
from build_thesis_p2 import write_chapters_3_to_6
from build_thesis_p3 import write_chapters_7_to_11

OUTPUT_DIR = "Project_Documentation"
DOCX_PATH = os.path.join(OUTPUT_DIR, "Complete_Project_Documentation.docx")
PDF_PATH = os.path.join(OUTPUT_DIR, "Complete_Project_Documentation.pdf")

def assemble_docx():
    print("[1/2] Generating Complete University Project Documentation (DOCX)...")
    doc = build_docx()
    write_chapters_3_to_6(doc)
    write_chapters_7_to_11(doc)
    doc.save(DOCX_PATH)
    file_size = os.path.getsize(DOCX_PATH)
    print(f"SUCCESS: Generated {DOCX_PATH} ({file_size / 1024:.1f} KB)")
    return doc

if __name__ == "__main__":
    assemble_docx()
