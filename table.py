import hand, deck

class Game:
    """Represents the whole table"""

    def __init__(self, number_of_players):
        self.community_cards = hand.Hand()
        self.deck = deck.Deck()

        self.players = []
        for i in range(number_of_players):
            self.players.append[hand.Hand()]

    def deal():
        self.deck.shuffle()

        for player self.players:
            deck.deal(player)

    def flop(self, deck):
        deck.burn()
        for i in range(3):
            deck.deal(self.community_cards)

    def turn(self, deck):
        deck.burn()
        deck.deal(self.community_cards)

    def river(self, deck):
        deck.burn()
        deck.deal(self.community_cards)
