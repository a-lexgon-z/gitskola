import PySimpleGUI as sg

# Gör listor
cash = 0
transactions = []

# Lägger till en funktion för GUI:n för att skriva ut en lista på transaktioner
def balance():
    line = 0
    summa = 0
    output = ("\n\tTransactions\n"
              "\nNr. Income/Outcome. Total"
              "\n==============================")
    print(output)
    for t in transactions:
        line += 1
        summa += t
        print(f"\n{line}. {t} € {summa} €")

# Ger GUI:n ett tema, ändrar så att texten kommer från vänster håll och ger den knappar med namn (inte funktioner)
sg.ChangeLookAndFeel('black')
sg.SetOptions(text_justification='left')
layout = [[sg.Text('Bank of Zimbabwe', font=('Helvetica', 30))],
         [sg.Button('Account balance'), sg.Button('Deposit'), sg.Button('Withdraw'), sg.Button('Transactions')]]

# Skapar själva fönstret
window = sg.Window('Bank of Zimbabwe', layout)

# Ger alla "Buttons" en funktion när man trycker på dom med hjälp av if satser
# Loopar jag koden för att kunnas utföras hur många gånger man vill
while True:
    event, values = window.read()
    if event == 'Account balance':
        print(f'Your balance is: {cash}')   # Enkel kod för att bara visa hur mycket pengar man har

    # Skapar en input där man kan ta sätter in pengar och sparar informationen med append
    elif event == 'Deposit':
        deposit = float(input("Submit the amount you would like to deposit: "))
        if deposit > 0:
            cash += deposit
            transactions.append(+deposit)
        else:
            print("Please select a higher amount than 0")

    # Skapar en input där man kan ta ut pengar och sparar informationen med append
    elif event == 'Withdraw':
        withdraw = float(input("Submit the amount you would like to withdraw: "))
        if withdraw <= cash and withdraw > 0:
            cash -= withdraw
            transactions.append(-withdraw)
        elif withdraw < 0:
            print("Please select a higher amount than 0")
        else:
            print("ye")

    # Printar ut alla transaktioner
    elif event == 'Transactions':
        balance()
    elif event == sg.WIN_CLOSED:    # Avslutar loopen
        break

window.close()