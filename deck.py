import numpy as np
import random
import card, const

class Deck(list):
    """Represents a deck of cards"""

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        # Clean up any leftover cards
        del self[:]

        # Create deck of cards
        for rank in const.ranks:
            for suit in const.suits:
                self.append(card.Card(rank, suit))

        # Shuffle cards
        number_of_cards = len(self)
        for i in range(number_of_cards):
            rand_index = random.randint(1, number_of_cards) - 1
            # Grab top card and put it in a new random location
            self.insert(rand_index, self.pop())

    def burn(self):
        self.pop()

    def deal(self, hand):
        hand.add_card(self.pop())
