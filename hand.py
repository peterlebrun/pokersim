import numpy as np
import numpy.matlib
import card

class Hand(list):
    """Represents a player's hand"""

    def __init__(self):
        self.matrix = numpy.matlib.zeros((13, 4))

    def add_card(self, card):
        self.append(card)
        self.matrix += card.matrix

    def get_best_hand(self, community_cards):
        self.extend(community_cards)
        self.matrix += community_cards.matrix

        #rank_summary = self.matrix * np.ones([4, 1])
        #suit_summary = self.matrix.getT() * np.ones([13, 1])

        #print(rank_summary)
        #print(suit_summary)

        print(self.matrix[:][0])
        print(self.matrix[0, :].sum())
        print("")
        print(self.matrix[1, :])
        print(self.matrix[1, :].sum())
        print("")
        print(self.matrix[2, :])
        print(self.matrix[2, :].sum())
        print("")
        print(self.matrix[3, :])
        print(self.matrix[3, :].sum())
        print("")

        # check for a royal flush

        # check for a straight flush

        # check for four of a kind

        # check for a full house

        # check for a flush

        # check for a straight

        # check for three of a kind

        # check for two pairs

        # check for one pair

        # check for a high card

