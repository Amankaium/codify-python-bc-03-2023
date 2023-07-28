from openpyxl import Workbook
from my_package.code_1 import cool_print
# from my_package.my_package_2.code_1 import cool_print


new_excel = Workbook()
page = new_excel.active
page["C4"] = "БУМ!"
new_excel.save("my_first.xlsx")
cool_print("Программа завершена")

