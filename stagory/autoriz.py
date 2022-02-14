import PySimpleGUI as sg
import mysql


def avtoriz():
    layout = [
        [sg.Text('Фамилия'), sg.InputText(size=(50, 1))],
        [sg.Text('Имя'), sg.InputText(size=(50, 1))],
        [sg.Output(size=(30, 5))],
        [sg.Submit(button_text='OK'), sg.Cancel(button_text='CANCEL')]
        ]
    layout1 = [
        [sg.Text('Вы успешно авторизовались!')],
        [sg.Output(size=(30, 5))],
        [sg.Submit(button_text='OK')],
    ]
    window = sg.Window('Авторизация', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit', 'CANCEL'):
            break
        if event == 'OK':
            if mysql.databas(values[0], values[1]):
                break
            else:
                print('Вы ввели не верные данные')
    window.close()
    window = sg.Window(f'{values[0]}{values[1]}', layout1)
    while True:
        event, values = window.read()
        if event in (None, 'Exit', 'Выйти'):
            break
        if event == 'OK':
            print('Загрузка....')
            break
    window.close()

if __name__ == '__main__':
    avtoriz()