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

        # aces   = self.matrix[ 0, :]
        # twos   = self.matrix[ 1, :]
        # threes = self.matrix[ 2, :]
        # fours  = self.matrix[ 3, :]
        # fives  = self.matrix[ 4, :]
        # sixes  = self.matrix[ 5, :]
        # sevens = self.matrix[ 6, :]
        # eights = self.matrix[ 7, :]
        # nines  = self.matrix[ 8, :]
        # tens   = self.matrix[ 9, :]
        # jacks  = self.matrix[10, :]
        # queens = self.matrix[11, :]
        # kings  = self.matrix[12, :]

        number_of_aces   = self.matrix[ 0, :].sum()
        number_of_twos   = self.matrix[ 1, :].sum()
        number_of_threes = self.matrix[ 2, :].sum()
        number_of_fours  = self.matrix[ 3, :].sum()
        number_of_fives  = self.matrix[ 4, :].sum()
        number_of_sixes  = self.matrix[ 5, :].sum()
        number_of_sevens = self.matrix[ 6, :].sum()
        number_of_eights = self.matrix[ 7, :].sum()
        number_of_nines  = self.matrix[ 8, :].sum()
        number_of_tens   = self.matrix[ 9, :].sum()
        number_of_jacks  = self.matrix[10, :].sum()
        number_of_queens = self.matrix[11, :].sum()
        number_of_kings  = self.matrix[12, :].sum()

        has_aces   = number_of_aces   > 0
        has_twos   = number_of_twos   > 0
        has_threes = number_of_threes > 0
        has_fours  = number_of_fours  > 0
        has_fives  = number_of_fives  > 0
        has_sixes  = number_of_sixes  > 0
        has_sevens = number_of_sevens > 0
        has_eights = number_of_eights > 0
        has_nines  = number_of_nines  > 0
        has_tens   = number_of_tens   > 0
        has_jacks  = number_of_jacks  > 0
        has_queens = number_of_queens > 0
        has_kings  = number_of_kings  > 0

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

        # check for flush
        # has_flush
        # check for straight
        # has_straight
        # if flush and straight, check for straight flush/royal flush
        # has_straight_flush
        # check for pair
        # has_pair
        # has_two_pair
        # has_three_of_a_kind
        # has_four_of_a_kind
        # has_full_house
        # if pair, check for two pair, full house, four of a kind
        # if not flush/straight/pair, just check for high card
