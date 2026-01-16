from zipfile import ZipFile

with ZipFile(r'tmp\hello.zip') as zip_file:
    # список файлов в архиве
    print(zip_file.namelist())
    
    # посмотреть содерж файла
    text = zip_file.read('rout.txt')
    print(text)
    
    # разархивировать
    zip_file.extract('rout.txt',path = 'tmp')
    