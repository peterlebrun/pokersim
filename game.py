import hand, deck

class Game(object):
    """Represents the whole table"""

    def __init__(self, number_of_players = 10):
        self.community_cards = hand.Hand()
        self.deck = deck.Deck()

        self.players = []
        for i in range(number_of_players):
            self.players.append(hand.Hand())

        self.test_it()

    def deal_initial(self):
        self.deck.shuffle()

        for i in range(2):
            for player in self.players:
                self.deck.deal(player)

    def deal_flop(self):
        self.deck.burn()
        for i in range(3):
            self.deck.deal(self.community_cards)

    def deal_turn(self):
        self.deck.burn()
        self.deck.deal(self.community_cards)

    def deal_river(self):
        self.deck.burn()
        self.deck.deal(self.community_cards)

    def start(self):
        self.deal_initial()
        self.deal_flop()
        self.deal_turn()
        self.deal_river()
        #print(self.community_cards.matrix)

    def test_it(self):
        self.start()
        x = self.community_cards
        self.players[0].get_best_hand(x)
        #self.players[1].get_best_hand(x)
        #self.players[2].get_best_hand(x)
        #self.players[3].get_best_hand(x)
        #self.players[4].get_best_hand(x)
        #self.players[5].get_best_hand(x)
