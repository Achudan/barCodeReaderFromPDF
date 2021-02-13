'''
Created on 13-Feb-2021

@author: Achudan
'''

from pyzbar import pyzbar
from PIL import Image
from pylibdmtx import pylibdmtx

def get_decoded_value(output_image_file, code_type):
    
    try:
        info = []
        #bar code
        if 'bar' in code_type.lower():
            info = pyzbar.decode(Image.open(output_image_file))
        #Data Matrix code
        if 'matrix' in code_type.lower():
            info = pylibdmtx.decode(Image.open(output_image_file))
        #converting bytes to string
        decoded_value = (info[0].data).decode("utf-8")
        return(decoded_value)
    
    except:
        return ""
        