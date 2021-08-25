transactions = []
filename = "transactions.txt"

def balance():
    balance = 0 
    for t in transactions:
        balance += t
    return balance

def print_transactions():
    line = 0
    summa = 0
    output = ("\n\tTransactions\n"
              "\n{:>3} {:>12} {:>12}"
              "\n==============================").format("Nr", "Händelse", "Balance")
    for t in transactions:
        line += 1
        summa += t
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format(line, t, summa))
    return output

def validate_int(output, error_mess):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

def check_file_exists():
    try:
        with open(filename, "x"):
            print("File's been created")

        with open(filename, "a") as f:
            f.write("{}\n".format(500))
    except:
        return

def read_file():
    check_file_exists()

    with open(filename) as f:
        for row in f:
            if len(row) > 0:
                add_transaction(int(row))
            
def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

def write_transaction_to_file(transaction):
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))

read_file()

while True:
    menu = (f"\n======================================"
            "\n\tBank of Zimbabwe"
            "\n======================================"
            "\n1. Account balance"
            "\n2. Deposit"
            "\n3. Withdraw"
            "\n0. Exit program"
            "\n======================================"
            "\nNavigate with 0-3\n").format(balance())

    choice = validate_int(menu, "Pogchamp but that's wrong.")

    if choice == 0:
        break

    elif choice == 1:
        print(print_transactions())

    elif choice == 2:
        depositin = int(input("Enter amount to deposit:\n\n"))
        if depositin > 0:
            add_transaction(depositin, True)
        else:
            print("Please enter a number with higher value than 0.")

    elif choice == 3:
        withdrawut = int(input("Enter amount to withdraw:\n\n"))
        if withdrawut <= balance() and withdrawut >= 0:
            add_transaction(-withdrawut, True)
        elif withdrawut < 0:
            print("Please enter a number with higher value than 0.")
        else:
            print("You can't withdraw more than you have in your account.")

    else:
        print("Please select a number between 0-3.")

print("\nThank you for using the Bank of Zimbabwe")