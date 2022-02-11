import pandas as pd
import def_x


def test(n=0):
    path_zav_file = 'file/dog.csv'
    path_users_file = 'file/users.csv'
    result = {}
    list_adres = []
    adres = 'C:/Users/kalabin_as/Desktop/СТАЖЕРЫ/Тестовые файлы/Наборы стажеров/Тест по Договорам/'
    for i in def_x.name_list(path_users_file):
        adres_name = adres + i + '.xlsx'
        list_adres.append(adres_name)
        num_list = def_x.dog_x(path_zav_file, n)
        result['№ договора'] = num_list
        result['Назначение договора'] = None
        result['Наименование центральной организации'] = None
        result['Дата договора'] = None
        result['Срок действия договора'] = None
        result['Тип пролонгации, автоматический/через ДС'] = None
        result['Код договора в SAP'] = None
        result['Централизованный/Филиальный'] = None
        result['Период выполнения ремонта деталей'] = None
        result[
            'Сроки предоставления документов по ремонту деталей,'
            ' разделка/демонтаж, хранение, погрузка/выгрузка Подрядчиком'
        ] = None
        result[
            'Сроки согласования документов по ремонту деталей, '
            'разделка /демонтаж, хранение, погрузка/выгрузка Заказчиком'
        ] = None
        result['Сроки подписания комплекта документов Подрядчиком'] = None
        result['Сроки подписания комплекта документов Заказчиком'] = None
        result['Срок предоставления СФ Подрядчиком'] = None
        result[
               'Акт о выполненных работах(оказанных услугах), '
               'Акт сдачи-приемки оказанных услуг по хранению, '
               'Акт сдачи-приемки выполненных работ разделка/демонтаж '
        ] = None
        result[
            'Заявка на определение ремонтопригодности и/или ремонт деталей, узлов, колесных пар (заявка на ремонт)'
        ] = None
        result['Счет-фактура'] = None
        result['Заявка на отгрузку деталей'] = None
        result['Расчетно-дефектная ведомость'] = None
        result['Акт приема-передачи материальных ценностей ф. М-15'] = None
        result['Акт выбраковки узлов и деталейе'] = None
        result['Опись деталей и узлов забракованных в металлолом в процессе ремонта'] = None
        result['Заявка на формирование колесных пар'] = None
        result['Акт о приеме-передаче товарно-материальных ценностей на хранение ф. МХ-1'] = None
        result['Акт о возврате товарно-материальных ценностей, сданных на хранение ф. МХ-3'] = None
        result['Расчет стоимости работ по погрузке/ выгрузке'] = None
        result['Отгрузочная разнарядка на выдачу деталей и узлов и металлолома'] = None
        result['Расчет стоимости оказанных услуг по хранению узлов и деталей, металлолома'] = None
        result['Пересылочная ведомость ВУ-50 / Д2'] = None
        result['Отчет о расходах, подлежащих возмещению'] = None
        result['Срок храненния металолома'] = None
        result['Срок хранения деталей'] = None
        try:
            df = pd.DataFrame(result)
            # df.to_excel(adres_name, sheet_name='ТЕСТ ПО ДОГОВОРАМ', index=False)set_column pandas как заполнять
            with pd.ExcelWriter(adres_name, engine='xlsxwriter') as wb:
                df.to_excel(wb, sheet_name='ТЕСТ ПО ДОГОВОРАМ', index=False)
                sheet = wb.sheets['ТЕСТ ПО ДОГОВОРАМ']
                sheet.set_row(0, 100)
                sheet.set_column(0, 0, 40)
                sheet.set_column(1, 1, 20)
                sheet.set_column(2, 31, 20)
                # cell_format = wb.add_format()
                # cell_format.set_font_color('red')
                # sheet.set_align('centre')
        except PermissionError:
            print(f'Не закрыт файл {i}')


def test_indiv(name, n=0):
    path_zav_file = 'file/dog.csv'
    result = {}
    list_adres = []
    adres = 'C:/Users/kalabin_as/Desktop/СТАЖЕРЫ/Тестовые файлы/Наборы стажеров/Тест по Договорам/'
    adres_name = adres + name + '.xlsx'
    list_adres.append(adres_name)
    num_list = def_x.dog_x(path_zav_file, n)
    result['№ договора'] = num_list
    result['Назначение договора'] = None
    result['Наименование центральной организации'] = None
    result['Дата договора'] = None
    result['Срок действия договора'] = None
    result['Тип пролонгации, автоматический/через ДС'] = None
    result['Код договора в SAP'] = None
    result['Централизованный/Филиальный'] = None
    result['Период выполнения ремонта деталей'] = None
    result[
        'Сроки предоставления документов по ремонту деталей,'
        ' разделка/демонтаж, хранение, погрузка/выгрузка Подрядчиком'
    ] = None
    result[
        'Сроки согласования документов по ремонту деталей, '
        'разделка /демонтаж, хранение, погрузка/выгрузка Заказчиком'
    ] = None
    result['Сроки подписания комплекта документов Подрядчиком'] = None
    result['Сроки подписания комплекта документов Заказчиком'] = None
    result['Срок предоставления СФ Подрядчиком'] = None
    result[
           'Акт о выполненных работах(оказанных услугах), '
           'Акт сдачи-приемки оказанных услуг по хранению, '
           'Акт сдачи-приемки выполненных работ разделка/демонтаж '
    ] = None
    result[
        'Заявка на определение ремонтопригодности и/или ремонт деталей, узлов, колесных пар (заявка на ремонт)'
    ] = None
    result['Счет-фактура'] = None
    result['Заявка на отгрузку деталей'] = None
    result['Расчетно-дефектная ведомость'] = None
    result['Акт приема-передачи материальных ценностей ф. М-15'] = None
    result['Акт выбраковки узлов и деталейе'] = None
    result['Опись деталей и узлов забракованных в металлолом в процессе ремонта'] = None
    result['Заявка на формирование колесных пар'] = None
    result['Акт о приеме-передаче товарно-материальных ценностей на хранение ф. МХ-1'] = None
    result['Акт о возврате товарно-материальных ценностей, сданных на хранение ф. МХ-3'] = None
    result['Расчет стоимости работ по погрузке/ выгрузке'] = None
    result['Отгрузочная разнарядка на выдачу деталей и узлов и металлолома'] = None
    result['Расчет стоимости оказанных услуг по хранению узлов и деталей, металлолома'] = None
    result['Пересылочная ведомость ВУ-50 / Д2'] = None
    result['Отчет о расходах, подлежащих возмещению'] = None
    result['Срок храненния металолома'] = None
    result['Срок хранения деталей'] = None
    try:
        df = pd.DataFrame(result)
        with pd.ExcelWriter(adres_name, engine='xlsxwriter') as wb:
            df.to_excel(wb, sheet_name='ТЕСТ ПО ДОГОВОРАМ', index=False)
            sheet = wb.sheets['ТЕСТ ПО ДОГОВОРАМ']
            sheet.set_row(0, 100)
            sheet.set_column(0, 0, 40)
            sheet.set_column(1, 1, 20)
            sheet.set_column(2, 31, 30)
    except PermissionError:
        print(f'Не закрыт файл {name}')


if __name__ == '__main__':
    test()
