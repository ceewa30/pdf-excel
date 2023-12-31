import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import datetime

filepaths = glob.glob('invoice/*.xlsx')

for filepath in filepaths:
    
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w = 80, h = 10, txt=f"Invoice no. {invoice_nr}", border = 0, ln = 1, align = 'L', fill = False)
    
    date = date.replace(".", "-")
    invoice_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%m-%d-%Y")

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w = 80, h = 10, txt=f"Date: {invoice_date}", border = 0, ln = 1, align = 'L', fill = False)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]

    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w = 25, h = 8, txt=str(columns[0]), border = 1, align = 'L', fill = False)
    pdf.cell(w = 70, h = 8, txt=str(columns[1]), border = 1, align = 'L', fill = False)
    pdf.cell(w = 40, h = 8, txt=str(columns[2]), border = 1, align = 'L', fill = False)
    pdf.cell(w = 30, h = 8, txt=str(columns[3]), border = 1, align = 'L', fill = False)
    pdf.cell(w = 25, h = 8, txt=str(columns[4]), border = 1, ln = 1, align = 'L', fill = False)

    for index, row in df.iterrows():
        
        pdf.set_font(family='Times', size=12)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w = 25, h = 8, txt=str(row['product_id']), border = 1, align = 'L', fill = False)
        pdf.cell(w = 70, h = 8, txt=str(row['product_name']), border = 1, align = 'L', fill = False)
        pdf.cell(w = 40, h = 8, txt=str(row['amount_purchased']), border = 1, align = 'L', fill = False)
        pdf.cell(w = 30, h = 8, txt=str(row['price_per_unit']), border = 1, align = 'L', fill = False)
        pdf.cell(w = 25, h = 8, txt=str(row['total_price']), border = 1, ln = 1, align = 'L', fill = False)

    total_sum = df.total_price.sum()
    pdf.set_font(family='Times', size=12, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w = 25, h = 8, txt="", border = 0, align = 'L', fill = False)
    pdf.cell(w = 70, h = 8, txt="", border = 0, align = 'L', fill = False)
    pdf.cell(w = 40, h = 8, txt="", border = 0, align = 'L', fill = False)
    pdf.cell(w = 30, h = 8, txt="Total", border = 1, align = 'L', fill = False)
    pdf.cell(w = 25, h = 8, txt=str(total_sum), border = 1, ln = 1, align = 'L', fill = False)

    # Add total sum sentence
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w = 25, h = 8, txt=f"The total price is {str(total_sum)}", ln = 1, align = 'L', fill = False)

    # Add company name and logo
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w = 25, h = 8, txt=f"PythonHow", ln = 1, align = 'L', fill = False)
    pdf.image("pythonhow.png", w=10)

    pdf.output(f'pdfs/{filename}.pdf')