#!/usr/bin/env python

from pdf2image import convert_from_path
import os


pdf_files = [item for item in os.listdir('.') if '.pdf' in item]

for pdf_file in pdf_files:
    print(f'process {pdf_file}')
    image = convert_from_path(pdf_file)
    out_name = pdf_file.replace('.pdf','.jpg')
    image[0].save(out_name,'JPEG')

