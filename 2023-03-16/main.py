# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
# The Deck class should have a deal method to deal a single card from the deck.
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

import random


class DeckOfCards:
    def __init__(self) -> None:
        self.card = self.Card()

    def deck(self):
        deck = []
        for value in self.card.list_of_values:
            for suit in self.card.list_of_suits:
                deck.append(value + suit)
            # deck[value] = suit
        print(deck)

    # def randomize():
    #     i = 52
    #     random_card = random.randint(0, i)

    # def deal():
    # deck =

    class Card:
        def __init__(self) -> None:
            self.list_of_values = [
                "A of ",
                "2 of ",
                "3 of ",
                "4 of ",
                "5 of ",
                "6 of ",
                "7 of ",
                "8 of ",
                "9 of ",
                "10 of ",
                "J of ",
                "Q of ",
                "K of ",
            ]
            self.list_of_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


cards = DeckOfCards()
cards.deck()
