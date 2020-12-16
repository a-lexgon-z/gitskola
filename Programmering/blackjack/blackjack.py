import kortlek

def räknaPoäng(hand):
    poäng = 0
    for kort in hand:
        if kort == "J" or kort == "Q" or kort == "K":
            poäng += 10
        elif kort == "A" and poäng < 11:
            poäng += 11
        elif kort == "A" and poäng >= 11:
            poäng += 1
        else:
            poäng += kort
    return poäng

#hålla koll på handen


def skrivUtHanden(hand):
    print("Dina kort är: ", end="")
    for kort in hand:
        print(str(kort) + ", ", end="")

#checka vinnaren
def checkaVinnare(hand, dealer):
    dealerPoäng = räknaPoäng(dealer)
    spelarePoäng = räknaPoäng(hand)

    print(f"Dealerns kort är {dealer[0]} och {dealer[1]}")
    print(f"Dealerns totala hand är {dealerPoäng}")
    print(f"Din totala hand är {spelarePoäng}")

    if spelarePoäng == 21:
        print("Blackjack")
    elif spelarePoäng <= dealerPoäng or spelarePoäng > 21:
        print("Dealern vinner")
    else:
        print("Du vann")

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

    fortsätt = True

    #göra fler val (ta ett till kort eller stanna)
    while fortsätt:
        #fråga användaren om han vill ta ett kort eller stanna
        taKort = input(
            "Hit or stand? (h = hit | annan tangent = stand)")
        if taKort == "h":
            #dela ut ett kort
            hand.append(lek.pop(0))
            #skriv ut hand
            skrivUtHanden(hand)
        else:
            fortsätt = False
    
    checkaVinnare(hand, dealer)

print("Spelet är slut")
    