#!/usr/bin/python3

'''
makepairs.py - A text-based card game played with a standard 52 card
               deck of playing cards played against the cpu. The first
               to play 3 pairs wins.
'''

import random, sys
from deckhandspairs import *

#random - used for shuffling the deck
#sys - used for helping exit
#deckhandspairs - file containing the deck, player and cpu hands and their pairs
#                 original deck is saved as a tuple, all others are lists for holding
#                 what happens in the game.

def draw_a_card(turn):

    #turn - a string that is either 'player' or 'cpu' so the game
    #knows who is drawing the card.
    
    if len(current_deck) == 0:
                
        print("Game over! No one wins!")
        main_menu()
		
        #Ends the game and returns you to the main menu if there are no cards left to draw.

    random.shuffle(current_deck)
    
    drawn_card = current_deck.pop()
		
    if turn == 'player':
            
        player_hand.append(drawn_card)

    else:

        cpu_hand.append(drawn_card)

def print_player_hand():

    C = []
    D = []
    H = []
    S = []
    #These all refer to suits. Clubs, Diamonds, Hearts, and Spades
    
    for card in player_hand:
        
        exec('{}.append(card)'.format(card[0]))
        #Checks the first letter of each card in the players hand
        #and appends them to the correct list based on that. These
        #Lists are used to display the player's hand below.
        
    all_suits = (C, D, H, S)
    #Tuple of these lists to be iterated over below.

    print('\nYour hand:')
    
    for suit in all_suits:

        if len(suit) > 0:
        
            print('{}: '.format(suit[0][0]), end = '')
        
            for card in suit:
                
                if card != suit[-1]:
                
                    print(card[1:], end = ', ')
                    
                else:
                    
                    print(card[1:])

    #What this looks like:
    #C: A, 2
    #D: 4
    #H: A
    #S: 7, 9

def set_up_game():

    for i in range(5):
        
        draw_a_card('player')
        draw_a_card('cpu')

    #Players start with 5 cards in their hands.

    discard_number = 1
    
    while True:
    
        if current_deck[-discard_number][1:] != '2':
        
           #check to make sure the top card of the discard pile isn't a 2
           #if the card is a 2, it will check the next last card instead.
        
            to_discard = current_deck.pop(-discard_number)

            discard_pile.append(to_discard)
            
            print('The first card in the discard pile is {}!\n'.format(to_discard))
            
            break
            
        else:
        
            discard_number += 1

def player_turn_switchboard():

    top_discard_num = discard_pile[-1][1:]

    possible_pairs = [card for card in player_hand if card[1:] == top_discard_num
                      and card != discard_pile[-1] and discard_pile[:1] != '2']

    #creates a list of all cards that match with the top card of the discard pile
    #Done so the player can choose which card to match with the top of the discard pile
    #in the event of multiple matches.
    
    #card != discard_pile[-1] is to prevent a bug I ran into where the game let you
    #play a pair with itself.

    #discard_pile[:1] != '2' is because you're not able to play the 

    print("The player's turn beings!")
    
    if len(possible_pairs) > 0:

        play_top_discard(possible_pairs)
        
        #If there are any matches, the player will play the top card of the discard pile
        #This won't be optional, but it is in the player's best interest to make this play.
        #This also happens before the player draws a card for the turn.

    else:

        draw_a_card('player')
        take_an_action()
        
        #Otherwise they'll go into their turn as normal.
        
    if len(player_pairs) < 3:

        end_turn()
        #Goes to the discard step if the game isn't over. The game is over when
        #a player has played 3 pairs.
            

def play_top_discard(ppairs):

    #ppairs - list - a list of cards that matches with the top card of the discard pile.

    while True:

        print_player_hand()

        print('\nThe top card of the discard pile {} pairs with a card'.format(discard_pile[-1]))
        print('in your hand! Which would you like to play with it?')

        #shows the player what the top card is

        print('\nMatches in hand: ', ppairs)

        #shows the player what they can play with that top discard pile card.

        choice = input('> ')
        
        choice = choice.upper()

        if card_checker(choice) == True and choice in ppairs:

            top_discard = discard_pile.pop()

            player_pairs.append((choice, top_discard))

            player_hand.remove(choice)

            break

        else:

            print('That is not a valid choice! Please choose another card!')
        
def take_an_action():

    #Menu for the player's turn, with all the actions they can take.

    print('You draw {} for the turn!'.format(player_hand[-1]))

    pair_played = False

    pair = ('pair', 'p')
    end = ('end', 'e')
    help_me = ('help', 'h')

    while True:

        print_player_hand()
        
        print('\nPlayer pairs in play:', player_pairs)
        print('\nCPU pairs in play: ', cpu_pairs)
        
        print('\nWhat will you do?')
        print('Type p to play a pair, e to end your turn, or h for help.')

        action = input('> ')
        
        action = action.lower()

        if action in pair:

            pair_played = play_a_pair()
            
            if pair_played == True:
                
                break

        elif action in end:
                
            break

        elif action in help_me:

            help_the_player()

        else:

            print('That is not a valid choice! Please enter another choice.')

def card_checker(card):

    #card - string - the card the player wishes to play as part of the pair.
    
    #This checks to make sure the player's choice is actually a card, is in their hand.

    if card not in original_deck or card not in player_hand:
            
        return False

    else:
            
        return True

def play_a_pair():

    back = ('B', 'BACK')
    pair_to_play = []

    while True:

        #needs to exist so if the pair ends up being invalid, the user can
        #go all the way back to the start.

        while True:

            print('Which card will you play? (type b to go back): ')
            card = input('> ')
            
            card = card.upper()

            #Upper is used to ensure the suit of the card is always upper case to match
            #how they are stored.

            if card in back:
                
                return False

            elif card_checker(card) == False:

                #card_checker makes sure the card exists, and is in the player's hand

                print('That is not a valid choice! Please enter another card')

            else:

                pair_to_play.append(card)
                
                break

        while True:
            
            print('Your first card in the pair: {}'.format(pair_to_play[0]))
            
            print('What will you play with this card?')
            card = input('> ').upper()

            if card in back:
                
                return False

            elif card_checker(card) == False:

                print('\nThat is not a valid choice! Please enter another card')

            elif card == pair_to_play[0]:

                #check for same just makes sure the player didn't enter the same card twice.

                print('\nThat is the same card you played first! Choose another card!')

            else:

                pair_to_play.append(card)

                break

        pair1 = pair_to_play[0][1:]
        pair2 = pair_to_play[1][1:]
        #[1:] is the number/face of the card

        check_for_pair = pair1 == pair2
        check_for_2 = pair1 == '2' or pair2 == '2'
        #Written as variables for more clarity
        #2's are wild so if there are any in the player's pair it is
        #considered valid no matter what the other cards are.

        if check_for_2 == True:

            player_pairs.append((pair_to_play[0], pair_to_play[1]))

            print('\nA 2 was used to make a pair!')
            print('You put {} and {} into play as a pair!'.format(pair_to_play[0], pair_to_play[1]))

            for cards in pair_to_play:

                player_hand.remove(cards)

            pair_to_play.clear()

            return True

        elif check_for_pair == False:

            print('\nSorry! That is not a pair. Please try again or type b to go back.')
            
            pair_to_play.clear()

        elif check_for_pair == True:

            player_pairs.append((pair_to_play[0], pair_to_play[1]))

            print('\nYou put {} and {} into play as a pair!'.format(pair_to_play[0], pair_to_play[1]))

            for cards in pair_to_play:

                player_hand.remove(cards)

            pair_to_play.clear()

            return True
            
def end_turn():
    
    while True:
    
        print('\nYou end your turn! Please choose a card to discard.')
    
        print_player_hand()
    
        choice = input('> ')
        
        choice = choice.upper()
        
        if card_checker(choice) == True:

            if choice[1:] == '2':

                print("Don't discard a 2! Those are wild!\n")
                #Prevents the player from discarding a wild card

            else:
            
                to_discard = choice
                
                discard_pile.append(to_discard)
                
                player_hand.remove(to_discard)

                #Moves the chosen card from the player's hand to the discard pile.
                
                print('You discard {} and end your turn!\n'.format(to_discard))
                
                break
            
        else:
            
            print('That is not a valid choice! Please enter another card.\n')
            
def help_the_player():
    
    back = ('b', 'back')

    print('\n\t\t=== HELP MENU ===')
    
    while True:
    
        print('\nWhat would you like help with?')
        print('1. Rules')
        print('2. Controls')
        print('Or enter b to go back.')
    
        choice = input('> ')
        
        if choice in back:
            
            break
            
        elif choice == '1':
            
            print('\n\t\t=== RULES ===\n')
            
            print('You and your opponent are both trying to be the first to play three pairs!')
            print('Players start with 5 cards in hand and each draw 1 card per turn.')
            print('During your turn, you can either play a pair, or pass your turn.')
            print("Look out for 2's! They're wild!")
            print('You may also play the top card of the discard pile if it pairs with one')
            print('of your cards in hand!')
            
            print('At the end of your turn you must discard a card from your hand.')
            
        elif choice == '2':
            
            print('\n\t\t=== CONTROLS ===\n')
            
            print('To play a pair, enter p or pair.')
            print('To end your turn, press e or end.')
            
            print('\nTo play a card in a pair, first type the letter of the suit,')
            print('which is C for clubs, D for diamonds, H for hearts, and S for spades,')
            print('followed by the number or letter of the card, which are J for jack,')
            print('Q for queen, K for king, and A for ace.')
            
        else:
            
            print('\nThat is not a valid choice! Please enter another choice.')

def cpu_turn():
    
    pair_played = False
    #Changing pair_played to True will prevent the CPU from playing more than one pair during its turn.
    
    print('The CPU starts its turn!')
    
    for card in cpu_hand:
    
    #This for loop checks the top card of the discard pile against the cpu's hand.
    #If it can use the top discard card, it will do that first. If it can't then it will
    #draw a card and play out the turn as normal.
        
        if card[1:] == discard_pile[-1][1:] and card[1:] != '2' and card != discard_pile[-1]:
        
            #Check for a match and also prevents the CPU from using a wild on the top card
            #of the discard pile, which is against the rules.
        
            top_discard = discard_pile.pop()
            
            print('\nThe CPU plays the top card of the discard pile!')
            print('The CPU plays {} and {} as a pair!'.format(card, top_discard))
            
            cpu_pairs.append((card, top_discard))
            
            cpu_hand.remove(card)
            
            pair_played = True
            
            break
            
    if pair_played == False:
    
        draw_a_card('cpu')
        print('\nThe CPU draws a card!')
    
        for card in cpu_hand:
                
            if pair_played == True:
            
                break
        
            for card2 in cpu_hand:
            
                if card == card2:
                
                    #Prevents a pair from being played with itself.
                
                    pass
                    
                else:
                
                    if card[1:] == card2[1:] or card2[1:] == '2':
                   
                        #checks for a pair, but also checks for wilds as well.
                                       
                        cpu_pairs.append((card, card2))
                        
                        cpu_hand.remove(card)
                        cpu_hand.remove(card2)
                        
                        pair_played = True

                        print('\nThe CPU plays {} and {} as a pair!'.format(card, card2))
                        
                        break

    #regardless of how a pair was made, discards always happen.

    if len(cpu_pairs) < 3:

        #passes this if the game is going to be over. The CPU will have 0 cards in hand
        #and won't be able to discard.
    
        discard_number = -1
        
        while True:
        
            if cpu_hand[discard_number][1:] != '2':

               #check to make sure the CPU doesn't discard a wild card by mistake
               #if the card is a 2, it will check the next last card instead.
            
                to_discard = cpu_hand[discard_number]
                
                discard_pile.append(to_discard)
                
                cpu_hand.remove(to_discard)
                
                print('\nThe CPU discards {} and ends its turn!\n'.format(to_discard))
                
                break
                
            else:
            
                discard_number -= 1

def turn_order():

    goes_first = random.randint(1, 2)

    #rolls for first. A 1 is the player going first, a 2 is the cpu

    if goes_first == 1:

        print('The player goes first!\n')

        player_turn_switchboard()

    else:

        print('The CPU goes first!\n')

    while True:

        cpu_turn()

        results = win_check()

        #win_check returns a tuple, ('winning player' and True/False) if the 2nd element
        #is True, the game will have a winner. The winning player is then passed back to
        #the main menu to display the winner and let the player start the game again.

        if results == True:

            return
        
        player_turn_switchboard()

        results = win_check()

        if results == True:

            return
        

def win_check():

    if len(player_pairs) == 3:

        #3 pairs are needed to win the game

        print('\n\t\tPLAYER WINS! CONGRATULATIONS!\n')

        return True

    elif len(cpu_pairs) == 3:

        print('\n\t\tCPU WINS! BETTER LUCK NEXT TIME!\n')

        return True

    else:

        return False

def main_menu():

    start = ('s', 'start')
    rules = ('r', 'rules')
    exit_game = ('q', 'quit')

    while True:

        print('\t\t=== MAKE PAIRS ===')
        print('\nYou can START, see the RULES, or QUIT')

        choice = input('> ')

        choice = choice.lower()

        if choice in start:

            print('\nStarting game!\n')

            #Resets the deck so the game works on multiple plays
            
            set_up_game()
            
            turn_order()

        elif choice in rules:

            help_the_player()

        elif choice in exit_game:

            print('Thanks for playing! See you soon!')
            
            sys.exit(0)

        else:

            print('That is not a valid choice! Please choose something else!')


if __name__ == '__main__':

    current_deck = list(original_deck[:])

    random.shuffle(current_deck)

    main_menu()
