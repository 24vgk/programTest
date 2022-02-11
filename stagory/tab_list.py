import pandas as pd
import def_x


def tab(FLAG_X = False):
    path_zav_file = 'file/det.csv'
    path_users_file = 'file/users.csv'
    result = {}
    list_adres = []
    adres = 'C:/Users/kalabin_as/Desktop/СТАЖЕРЫ/Тестовые файлы/Наборы стажеров/'
    for i in def_x.name_list(path_users_file):
        if FLAG_X:
            adres_name = adres + i + '.xlsx'
            list_adres.append(adres_name)
            num_list = def_x.det_x(path_zav_file)
            name_det = def_x.name_det('file/namedet.csv')
            result['Номер детали'] = num_list
            result['Наименование детали'] = name_det
            tol_list_x = []
            for n in name_det:
                if n.strip() == 'Колесная пара':
                    tol_list_x.append(def_x.tol_kp('file/tol_kp.csv'))
                else:
                    tol_list_x.append(None)
            result['Толщина обода'] = None
            vid_rem_x = []
            for j in name_det:
                if j.strip() == 'Колесная пара':
                    vid_rem_x.append(def_x.rem('file/vidrem.csv'))
                else:
                    vid_rem_x.append('Участковый ремонт')
            result['Вид ремонта'] = None
            result['Цена детали до ремонта'] = None
            result['Состояние детали до ремонта'] = None
            result['Состояние детали после ремонта'] = None
            result['Цена детали после ремонта'] = None
            result['Лом (Есть/Нет'] = None
            result['Лом (Вес)'] = None
            result['Категория Лома'] = None
            result['Договор'] = None
            df = pd.DataFrame(result)
            df.to_excel(adres_name, sheet_name='ДАНО', index=False)
        else:
            adres_name = adres + i + '.xlsx'
            list_adres.append(adres_name)
            num_list = def_x.det_x(path_zav_file)
            name_det = def_x.name_det('file/namedet.csv')
            result['Номер детали'] = num_list
            result['ID детали'] = None
            result['Наименование детали'] = None
            result['Толщина обода'] = None
            result['ID Ремонта'] = None
            result['ID Пересылки1'] = None
            result['ID Пересылки2'] = None
            result['С какого Вагона'] = None
            result['Дата'] = None
            result['Собственность'] = None
            result['Сколько деталей в Пересылке1'] = None
            result['Сколько деталей в Ремонте'] = None
            result['Пересылка1 готова?'] = None
            result['Склад образования'] = None
            df = pd.DataFrame(result)
            df.to_excel(adres_name, sheet_name='ДАНО', index=False)