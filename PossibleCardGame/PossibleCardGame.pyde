from random import*
from time import*


def setup():
    background(255)
    size(100,200)


def draw():
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
        
    
    
    shuffle(Deck)
    
    '''for m in range(52):
        print(Deck[m])'''
    
    
    #DECK CODE
    
    
    print(Deck[i])
    
    def makeCard():
        fill(40,200,180)
        rect(0,0,99,199)
        fill(1)
        textSize(15)
        text(Deck[i],8,100)
    
    
    if keyPressed and key == ' ':
        sleep(.09)
        makeCard()
        sleep(.2)
    
    