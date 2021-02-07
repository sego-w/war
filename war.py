# Control flow? 
# Initialising the game

# Defining a deck class
from random import shuffle
from card import Card
from deck import Deck
from player import Player
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}

p1 = Player("user 1")
p2 = Player("user 2")
new_deck = Deck()
new_deck.shuffl()
# deck_cards = new_deck.list_of_cards
for i in range(26):
    p1.add_cards(new_deck.deal())
    p2.add_cards(new_deck.deal())
x=0
y=0
game = True
p1_cards = []
p2_cards = []
while game:
    if len(p1.hand) >= 52 or len(p2.hand) >= 52:
        print("One of the players has too many cards!")
        game = False
        break
    if len(p1.hand) == 0:
        print("Player one ran out of cards!")
        game = False
        winner = "2"
        break
    if len(p2.hand) == 0:
        print("Player two ran out of cards!")
        game = False
        winner = "1"
        break
    try:
        
        p1_cards.append(p1.deal_cards())
        p2_cards.append(p2.deal_cards())
        printwar = True
        comparing = True
        while comparing:
           
            x+=1
            if p1_cards[-1].value > p2_cards[-1].value:
                print("p1 won a comparison!")
                p1.add_cards(p1_cards[0])
                p1.add_cards(p2_cards[0])
                comparing = False
                
            elif p1_cards[-1].value < p2_cards[-1].value:
                print("p2 won a comparison!")
                p2.add_cards(p1_cards[0])
                p2.add_cards(p2_cards[0])
                comparing = False
            
            else:
                if printwar:
                    print("A war has begun!")
                    printwar = False
                if len(p1.hand) <= 1:
                    print("p1 doesn't have enough cards!!")
                    comparing = False
                    game = False
                    winner = "2"
                    break
                elif len(p2.hand) <= 1:
                    print("p2 doesn't have enough cards!!")
                    comparing = False
                    game = False
                    winner = "2"
                    break
                else:
                    y+=1
                    p1_cards.append(p1.deal_cards())
                    p2_cards.append(p2.deal_cards())
                    

    except IndexError:
        print("Whoops! Out of cards!")
        if len(p1.hand) > len(p2.hand):
            print("player one won by having more cards!")
            print(len(p1.hand))
            print(len(p2.hand))
            winner = "1"
        else:
            print("player two won by having more cards!")
            print(len(p1.hand))
            print(len(p2.hand))
            winner = "2"
        game = False
        break

print(f"The winner was Player {winner}, with a game lasting {x} rounds!")
print(f"Player one had {len(p1.hand)} cards and Player two had {len(p2.hand)} cards")
print(f"{y} Wars were held in total")



# SOME REDUNTANT CODE
'''
if p1_cards[-1].value < p2_cards[-1].value:
    print("p2 won the war!")
    p2.add_cards(p1_cards[y:-1])
    p2.add_cards(p2_cards[y:-1])
    print(p2.hand)
    comparing = False
    winner = "2"
    break
    elif p1_cards[-1].value > p2_cards[-1].value:
    print("p1 won the war!")
    p1.add_cards(p1_cards[y:-1])
    p1.add_cards(p2_cards[y:-1])
    print(p1.hand)
    comparing = False
    winner = "1"
    break
'''

# Originally my classes were in the same file

'''
class Card:
    
    Creating cards with suit/rank pairs
    
    def __init__(self,suitarg,rankarg):
        self.rank = rankarg
        self.suit = suitarg
        self.value = values[rankarg]
    if __name__ == '__main__':
        def __str__(self):
            return f"The card is a(n) {self.rank} of {self.suit}"
class Deck:
    
    In this class I need to define creating a deck,
    as well as allowing myself to shuffle it and control
    what cards are actually in the deck.
    
    def __init__(self):
        self.list_of_cards = []
        for suitarg in suits:
            for rankarg in ranks:
                self.list_of_cards.append(Card(suitarg,rankarg))
    def shuffl(self):
        shuffle(self.list_of_cards)
    def deal(self):
        pop_card = self.list_of_cards.pop(0)
        return pop_card

   # def __str__(self):
   #    return f'The last card is {self.rank} of {self.suit}'
class Player:
    
    being able to have a 'hand' of cards
    + dealing cards
    + adding cards to ur hand
    
    def __init__(self,which_one):
        self.user = which_one
        self.hand = []
    def add_cards(self,cards):
        if isinstance(cards,list):
            self.hand.extend(cards)
        elif isinstance(cards,Card):
            self.hand.append(cards)
        else:
            self.hand.append("Uh-oh, something went wrong...")
            print(type(cards))
    def deal_cards(self):
        pop_card = self.hand.pop(0)
        return pop_card
'''