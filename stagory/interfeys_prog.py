import PySimpleGUI as sg
import time
import test_dog
import tab_list
import def_x

# def countdown(num_of_secs):
#     while num_of_secs:
#         m, s = divmod(num_of_secs, 60)
#         min_sec_format = '{:02d}:{:02d}'.format(m, s)
#         print(min_sec_format, end='/r')
#         time.sleep(1)
#         num_of_secs -= 1
#
#     print('Countdown finished.')
#

path_users_file = 'file/users.csv'
combo = sg.Combo(def_x.name_list(path_users_file))

# text = sg.popup_get_text('Введите Ваше Имя', title='Привет', default_text='Иванов Иван Иванович')
# sg.popup(text)

layout = [
    [sg.Text('Выберите действие'),
     sg.Checkbox('Тест по деталям'), sg.Checkbox('Тест по Договорам'),
     sg.Text('Введите колличество заданий'), sg.InputText(size=(2, 1), border_width=2, tooltip='Введите число заданий')
     ], [combo],
    [sg.Output(size=(60, 5))],
    [sg.Submit(button_text='Сформировать Тест'), sg.Cancel(button_text='Выйти')]
]
window = sg.Window('МЕНЮ ТЕСТОВ', layout)
while True:
    event, values = window.read()
    if values[3]:
        continue
    if event in (None, 'Exit', 'Выйти'):
        break
    if event == 'Сформировать Тест':
        if values[0]:
            tab_list.tab()
        elif values[1]:
            if values[2]:
                if values[3] == 'Калабин Андрей Сергеевич':
                    test_dog.test(int(values[2]))
                elif not values[3]:
                    print('МЫ ВАС НЕ УЗНАЛИ!!! НАйдите себя в списке!')
                else:
                    test_dog.test_indiv(values[3], int(values[2]))
                print('Тест сформирован')
            else:
                print('Введите количество задач')
        elif not values[0] and not values[1]:
            print('Выберите тест для формирования')
    else:
        print('МЫ ВАС НЕ УЗНАЛИ!!! НАйдите себя в списке!')
window.close()