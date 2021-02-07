# Defining a deck class
from random import shuffle
from card import Card
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}
class Deck:
    '''
    In this class I need to define creating a deck,
    as well as allowing myself to shuffle it and control
    what cards are actually in the deck.
    '''
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
