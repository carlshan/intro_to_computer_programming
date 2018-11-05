import random

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
            # Since str(card) will invoke the __str__() function of the card class
            # it will append things like "Ace of Spades"
            result.append(str(card))

        # Just invoking the __str__() function of `lists`
        return str(result)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        # Returns the top card and removes it
        # Last card in the deck

        return self.cards.pop()

    def add_card(self, card):
        # Adds a card to the top of the deck
        self.cards.append(card)

card_points = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

deck = Deck()

### Making the game blackjack

deck.shuffle()

def sum_points(cards):
    points = 0
    for card in cards:
        points += card_points[card.rank]
    return points

play_game = True

def play_turn():
    card1 = deck.draw_card()
    card2 = deck.draw_card()
    print("Your cards are: ", card1, " and ", card2)
    choice = input("Do you want to hit or stay? ")
    if choice == 'hit':
        card3 = deck.draw_card()
        print("You drew " + str(card3))

        total_points = sum_points([card1, card2, card3])
    else:
        total_points = sum_points([card1, card2])

    return total_points

while play_game:
    print("Player 1, it is your turn: ")
    player1 = play_turn()
    print("Player 2, it is your turn: ")
    player2 = play_turn()
    if player1 > 21 and player2 > 21:
        print("Everyone went bust. No one wins")

    elif player1 > 21:
        print("Player 1, you went bust!")

    elif player2 > 21:
        print("Player 2, you went bust! You lose.")

    elif player1 > player2:
        print("Player 1 wins with a total of ", player1, " points compared to ", player2)

    else:
        print("Player 2 wins with a total of ", player2, " points compared to ", player1)

    choice = input("Do you want to play again? y/n ")

    if choice == 'n':
        play_game = False
