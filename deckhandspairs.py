#!/usr/bin/python3

'''
deckhandspairs.py - a support file for the makepairs.py file.

contains a tuple with the original deck used in the game, and
lists designed to hold the current deck, discard pile, the player's hands
and pairs, and the cpu's hands and pairs.
'''

original_deck = (
    
'SA', 'HA', 'CA', 'DA',
'S2', 'H2', 'C2', 'D2',
'S3', 'H3', 'C3', 'D3',
'S4', 'H4', 'C4', 'D4',
'S5', 'H5', 'C5', 'D5',
'S6', 'H6', 'C6', 'D6',
'S7', 'H7', 'C7', 'D7',
'S8', 'H8', 'C8', 'D8',
'S9', 'H9', 'C9', 'D9',
'S10', 'H10', 'C10', 'D10',
'SJ', 'HJ', 'CJ', 'DJ',
'SQ', 'HQ', 'CQ', 'DQ',
'SK', 'HK', 'CK', 'DK'

)

#First letter is the suit.
#S is Spades, H is hearts, C is clubs, D is diamonds
#2nd letter/number is card's value.

current_deck = []

#Will hold a list copy of the original deck to be used in the game
#Good for when the player wants to play again. Instead of trying to
#fix the original deck, another copy can be made.
                        
discard_pile = []
#The discard pile is shared between both players.
#If the top card (or the last item of the list in this case)
#of the discard pile is a card a player can use,
#they can draw that card instead of one from the deck.

player_hand = []
player_pairs = []
#Stores the players hand and cards in play.

cpu_hand = []
cpu_pairs = []
#stores the cpu's hand and cards in play

if __name__ == '__main__':

    print('This file supports makepairs.py. Please launch and play that instead!')
