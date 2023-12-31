from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob('TextFiles/*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    
    pdf.set_font(family='Times', style='B', size=26)
    pdf.cell(w = 80, h = 20, txt=filename.capitalize(), border = 0, ln = 1, align = 'L', fill = False)
    pdf.line(10, 25, 200, 25)

    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=6, txt = content, align = 'J', fill = False)

pdf.output('text-pdfs/output.pdf')