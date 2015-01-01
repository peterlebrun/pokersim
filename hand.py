import numpy as np
import numpy.matlib
import card

class Hand:
    """Represents a player's hand"""

    def __init__(self):
        self.cards = []
        self.matrix = numpy.matlib.zeros((13, 4))

    def add_card(self, card):
        self.cards.append(card)
        self.matrix += card.matrix
