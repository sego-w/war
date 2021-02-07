from card import Card

class Player:
    '''
    being able to have a 'hand' of cards
    + dealing cards
    + adding cards to ur hand
    '''
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