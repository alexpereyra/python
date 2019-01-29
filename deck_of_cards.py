#List all 52 cards in a deck

deck1 = [ ]
deck2 = [ ]
card_suits = [ "Diamonds", "Hearts", "Spades", "Clubs" ]
card_symbol = [ "Jack", "Queen", "King", "Ace" ]
card_num = [ ]
num = 1

while num <= 9:
    num = num + 1
    card_num.append(num)


for n in card_num:
    for s in card_suits:
            deck1.append(str(n) + " of " + s)
deck1 = '\n'.join(deck1)
for n in card_symbol:
    for s in card_suits:
        deck2.append(n + " of " + s)
deck2 = '\n'.join(deck2)
            
full_deck = deck1 + deck2
print("Here is a list of a full deck of cards: \n", full_deck)
