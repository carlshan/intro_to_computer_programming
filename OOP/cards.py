class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit)


card = Card(rank="1", suit='hearts')

print(card)


class Deck(object):
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self):
        self.cards = []

        for suit in Deck.suit_names:
            for rank in Deck.rank_names:
                card = Card(suit=suit, rank=rank)
                self.cards.append(card)

    def __str__(self):
        result = []
        for card in self.cards:
            result.append(str(card))
        return '\n'.join(result)

deck = Deck()
print(deck)
