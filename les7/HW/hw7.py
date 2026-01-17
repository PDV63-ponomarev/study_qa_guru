import os
from zipfile import ZipFile
import shutil #библиотека для простого копирования
from io import BytesIO #библиотека созд временный файл
import pandas as pd #для чтения файлов
from pypdf import PdfReader


# путь до этой папки
DIR_CURRENTS = os.path.dirname(os.path.abspath(__file__))
DIR_CURRENTS = os.path.join(DIR_CURRENTS)

# путь до files
DIR_FILES = os.path.join(DIR_CURRENTS, 'files')


# – Запаковать кодом в zip архив несколько разных файлов: pdf, xlsx, csv;

# путь до архива
archive = os.path.join(DIR_FILES, 'archive.zip')

# создание архива с указанием пути до файла и его имя
if not os.path.exists(archive):
    with ZipFile(archive, 'w') as zip:

        zip.write(os.path.join(DIR_FILES,'some_file.txt'), 'some_file.txt')
        zip.write(os.path.join(DIR_FILES, 'some_csv.csv'), 'some_csv.csv')
        zip.write(os.path.join(DIR_FILES, 'some_pdf.pdf'), 'some_pdf.pdf')
        zip.write(os.path.join(DIR_FILES, 'some_xlsx.xlsx'), 'some_xlsx.xlsx')
        
        print('архив создан, содержимое:\n', zip.namelist())



# посмотреть содержимое архива, разархивировать с создание папки
dop_HW = False
if dop_HW == True:
    with ZipFile(archive) as zip:

        print(zip.namelist())

        for file in zip.namelist():
            zip.extract(file, path = DIR_FILES+'/acrhive')


# – Положить его в ресурсы;
if not os.path.exists(DIR_FILES+'/acrhive'):

    os.mkdir(DIR_FILES+'/acrhive')
    print('Папка создана')

    shutil.copy(archive, DIR_FILES+'/acrhive')
    print('Архив копирован')



# – Реализовать чтение и проверку содержимого каждого файла из архива
#  не распаковывая сам архив


with ZipFile(archive) as zip:
    
    for file in zip.namelist():
       
        print(f'Чтение файла {file}')
        
        if '.txt' in file:
            data = str(zip.read(file))
            print(f'Содержимое {file}:\n',data)

            if 'text' in data:
                print(f'{file} проверку прошел')
            else: 
                print('Проверку не прошел')


        if '.xlsx' in file:
            file_xlsx = zip.read(file)
            
            #создает временный файл 
            file_IO = BytesIO(file_xlsx)        

            # чтение файла с помошью panda
            data = pd.read_excel(file_IO)
            print(f'Содержимое {file}:\n',data)
           
            # if data.isin(['A3']).any().any():
            if (data == 'A3').any().any():
                print(f'{file} проверку прошел')
            else:
                print('Проверку не прошел')

        
        if '.csv' in file:

            file_csv= zip.read(file)
            file_IO = BytesIO(file_csv) 

            data = pd.read_csv(file_IO, sep=None, engine='python')

            print(f'Содержимое {file}:\n',data)

            if (data == 'A3').any().any():
                print(f'{file} проверку прошел')
            else:
                print('Проверку не прошел')


        if '.pdf' in file:

            file_pdf= zip.read(file)
            file_IO = BytesIO(file_pdf) 

            # направление временного файла в ПДФРеадер
            reader =  PdfReader(file_IO)

            # чтение 1 страницы
            data = reader.pages[0].extract_text()

            print(f'Содержимое {file}:\n',data)
           
            if 'Запаковать' in data:
                print(f'{file} проверку прошел')
            else:
                print('Проверку не прошел')
        

        print('~'*10)