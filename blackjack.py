import random 


playerIN= True 
dealerIN= True

#deck of cards 

deck=[2,3,4,5,6,7,8,9,10,'A','K','Q','J',2,3,4,5,6,7,8,9,10,'A','K','Q','J',2,3,4,5,6,7,8,9,10,'A','K','Q','J',2,3,4,5,6,7,8,9,10,'A','K','Q','J']
#TOTAL 52 CARDS 

playerhand=[]
dealerhand=[]

#dealing the deck of cards 

def deal(turn):
    card= random.choice(deck)
    turn.append(card)
    deck.remove(card)


#calculate total of each


def total(hand):
    total = 0
    ace_11s = 0
    for card in hand:
        if card in range(11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total




#check for winner 
def revealdealerhand(turn):
    if len(turn)==2:
        return turn[0]
    elif len(turn)>2:
        return turn[0],turn[1]



#game loop 
for i in range(2):
    deal(dealerhand)
    deal(playerhand)

while playerIN or dealerIN:
    print("dealer has",revealdealerhand(dealerhand),"and X")
    print("you have",playerhand,"for a total of",total(playerhand))

    if playerIN:
        stayorhit=input("1:stay\n2:hit\n")
    if total(dealerhand)>16:
        dealerIN=False
    else:
        deal(dealerhand)

    if stayorhit=='1':
        playerIN=False
    else:
        deal(playerhand)


    if total(playerhand) >= 21 or total(dealerhand) >= 21:
        break

if total(playerhand) == 21:
    print(playerhand,"for a total of",total(playerhand),"BLACKJACK! YOU WIN!")

elif total(dealerhand) == 21:
    print(dealerhand,"for a total of",total(dealerhand),"BLACKJACK! DEALER WINS!")
elif total(playerhand)> 21:
    print(playerhand,"for a total of",total(playerhand),"BUST! DEALER WINS!")
elif total(dealerhand)> 21:
    print(dealerhand,"for a total of",total(dealerhand),"BUST! YOU WIN!")
elif total(dealerhand)>total(playerhand):
    print(dealerhand,"for a total of",total(dealerhand),"DEALER WINS!")
elif total(dealerhand)<total(playerhand):
    print(playerhand,"for a total of",total(playerhand),"YOU WIN!")



          

