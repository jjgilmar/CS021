Joey Gilmartin
README.txt for war.py


My final project is the card game war. My code gives the user a simple, yet effective interface in the python shell that displays the current round, the user's card, the computer's card, and who won the round. In the event of war, it also displays the four additional cards put down by both the player and the computer. In the rare event of a tie on the last card of war, the program ignores the second tie and puts the cards from the round back into the respective player's deck in a different order to prevent it from happening again. Lastly, every 100 rounds, the program shuffles both the player's deck and the computer's deck to prevent any infinite games. If either the player or the computer runs out of cards, the other wins, and the code prints who won the game, followed by the number of rounds the game took.

At the beginning of the game, it displays the rules as followed: 
"You and the computer will both flip a card at the same time. The higher card wins both cards.
In the event of a tie, you and the computer will both flip 4 additional cards, and the 4th card will decide the round.
For simplicity of the game, face cards are not used, but their number equivalent is:
A = 14, K = 13, Q = 11, J = 10"

The program replicates different human actions by using functions. For example, the shuffle function uses the random.shuffle operator to shuffle the list. The deal function splits the shuffled deck of cards and deals it to both the player and the computer. The play-a-round function contains everything that could possibly happen in a round. It pops a card from the start of the player's cards, compares them, and appends the cards from the round to the deck of the person who won the round.


With my program, there are multiple ways of playing and testing. The program will be submitted as if it is being used for a game, in which case, after each round it will ask the user to continue by pressing 'y' or to quit by pressing 'q'. However, if lines 144-146 and lines 167-168 are removed or commented out, the program will run a whole simulation of the game by printing out each turn, but without asking for user input for each round. This would be helpful in the case of wondering how long a game would take. Additionally, to see what the program is doing each turn lines 154-155 can be uncommented to see the change in players' cards. This would be used to make sure the program is actually working. 
