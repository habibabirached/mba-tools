import sys
import comtypes.client as cc
import win32com.client
import docx2pdf
from win32com.client import constants

#import aspose.words as aw

'''
inFile = 'C:/Users/PCII-Researcher-02/Desktop/COMBINE-PDF/PAI2.rtf'

outFileDoc = 'C:/Users/PCII-Researcher-02/Desktop/COMBINE-PDF/outdoc.doc'
outFileDocx = 'C:/Users/PCII-Researcher-02/Desktop/COMBINE-PDF/outdoc.docx'

outFilePdf = 'C:/Users/PCII-Researcher-02/Desktop/COMBINE-PDF/outpdf.pdf'

word = win32com.client.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open(inFile)
doc.Activate()

word.ActiveDocument.SaveAs(outFileDoc, FileFormat=constants.wdFormatDocument)
doc.Close(False)

docx2pdf.convert(outFileDocx,outFilePdf)

exit()

doc = aw.Document("PAI2.rtf")
doc.save('newdoc.pdf',aw.SaveFormat.PDF)

exit()
'''

wdFormatPDF = 17

#word = comtypes.client.CreateObject('Word.Application')
#word = cc.CreateObject('Word.Application')
word = win32com.client.DispatchEx('Word.Application')
word.Visible = True

outFile = 'C:/Users/PCII-Researcher-02/Desktop/COMBINE-PDF/out.pdf'

#with open('C:/Users/PCII-Researcher-02/Desktop/COMBINE-PDF/PAI.rtf','r') as inFile:
#   doc = word.Documents.Open(inFile)
#    doc.SaveAs(outFile, FileFormat=wdFormatPDF)
#    doc.Close()
#    word.Quit()
    
doc = word.Documents.Open('C:/Users/PCII-Researcher-02/Desktop/COMBINE-PDF/PAI.rtf')
doc.SaveAs(outFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()

