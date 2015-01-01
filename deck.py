import numpy as np
import random
import card, const

class Deck:
    """Represents a deck of cards"""

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        # Start by creating a deck of cards, then shuffling
        self.cards = []

        for rank in const.ranks:
            for suit in const.suits:
                self.cards.append(card.Card(rank, suit))

        for i in range(len(self.cards)):
            rand_index = random.randint(1, len(self.cards)) - 1
            # Grab top card and put it in a new random location
            self.cards.insert(rand_index, self.get_next_card())

    def get_next_card(self):
        return self.cards.pop(0)

    def burn(self):
        self.get_one_card()

    def deal(self, hand):
        hand.add_card(self.get_one_card)
