import pandas as pd

cols = [6, 7, 8]
adres = 'C:/Users/kalabin_as/Desktop/СТАЖЕРЫ/Тестовые файлы/УДВ Опер Наличие.xlsx'
excel_data_df = pd.read_excel(adres, sheet_name='Лист2')

# print whole sheet data
print(excel_data_df)
