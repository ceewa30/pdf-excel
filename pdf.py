from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pages = row['Pages']
    # Header Page
    for i in range(pages):
        pdf.add_page()
        pdf.set_font('Arial', 'B', 24)
        pdf.set_text_color(100,100,100)
        # pdf.cell(w = 40, h = 10, txt="Hello World!", border = 0, ln = 1, align = 'L', fill = False, link = 'http://www.ceewa30.com')
        
        pdf.cell(w = 80, h = 10, txt=row['Topic'], border = 0, ln = 1, align = 'L', fill = False)
        # pdf.line(10, 21, 200, 21)
        
        for j in range(20, 290, 10):
            pdf.line(10, j, 200, j)
            

      # Footer Page  
        pdf.ln(265)
        pdf.set_font('Arial', 'I', 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
pdf.output('output.pdf')