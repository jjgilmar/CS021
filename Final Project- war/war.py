"""
Joey Gilmartin
CS021
War: The Card Game
Final Project
"""

import random

def shuffle(deck_):
    random.shuffle(deck_)
    return deck_


def deal(deck_, computer_deck_, player_deck_):
    for i, card in enumerate(deck_):
        if i % 2 == 0:
            computer_deck_.append(card)
        elif i % 2 == 1:
            player_deck_.append(card)
    return deck_

def play_a_round(computer_deck_, player_deck_):
    computer_card = computer_deck_.pop(0)
    player_card = player_deck_.pop(0)
    
    print(f'\nComputer Card: {computer_card}\n')
    print(f'Player Card: {player_card}\n')
    
    if computer_card > player_card:
        print('Computer has won this round!\n\n\n')
        computer_deck_.append(computer_card)
        computer_deck_.append(player_card)
        
    elif player_card > computer_card:
        print('You won this round!\n\n\n')
        player_deck_.append(computer_card)
        player_deck_.append(player_card)
        
    elif player_card == computer_card:
        try:
            computer_card_2 = computer_deck_.pop(0)
            computer_card_3 = computer_deck_.pop(0)
            computer_card_4 = computer_deck_.pop(0)
            computer_card_5 = computer_deck_.pop(0)
            
            player_card_2 = player_deck_.pop(0)
            player_card_3 = player_deck_.pop(0)
            player_card_4 = player_deck_.pop(0)
            player_card_5 = player_deck_.pop(0)
            
            print("Time for war!\n")
            
            print(f"Computer War Cards: {computer_card_2}, {computer_card_3},"
            f" {computer_card_4}\n")
            print(f"Player War Cards: {player_card_2}, {player_card_3},"
                  f" {player_card_4}\n")
            print(f"Computer Final Card: {computer_card_5}\n")
            print(f"Player Final Card: {player_card_5}\n")
            
            if computer_card_5 > player_card_5:
                print('Computer has won this round!\n\n\n')
                computer_deck_.append(computer_card)
                computer_deck_.append(computer_card_2)
                computer_deck_.append(computer_card_3)
                computer_deck_.append(computer_card_4)
                computer_deck_.append(computer_card_5)

                computer_deck_.append(player_card)
                computer_deck_.append(player_card_2)
                computer_deck_.append(player_card_3)
                computer_deck_.append(player_card_4)
                computer_deck_.append(player_card_5)
            
            
        
            elif player_card_5 > computer_card_5:
                print('You won this round!\n\n\n')
                player_deck_.append(computer_card)
                player_deck_.append(computer_card_2)
                player_deck_.append(computer_card_3)
                player_deck_.append(computer_card_4)
                player_deck_.append(computer_card_5)
                
                player_deck_.append(player_card)
                player_deck_.append(player_card_2)
                player_deck_.append(player_card_3)
                player_deck_.append(player_card_4)
                player_deck_.append(player_card_5)
            
            elif player_card_5 == computer_card_5:
                player_deck_.append(player_card_5)
                player_deck_.append(player_card_4)
                player_deck_.append(player_card)
                player_deck_.append(player_card_3)
                player_deck_.append(player_card_2)
                
                computer_deck_.append(computer_card_5)
                computer_deck_.append(computer_card_4)
                computer_deck_.append(computer_card)
                computer_deck_.append(computer_card_3)
                computer_deck_.append(computer_card_2)
                
        except IndexError:
            
            if len(computer_deck_) < 4:
                print("Computer does not have enough cards for war.\n")
                for i in computer_deck_:
                    computer_deck_.pop(i)
                
            elif len(player_deck_) < 4:
                print("You do not have enough cards for war.\n")
                for i in player_deck_:
                    player_deck_.pop(i)
        
if __name__ == '__main__':
    
    deck = [14, 14, 14, 14, 13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11,
         10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6,
         5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]
    
    computer_deck = []
    
    player_deck = []
    
    round_counter = 0
    
    shuffle(deck)
    
    deal(deck, computer_deck, player_deck)

    print('Welcome to War: The Card Game!\n')
    print('Rules:\n'
          'You and the computer will both flip a card at the same time. The higher card'
          ' wins both cards.\n'
          'In the event of a tie, you and the computer will both flip 4 additional '
          'cards, and the 4th card will decide the round.\n'
          'For simplicity of the game, face cards are not used, but their '
          'number equivalent is:\n'
          'A = 14, K = 13, Q = 11, J = 10\n')
    
    while True:
            
        play = input("Would you like to continue? Yes: 'y'   Quit: 'q' : ")
        
        if play.lower() == 'y':
            round_counter += 1
            print(f"\n\n\nROUND {round_counter}")
                
            if round_counter % 100 == 0:
                shuffle(computer_deck)
                shuffle(player_deck)
                
            play_a_round(computer_deck, player_deck)
                
#             print(computer_deck)
#             print(player_deck)
            
            if len(player_deck) == 0:
                print("COMPUTER WINS THE GAME!")
                print(f"The game took {round_counter} rounds!")
                break
        
            if len(computer_deck) == 0:
                print("YOU WIN THE GAME!")
                print(f"The game took {round_counter} rounds!")
                break
                
        elif play.lower() == 'q':
            exit()
