import pandas as pd
import pdfkit

filename = 'Jane,Doe.csv'

csv_file = pd.read_csv(filename)

csv_file.to_html(filename + '.html')

html_file = filename + '.html'
pdf_file = filename + '.pdf'

pdfkit.from_file(html_file, pdf_file)

