import pandas as pd
import def_x


path_zav_file = 'file/zav.csv'
path_users_file = 'file/users.csv'
result = {}
df = pd.DataFrame(result)
list_adres = []
adres = 'C:/Users/kalabin_as/Desktop/СТАЖЕРЫ/Тестовые файлы/Для цитрикс/'
for i in def_x.name_list(path_users_file):
    adres_name = adres + i + '.xlsx'
    list_adres.append(adres_name)
    df.to_excel(adres_name, sheet_name='ДАНО', index=False)