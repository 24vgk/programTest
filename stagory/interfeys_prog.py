import PySimpleGUI as sg
import test_dog
import tab_list
import def_x


path_users_file = 'file/users.csv'
combo = sg.Combo(def_x.name_list(path_users_file))
layout = [
    [sg.Text('Выберите действие'),
     sg.Checkbox('Тест по деталям'), sg.Checkbox('Тест по Договорам'),
     sg.Text('Введите колличество заданий'), sg.InputText(size=(2, 1), border_width=2, tooltip='Введите число заданий')
     ], [combo],
    [sg.Output(size=(60, 5))],
    [sg.Submit(button_text='Сформировать Тест'), sg.Submit(button_text='Поиграть'), sg.Cancel(button_text='Выйти')]
]
window = sg.Window('МЕНЮ ТЕСТОВ', layout, finalize=True)
while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Выйти'):
        break
    elif event == 'Сформировать Тест':
        if values[0]:
            if values[3] == 'Калабин Андрей Сергеевич':
                if values[2]:
                    flag = False
                    tab_list.tab(int(values[2]), flag)
                else:
                    print('Введите количество заданий!!!')
            elif not values[3]:
                print('МЫ ВАС НЕ УЗНАЛИ!!! НАйдите себя в списке!')
            else:
                if values[2]:
                    flag = True
                    tab_list.tab(int(values[2]), flag)
                else:
                    print('Введите количество заданий!!!')
                print('Тест сформирован')
        elif values[1]:
            if values[2]:
                if values[3] == 'Калабин Андрей Сергеевич':
                    test_dog.test(int(values[2]))
                    print('Уважаемый Андрей Сергеевич! Все тесты сформированы!')
                elif not values[3]:
                    print('МЫ ВАС НЕ УЗНАЛИ!!! НАйдите себя в списке!')
                else:
                    test_dog.test_indiv(values[3], int(values[2]))
                print('Тест по Договрам сформирован')
            else:
                print('Введите количество задач для Теста по Договорам')
        elif not values[0] and not values[1]:
            print('Выберите тест для формирования')
    elif event == 'Поиграть':
        sg.SystemTray.notify('ИГРЫ КОНЧИЛИСЬ', 'ПОРА ДОМОЙ!!!')
    else:
        print('МЫ ВАС НЕ УЗНАЛИ!!! НАйдите себя в списке!')
window.close()