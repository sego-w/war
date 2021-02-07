# The individual cards
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}
class Card:
    '''
    Creating cards with suit/rank pairs
    '''
    def __init__(self,suitarg,rankarg):
        self.rank = rankarg
        self.suit = suitarg
        self.value = values[rankarg]
    if __name__ == '__main__':
        def __str__(self):
            return f"The card is a(n) {self.rank} of {self.suit}"

