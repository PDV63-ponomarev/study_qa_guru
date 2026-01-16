# библиотека чтения пдф
# pip install pypdf

import os
from pypdf import PdfReader

reader =  PdfReader(r'tmp\test_pdf.pdf')

# print(reader.pages)
# # количество страниц
# print(len(reader.pages))

# посмотреть текст первую страницу
# print(reader.pages[0].extract_text())

# assert 'Daniel Arbuckle' in reader.pages[0]

# проверка сравненя размера файла в байтах
print(os.path.getsize(r'tmp\test_pdf.pdf'))
assert os.path.getsize(r'tmp\test_pdf.pdf') == 2048650
