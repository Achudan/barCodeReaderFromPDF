'''
Created on 13-Feb-2021

@author: Achudan
'''

from code_readers.code_Extractor import Extract_Code_From_PDF
from code_readers.PDF_to_Image_Converter import Convert_PDF_to_Image
from code_readers.decode_code_from_images import get_decoded_value

#Input variables. *****has to be updated to get from Property files********
ip_pdf_file = r"C:\Users\Achudan\Downloads\sample.pdf"
op_pdf_file = r"C:\Users\Achudan\Downloads\out.pdf"
code_type = 'data matrix code'
code_type = 'bar code'
output_image_file = r"C:\Users\Achudan\Downloads\converted_code.png"

# extract the bar code/ data matrix code from Label PDF
Extract_Code_From_PDF(ip_pdf_file, op_pdf_file, code_type)

#Converts PDF into Image
Convert_PDF_to_Image(op_pdf_file, output_image_file)

#decrypts the image and return the code
decrypted_code = get_decoded_value(output_image_file, code_type)

print("The decrypted code from ",code_type, " is ",  decrypted_code)