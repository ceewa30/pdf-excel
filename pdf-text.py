from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob('TextFiles/*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    print(filename)
    pdf.set_font(family='Times', style='B', size=26)
    pdf.cell(w = 80, h = 20, txt=filename.capitalize(), border = 0, ln = 1, align = 'L', fill = False)
    f = open(f"TextFiles/{filename}.txt", "r")
    # insert the texts in pdf
    for x in f:
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt = x, ln = 2, align = 'C', fill = False)
        pdf.ln(10)
    # save the pdf with name .pdf
    # pdf.output("mygfg.pdf")   
    # df = pd.read_fwf(f'TextFiles/{filename}.txt')
    # print(df)
pdf.output(f'text-pdfs/{filename}.pdf')