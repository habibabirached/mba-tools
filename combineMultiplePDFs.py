from PyPDF2 import PdfFileMerger
import glob

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

list_pdfs = glob.glob('*.pdf')
print(list_pdfs)

merger = PdfFileMerger()

#for pdf in pdfs:
for pdf in list_pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()


