#Openpyxl is a python library used to work with excel spredsheet

#1.create new excel files
#2.read existing excel file
#3.write data into cells
#4.delete rows adn columns
#5.work with multiple sheets
# Installation: python -m pip install openpyxl

import openpyxl
#Reading an existing excel file.

workbook=openpyxl.load_workbook("C:\\Users\\ASUS\\Downloads\\student_data.xlsx")
sheet=workbook["data"]
print(sheet["A2"].value)
print(sheet["B2"].value)
#print(sheet["D2"].value)- > None

#Reading all rows from an excel file.

workbook=openpyxl.load_workbook("C:\\Users\\ASUS\\Downloads\\student_data.xlsx")
sheet=workbook["data"]
for row in sheet.iter_rows(values_only=True):
    print(row)
print(sheet.max_row)
print(sheet.max_column)