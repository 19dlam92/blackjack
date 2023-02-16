import random
from cards import Card

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
            { 'rank' : 'A', 'value' : 11 },
            { 'rank' : 'K', 'value' : 10 },
            { 'rank' : 'Q', 'value' : 10 },
            { 'rank' : 'J', 'value' : 10 },
            { 'rank' : '10', 'value' : 10 },
            { 'rank' : '9', 'value' : 9 },
            { 'rank' : '8', 'value' : 8 },
            { 'rank' : '7', 'value' : 7 },
            { 'rank' : '6', 'value' : 6 },
            { 'rank' : '5', 'value' : 5 },
            { 'rank' : '4', 'value' : 4 },
            { 'rank' : '3', 'value' : 3 },
            { 'rank' : '2', 'value' : 2 }
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for i in range(number):
            card = self.cards.pop()
            cards_dealt.append(card)
            return cards_dealt
        


        # for suit in suits:
        #     for rank in ranks:
        #         self.cards.append(Card[suit, rank])

    # def shuffle(self):
    #     if len(self.cards) > 1:
    #         random.shuffle(self.cards)

    # def deal(self, number):
    #     cards_dealt = []
    #     for i in range(number):
    #         if len(self.cards) > 0:
    #             card = self.cards.pop()
    #             cards_dealt.append(card)
    #         return cards_dealt

deck1 = Deck()
print(deck1.cards)