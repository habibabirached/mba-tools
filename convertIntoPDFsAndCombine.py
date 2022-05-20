import os
import pandas as pd
import pdfkit
import win32com.client
from pathlib import Path
from PyPDF2 import PdfFileMerger

wdFormatPDF = 17

word = win32com.client.DispatchEx('Word.Application')
word.Visible = True

#### Change this to your correct path
rootdir = 'C:/Users/PCII-Researcher-02/Desktop/MAY-5-DATA-PROCESSING/ALLDATA'

for path in Path(rootdir).iterdir():
    print('\n##################################################')
    if path.is_dir():
        print(path)
        subject_id = str(path.stem).replace('Data','')
        print('subject_id = ',subject_id)

        # convert RTF and CSV files to PDF                
        for subpath in Path(path).iterdir():
            
            suffix = Path(subpath).suffix.lower()
            parentDir = Path(subpath).parent
            stemName = Path(subpath).stem
            onlyFilename = Path(subpath).name
            
            if 'rtf' in suffix:
                print('Found valid RTF: ',subpath)
                
                outFile = str(parentDir) + '/' + str(stemName) + '.pdf'

                doc = word.Documents.Open(str(subpath))
                doc.SaveAs(outFile,FileFormat=wdFormatPDF)
                doc.Close()
  
            elif 'csv' in suffix:
                if not str(stemName).lower().endswith('mab') and not str(onlyFilename).lower().startswith('hq'):
                
                    print('Found valid CSV: ',subpath)
                    csv_file = pd.read_csv(subpath)
                    csv_file.to_html(str(subpath) + '.html')

                    html_file = str(subpath) + '.html'
                    pdf_file = str(subpath) + '.pdf'

                    #### Change this to the correct path on your computer
                    path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
                    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

                    with open(html_file,'r') as inFile:
                        pdfkit.from_file(inFile, pdf_file)

                    os.remove(html_file)

        print('\nNOW COMBINE ALL PDFs into one\n')

        searchPath = str(path) + '/*.pdf'
            
        list_of_pdfs = []
        for filename in os.listdir(str(path)):
            if filename.endswith('.pdf'):
                if filename.startswith(subject_id) or filename.endswith('.csv.pdf'):
                    fullfilename = str(path) + '/' + filename
                    list_of_pdfs.append(fullfilename)
                
        merger = PdfFileMerger()
        for pdffile in list_of_pdfs:
            merger.append(pdffile)
        combinedpdffile = str(path) + '\AllCombined.pdf'
        print('combinedpdffile = ',combinedpdffile)
        
        merger.write(combinedpdffile)
        merger.close()

        for pdffile in list_of_pdfs:
            os.remove(pdffile)

word.Quit()

