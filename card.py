import numpy as np
import const

class Card(object):
    """Represents a single card"""

    def __init__(self, rank, suit):
        self.rank   = rank
        self.suit   = suit
        self.matrix = const.ranks[rank] * const.suits[suit]
