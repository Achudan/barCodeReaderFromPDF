'''
Created on 13-Feb-2021

@author: Achudan
'''

from PyPDF3 import PdfFileWriter, PdfFileReader

def Extract_Code_From_PDF(ip_pdf_file, op_pdf_file, code_type):
    
    output = PdfFileWriter()
    input1 = PdfFileReader(open(ip_pdf_file, "rb"))

    output_page = input1.getPage(0)

    #bar code
    if 'bar' in code_type.lower():
        output_page.cropBox.lowerLeft = (0, 0)
        output_page.cropBox.upperleft = (0, 100)
        output_page.cropBox.lowerRight = (286, 0)
        output_page.cropBox.upperRight = (286, 100)


    #Data Matrix code
    if 'matrix' in code_type.lower():
        output_page.cropBox.lowerLeft = (200, 309)
        output_page.cropBox.upperleft = (200, 378)
        output_page.cropBox.lowerRight = (270, 309)
        output_page.cropBox.upperRight = (270, 378)


    output.addPage(output_page)
    outputStream = open(op_pdf_file, "wb")
    output.write(outputStream)