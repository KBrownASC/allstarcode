from random import*
from time import*

#DECK CODE
Cards = []
Suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
Royal = ["J", "Q", "K" , "A" ]
Deck = []

for i in range(2,11):
    Cards.append(str(i))
    

for j in range(len(Royal)):
    Cards.append(str(Royal[j]))
    
    
    
for o in range(4):
    for l in range(13):
        card = (Cards[l] + " of " + Suits[o])
        Deck.append(card)
    



random.shuffle(Deck)

for m in range(52):
    print(Deck[m])


#DECK CODE