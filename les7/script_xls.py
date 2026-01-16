# pip install xlrd

from xlrd import open_workbook

workbook = open_workbook(r'tmp\xls_test.xls')

# колво листов
print(workbook.nsheets)
# имена
print(workbook.sheet_names())

# посмотреть на первой странице кол-ко строк, столбцов
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
# 4 строка (индекс 3) и 1 столбец (индекс 0)
print(sheet.cell_value(rowx=3,colx=0))

# прочитать все строки
for rx in range(sheet.nrows):
    print(sheet.row(rx))