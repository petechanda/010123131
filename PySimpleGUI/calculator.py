import PySimpleGUI as sg

sg.theme('Green')
#sg.theme_previewer()
layout = [ [sg.InputText(size=(23,1), font='Courier 20', justification='right', key='screen')],
            [sg.Button('AC', size=(5,1), font='Courier 20'), 
            sg.Button('+/-', size=(5,1), font='Courier 20'),
            sg.Button('%', size=(5,1), font='Courier 20'), 
            sg.Button('/', size=(5,1), font='Courier 20')],
            [sg.Button('7', size=(5,1), font='Courier 20'), 
            sg.Button('8', size=(5,1), font='Courier 20'), 
            sg.Button('9', size=(5,1), font='Courier 20'), 
            sg.Button('*', size=(5,1), font='Courier 20')],
            [sg.Button('4', size=(5,1), font='Courier 20'), 
            sg.Button('5', size=(5,1), font='Courier 20'), 
            sg.Button('6', size=(5,1), font='Courier 20'), 
            sg.Button('-', size=(5,1), font='Courier 20')],
            [sg.Button('1', size=(5,1), font='Courier 20'), 
            sg.Button('2', size=(5,1), font='Courier 20'), 
            sg.Button('3', size=(5,1), font='Courier 20'), 
            sg.Button('+', size=(5,1), font='Courier 20')],
            [sg.Button('0', size=(11,1), font='Courier 20'), 
            sg.Button('.', size=(5,1), font='Courier 20'), 
            sg.Button('=', size=(5,1), font='Courier 20')] ]

# Window('Name',layout,ระยะขอบ=(x,y))
window = sg.Window('Calculator', layout, margins=(10,10))

exp_lst = []
exp_var = ''
running = True
while running:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        running = False
    elif event in '0123456789.':
        exp_var += event
        if exp_var[len(exp_var)-2] in '+-*/':
            window['screen'].update(exp_var[len(exp_var)-1:])
        else:
            window['screen'].update(exp_var)
        #print('Enter',event)
    elif event in '+-*/':
        if exp_var[len(exp_var)-1] in '+-*/':
            exp_var = exp_var[:len(exp_var)-1]
        exp_var += event
    elif event == '%':
        if '+' not in exp_var or '-' not in exp_var or '*' not in exp_var or '/' not in exp_var:
            ans = int(exp_var)/100
            window['screen'].update(ans)
            exp_var = ''
        elif '+' in exp_var or '-' in exp_var or '*' in exp_var or '/' in exp_var:
            exp_var += event
    elif event == 'AC':
        window['screen'].update('')
        exp_var = ''
    elif event == '+/-':
        if '+' not in exp_var or '-' not in exp_var or '*' not in exp_var or '/' not in exp_var:
            ans = int(exp_var)*-1
            window['screen'].update(ans)
            exp_var = ''
        elif '+' in exp_var or '-' in exp_var or '*' in exp_var or '/' in exp_var:
            exp_var = '-({})'.format(event)
    elif event == '=':
        print(exp_var)

window.close()

