from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob('TextFiles/*.txt')

for filepath in filepaths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    print(filename)

    pdf.set_font(family='Times', style='B', size=26)
    pdf.cell(w = 80, h = 20, txt=filename.capitalize(), border = 0, ln = 1, align = 'L', fill = False)
    pdf.output(f'text-pdfs/{filename}.pdf')
