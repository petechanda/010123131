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

exp_var = ''
symb = ''
num = []
running = True
while running:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        running = False
    elif event in '0123456789.':
        exp_var += event
        window['screen'].update(exp_var)
        #print('Enter',event)
    elif event == '+':
        num.append(float(exp_var))
        if symb == '+':
            ans = num[0]+num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '-':
            ans = num[0]-num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '*':
            ans = num[0]*num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '/':
            ans = num[0]/num[1]
            num = [ans]
            window['screen'].update(ans)
        symb = '+'
        exp_var = ''
    elif event == '-':
        num.append(float(exp_var))
        if symb == '+':
            ans = num[0]+num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '-':
            ans = num[0]-num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '*':
            ans = num[0]*num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '/':
            ans = num[0]/num[1]
            num = [ans]
            window['screen'].update(ans)
        symb = '-'
        exp_var = ''
    elif event == '*':
        num.append(float(exp_var))
        if symb == '+':
            ans = num[0]+num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '-':
            ans = num[0]-num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '*':
            ans = num[0]*num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '/':
            ans = num[0]/num[1]
            num = [ans]
            window['screen'].update(ans)
        symb = '*'
        exp_var = ''
    elif event == '/':
        num.append(float(exp_var))
        if symb == '+':
            ans = num[0]+num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '-':
            ans = num[0]-num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '*':
            ans = num[0]*num[1]
            num = [ans]
            window['screen'].update(ans)
        elif symb == '/':
            ans = num[0]/num[1]
            num = [ans]
            window['screen'].update(ans)
        symb = '/'
        exp_var = ''
    elif event == '%':
        if symb == '':
            ans = float(exp_var)/100
            window['screen'].update(ans)
            exp_var = str(ans)
        else:
            num.append(float(exp_var))
            if symb == '+':
                ans = num[0]+(num[1]*num[0]/100)
            elif symb == '-':
                ans = num[0]-(num[1]*num[0]/100)
            elif symb == '*':
                ans = num[0]*num[1]/100
            elif symb == '/':
                ans = num[0]*100/num[1]
            window['screen'].update(ans)
            exp_var = str(ans)
            num = []
            symb = ''
    elif event == 'AC':
        window['screen'].update('')
        exp_var = ''
        num = []
        symb = ''
    elif event == '+/-':
        exp_var = float(exp_var)*-1
        window['screen'].update(exp_var)
        exp_var = str(exp_var)
    elif event == '=':
        num.append(float(exp_var))
        if symb == '+':
            ans = num[0]+num[1]
        elif symb == '-':
            ans = num[0]-num[1]
        elif symb == '*':
            ans = num[0]*num[1]
        elif symb == '/':
            ans = num[0]/num[1]    
        window['screen'].update(ans)
        exp_var = str(ans)
        num = []
        symb = ''

window.close()
