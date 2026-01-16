import os
import shutil

# посмотреть путь файла
CURRENT_FILE = os.path.abspath(__file__)

# путь до директории
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

# скрипт позволяюший делать путь до файла универсальным для всех ОС
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(TMP_DIR)

# если существует путь то
if not os.path.exists('tmp2'):
    os.mkdir('tmp2')
    print('создал')
else:
    print('не создал')    
    
# # создание директори
# os.mkdir('tmp2')

# удаление директори вместе с файлами
# shutil.rmtree(os.path.join(CURRENT_DIR, 'tmp2'))
