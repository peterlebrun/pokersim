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

        number_of_clubs    = self.matrix[: 0,].sum()
        number_of_diamonds = self.matrix[: 1,].sum()
        number_of_hearts   = self.matrix[: 2,].sum()
        number_of_spades   = self.matrix[: 3,].sum()

        has_flush = max([number_of_clubs, number_of_diamonds, number_of_hearts, number_of_spades]) >= 5

        number_of_aces   = int(self.matrix[ 0, :].sum())
        number_of_twos   = int(self.matrix[ 1, :].sum())
        number_of_threes = int(self.matrix[ 2, :].sum())
        number_of_fours  = int(self.matrix[ 3, :].sum())
        number_of_fives  = int(self.matrix[ 4, :].sum())
        number_of_sixes  = int(self.matrix[ 5, :].sum())
        number_of_sevens = int(self.matrix[ 6, :].sum())
        number_of_eights = int(self.matrix[ 7, :].sum())
        number_of_nines  = int(self.matrix[ 8, :].sum())
        number_of_tens   = int(self.matrix[ 9, :].sum())
        number_of_jacks  = int(self.matrix[10, :].sum())
        number_of_queens = int(self.matrix[11, :].sum())
        number_of_kings  = int(self.matrix[12, :].sum())

        my_str_2 = str(number_of_aces)   + \
                   str(number_of_twos)   + \
                   str(number_of_threes) + \
                   str(number_of_fours)  + \
                   str(number_of_fives)  + \
                   str(number_of_sixes)  + \
                   str(number_of_sevens) + \
                   str(number_of_eights) + \
                   str(number_of_nines)  + \
                   str(number_of_tens)   + \
                   str(number_of_jacks)  + \
                   str(number_of_queens) + \
                   str(number_of_kings)

        has_pair            = my_str_2.find('2') #>= 0
        has_two_pair        = has_pair and my_str_2.find('2', my_str_2.find('2') + 1) #>= 0
        has_three_of_a_kind = my_str_2.find('3') >= 0
        has_full_house      = has_pair and has_three_of_a_kind
        has_four_of_a_kind  = my_str_2.find('4') >= 0

        has_aces   = int(number_of_aces   > 0)
        has_twos   = int(number_of_twos   > 0)
        has_threes = int(number_of_threes > 0)
        has_fours  = int(number_of_fours  > 0)
        has_fives  = int(number_of_fives  > 0)
        has_sixes  = int(number_of_sixes  > 0)
        has_sevens = int(number_of_sevens > 0)
        has_eights = int(number_of_eights > 0)
        has_nines  = int(number_of_nines  > 0)
        has_tens   = int(number_of_tens   > 0)
        has_jacks  = int(number_of_jacks  > 0)
        has_queens = int(number_of_queens > 0)
        has_kings  = int(number_of_kings  > 0)

        my_str = str(has_aces)   + str(has_twos)   + str(has_threes) + \
                 str(has_fours)  + str(has_fives)  + str(has_sixes)  + \
                 str(has_sevens) + str(has_eights) + str(has_nines)  + \
                 str(has_tens)   + str(has_jacks)  + str(has_queens) + \
                 str(has_kings)  + str(has_aces)

        has_straight = my_str.find('11111') >= 0

        print(self.matrix)
        print(my_str_2)
        print(my_str)
        print("has_pair: "            + str(has_pair))
        print("has_two_pair: "        + str(has_two_pair))
        print("has_three_of_a_kind: " + str(has_three_of_a_kind))
        print("has_full_house: "      + str(has_full_house))
        print("has_four_of_a_kind: "  + str(has_four_of_a_kind))
        print("has_flush: "           + str(has_flush))
        print("has_straight: "        + str(has_straight))

        # if pair, check for two pair, full house, four of a kind
        # if not flush/straight/pair, just check for high card
