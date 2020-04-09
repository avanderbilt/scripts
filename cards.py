# coding=utf-8
import pydealer
from colorama import init

init()

from colorama import Fore, Back, Style

cardPrefix = 1271

codes  = {}
codes['spades'] =   [37,38,39,40,41,42,43,44,45,46,47,48,49]
codes['hearts'] =   [53,54,55,56,57,58,59,60,61,62,63,64,65]
codes['diamonds'] = [69,70,71,72,73,74,75,76,77,78,79,80,81]
codes['clubs'] =     [85,86,87,88,89,90,92,92,93,94,95,96,97]

suitColors = {
    'Spades' : Fore.BLACK,
    'Clubs' : Fore.BLACK,
    'Hearts' : Fore.RED,
    'Diamonds' : Fore.RED
}

deck = pydealer.Deck()
toRemove = [ 'King', 'Queen', 'Jack']
deck.cards = [card for card in deck.cards if card.value not in toRemove]

deck.shuffle()

hand = deck.deal(3)

for card in hand.cards:
    value = 0;
    if card.value == 'Ace':
        value = 0
    else:
        value = int(card.value) - 1

    code = '{}{}'.format(cardPrefix, codes[card.suit.lower()][value-1])

    message = '%s%s%s %s'
    print(message % (Back.WHITE + suitColors[card.suit], unichr(int(code)).encode('utf-8'), Back.RESET + Fore.RESET, card.name))
