'''
Created on 13-Feb-2021

@author: Achudan
'''
from pdf2image import convert_from_path
from fitz import *

def Convert_PDF_to_Image(op_pdf_file, output_image_file):
    doc = fitz.open(op_pdf_file)
    page = doc.loadPage(0)
    zoom = 10
    mat = fitz.Matrix(zoom, zoom)
    pix = page.getPixmap(matrix = mat)
    pix.writePNG(output_image_file)