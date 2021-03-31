import PySimpleGUI as sg

def start_gui():                                                                # Deklarerar vi funktionen
    sg.ChangeLookAndFeel('Dark Blue')                                                # Tema sätts
    sg.SetOptions(text_justification='left')                                   # Texten placeras till höger
    layout = [[sg.Text('Fortnite free v-bucks', font=('Helvetica', 102))],     # layout, Vi jobbar med listor. Efter detta sätter vi font size.
             [sg.Input(key='-IN-')],                                            # 
             [sg.Button('Free:')]]

    window = sg.Window('Tillämpad programmering', layout, font=("Helvetica", 22))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Free:':
            print('Haha no noob: ')
    
    event, values = window.read()

start_gui()