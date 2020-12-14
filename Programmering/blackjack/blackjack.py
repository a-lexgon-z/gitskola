import kortlek

#behöver räkna ut värden på korten


#hålla koll på handen

#Skriv handen
def skrivUtHanden(hand):
    print("Dina kort är: ", end="")
    for kort in hand:
        print(str(kort) + ", ", end="")

#checka vinnaren


#spel-loop
while True:
    spela = input("Blackjack? (j för ja, annan tangent för nej: ")

    if spela != "j":
        break

    lek = kortlek.skapaKortlek()

    print(lek)
    #dealer tar två kort
    dealer = [lek.pop(0), lek.pop(0)]
    print(f"Dealerns första kort är {dealer[0]}")

    hand = [lek.pop(0), lek.pop(0)]
    print(f"Dina första två kort är: {hand[0]} och {hand[1]}")


#göra fler val (ta ett till kort eller stanna)
fortsätt = True

while fortsätt:
    #fråga användaren om han vill ta ett kort eller stanna
    taKort = input(
        "Hit or stand? (h = hit | annan tangent = stand)")
    if taKort != "h":
        #dela ut ett kort
        hand.append(lek.pop(0))
        #skriv ut hand
        skrivUtHanden(hand)
    else:
        forsätt = False
    