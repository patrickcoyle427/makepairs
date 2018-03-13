discard_pile = ['C100']

cpu_hand = ['C6', 'D6', 'C9', 'C2']

cpu_pairs = []

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
    
        #draw_a_card('cpu')
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
    
        discard_number = -1

        #rint(cpu_hand)

        #print(cpu_hand[discard_number][])

        print(cpu_hand[discard_number][:1] == '2')
        
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

cpu_turn()
