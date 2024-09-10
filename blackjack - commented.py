import random 

# Game status flags
playerIN = True  # Player is still in the game (i.e., hasn't chosen to stay or busted)
dealerIN = True  # Dealer is still in the game (i.e., must keep drawing cards if hand total < 17)

# Deck of cards: a list containing all the cards in a deck (four suits of each value)
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J']
# TOTAL: 52 CARDS in a deck

# Player's and Dealer's hands: lists to store the cards dealt to each
playerhand = []
dealerhand = []

# Function to deal a card to the specified hand (player or dealer)
def deal(turn):
    card = random.choice(deck)  # Randomly select a card from the deck
    turn.append(card)           # Add the card to the hand (turn refers to playerhand or dealerhand)
    deck.remove(card)           # Remove the dealt card from the deck to avoid duplication

# Function to calculate the total value of the cards in a hand
def total(hand):
    total = 0         # Initialize the hand's total value
    ace_11s = 0       # Keep track of how many Aces are being counted as 11
    
    for card in hand:
        # If the card is an integer (between 2 and 10), add it directly to the total
        if card in range(11):
            total += card
        # Face cards (J, Q, K) are worth 10 points
        elif card in ['J', 'K', 'Q']:
            total += 10
        # Aces ('A') are initially worth 11 points
        else:
            total += 11
            ace_11s += 1  # Track that an Ace is being counted as 11
    
    # If total exceeds 21 and there are Aces counted as 11, reduce them to 1
    while ace_11s and total > 21:
        total -= 10   # Reduce the total by 10 for each Ace reduced from 11 to 1
        ace_11s -= 1  # Decrease the number of Aces being counted as 11

    return total  # Return the final total of the hand

# Function to reveal the dealer's hand
# If the dealer has two cards, only reveal the first one (second one remains hidden)
def revealdealerhand(turn):
    if len(turn) == 2:
        return turn[0]  # Return only the first card in dealer's hand
    elif len(turn) > 2:
        return turn[0], turn[1]  # Return the first two cards if dealer has more than two

# Game loop starts here
# Deal two cards to both the dealer and the player at the start
for i in range(2):
    deal(dealerhand)  # Deal two cards to the dealer
    deal(playerhand)  # Deal two cards to the player

# Main game loop: continues while the player or dealer is still playing
while playerIN or dealerIN:
    # Show the dealer's visible card and hide the other
    print("dealer has", revealdealerhand(dealerhand), "and X")
    # Show the player's hand and total value
    print("you have", playerhand, "for a total of", total(playerhand))

    # Player's turn: Decide whether to stay or hit
    if playerIN:
        stayorhit = input("1:stay\n2:hit\n")  # Get player's choice
    # Dealer's turn: Dealer must hit if their total is 16 or lower
    if total(dealerhand) > 16:
        dealerIN = False  # Dealer stays if their total is above 16
    else:
        deal(dealerhand)  # Dealer hits if their total is 16 or below

    # If the player chooses to stay, they are out of the game
    if stayorhit == '1':
        playerIN = False  # Player chooses to stay (no more cards)
    else:
        deal(playerhand)  # Player chooses to hit (draw another card)

    # End game loop if either player's or dealer's total reaches or exceeds 21
    if total(playerhand) >= 21 or total(dealerhand) >= 21:
        break  # Game ends if either hand hits or exceeds 21

# After exiting the game loop, check for the winner
if total(playerhand) == 21:
    print(playerhand, "for a total of", total(playerhand), "BLACKJACK! YOU WIN!")
elif total(dealerhand) == 21:
    print(dealerhand, "for a total of", total(dealerhand), "BLACKJACK! DEALER WINS!")
elif total(playerhand) > 21:
    print(playerhand, "for a total of", total(playerhand), "BUST! DEALER WINS!")
elif total(dealerhand) > 21:
    print(dealerhand, "for a total of", total(dealerhand), "BUST! YOU WIN!")
elif total(dealerhand) > total(playerhand):
    print(dealerhand, "for a total of", total(dealerhand), "DEALER WINS!")
elif total(dealerhand) < total(playerhand):
    print(playerhand, "for a total of", total(playerhand), "YOU WIN!")
