from openpyxl import load_workbook

my_excel = load_workbook("my_first.xlsx")
my_page = my_excel["Sheet"]
my_page["B7"] = "Привет"
my_excel.save("my_first.xlsx")
