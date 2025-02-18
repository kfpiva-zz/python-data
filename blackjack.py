import random

suits = ('Ouros', 'Copas', 'Espadas', 'Paus')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    '''
    recebe qual é a carta - naipe e valor
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)

class Deck():
    '''
    Define o deck = uma carta para cada
    '''
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        return "lista de cartas %s" %(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.card.append(card)
        self.value += values[card.rank]

        if card.rank = "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10

class Chips:

    def __init__(self, total=100):
        self.total =  total #
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How much money do you will start bet? (just numbers)'))
        except:
            print("This was not a number")
            continue
        else:
            if chips.bet > chips.total:
                print(f'Sorry, dont have enough chips, you have {chips.total}')
            else:
            break

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand,playing):

    while True:
        x = input('Hit or Stand - select H or S')
        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands, dealer's turn")
            playing = False

        else:
            print("Didn't understand, Please enter just h or s only")
            continue

        break

    return playing
