import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *
from collections import Counter
import functools

# Part 1
class Game:
    dict_hand_value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T' : 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    dict_hand_value_p2 = {'A': 13, 'K': 12, 'Q': 11, 'T' : 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

    def __init__(self, hands, bets):
        self.hands = hands
        self.bets = bets
        self.part = 1

    def __repr__(self):
        return f'Game({self.hands}, {self.bets})'

    def hand_value(self, hand):
        c = Counter(hand).values()
        # five of a kind
        if len(set(hand)) == 1:
            return 6
        # four of a kind
        elif 4 in c:
            return 5
        # full house
        elif 3 in c and 2 in c:
            return 4
        # three of a kind
        elif 3 in c:
            return 3
        # two pairs
        elif 2 in c and len(c) == 3:
            return 2
        # one pair
        elif len(set(hand)) == 4:
            return 1
        # high card
        else:
            return 0
        
    def hand_value_p2(self, hand : str):
        if 'J' in hand:
            nb_j = hand.count('J')
            hand = hand.replace('J', '')
            c = Counter(hand).values()
            # five of a kind (eg. 'JJJJJ', 'JJJJ2', 'JJJ22', 'JJ222', 'J2222')
            if nb_j > 3 or (nb_j == 3 and  2 in c) or (nb_j == 2 and 3 in c) or (nb_j == 1 and 4 in c):
                return 6
            # four of a kind (eg. 'JJJ23', 'JJ223', 'J2223')
            elif nb_j == 3 or (nb_j == 2 and 2 in c) or (nb_j == 1 and 3 in c):
                return 5
            # full house (eg. 'J2323')
            elif nb_j == 1 and list(c).count(2) == 2:
                return 4
            # three of a kind (eg. 'JJ234', 'J2234')
            elif nb_j == 2 or (nb_j == 1 and 2 in c):
                return 3
            # two pairs will never be made because we will prefer four of a kind
            # one pair (eg. 'J2345')
            elif nb_j == 1:
                return 1
        else:
            return self.hand_value(hand)
    
    def compare_hands(self, hand1, hand2):
        if self.part == 1:
            value1 = self.hand_value(hand1)
            value2 = self.hand_value(hand2)
        else:
            value1 = self.hand_value_p2(hand1)
            value2 = self.hand_value_p2(hand2)
        if value1 > value2:
            return 1
        elif value1 < value2:
            return -1
        else:
            if self.part == 1:
                for i in range(len(hand1)):
                    if self.dict_hand_value[hand1[i]] > self.dict_hand_value[hand2[i]]:
                        return 1
                    elif self.dict_hand_value[hand1[i]] < self.dict_hand_value[hand2[i]]:
                        return -1
            else:
                for i in range(len(hand1)):
                    if self.dict_hand_value_p2[hand1[i]] > self.dict_hand_value_p2[hand2[i]]:
                        return 1
                    elif self.dict_hand_value_p2[hand1[i]] < self.dict_hand_value_p2[hand2[i]]:
                        return -1
        return 0

    def order_hands(self):
        self.hands = sorted(self.hands, key=functools.cmp_to_key(self.compare_hands))

    def calculate_winnings(self):
        self.order_hands()
        winnings = 0
        for i, hand in enumerate(self.hands):
            winnings += self.bets[hand] * (i + 1)
        return winnings

lines = read_input(current,Choice.REAL).read().split('\n')
hands = []
bets = {}
for line in lines:
    hand, bet = line.split()
    hands.append(hand)
    bets[hand] = int(bet)

game = Game(hands, bets)
print(game.calculate_winnings())

# Part 2
game.part = 2
print(game.calculate_winnings())