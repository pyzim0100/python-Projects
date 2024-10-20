import random 
import time
import os
from cards import *

PLAYING_CARDS = [2,3,4,5,6,7,8,9,10,11]
CARDS_CATEGORIES = ['♠', '♥', '♦', '♣']

                 
def clear_terminal():
    os.system("cls")

def random_card():
    return random.choice(PLAYING_CARDS)

def random_categorie():
     return random.choice(CARDS_CATEGORIES)

def calculate_score(hand):
    if 11 in hand and sum(hand) > 21:
       hand.remove(11) 
       hand.append(1)
       
def main_menu():
    
    print ("Choose a game to start......")
    print ("\n1- Froggy \n2- Twenty one \n3- Snake \n------")
    quit() if input().lower() not in ("twenty one", "2") else clear_terminal()

    print ("Starting game .......")
    time.sleep(1)
    clear_terminal()
    blackjack_ascii(list(range(1, 10)))
    time.sleep(2)
    clear_terminal()

    run_project()

def run_project():
    computer_hand = [random_card(), random_card()]
    user_hand = [random_card(), random_card()]
    
    def final_hand():
          clear_terminal()
          print (f"\n \nYour final hand:")
          print_multiple_card(user_hand, card_categorie)
          sound_2()
          print(f"with score {sum(user_hand)}")
          print("-"*20)
          print (f"Computer final hand:")
          print_multiple_card(computer_hand, card_categorie)
          sound_2()
          print(f"with score {sum(computer_hand)}\n")

    
    
 
    while True: 
          card_categorie = random_categorie()
          calculate_score (computer_hand)
          calculate_score (user_hand)

      
          # The user points went over 21
          if sum (user_hand) > 21:
               final_hand()
               print ("You went over 21\n ** computer WIN **\n \n")
               time.sleep(3)
               break

          else:
               print (f"Your cards are:")
               print_multiple_card(user_hand, card_categorie)
               sound_2()
               print(f"current score is {sum(user_hand)}")
               print("-"*20)
               print (f"Computer's first card is:")
               print_multiple_card([0, computer_hand [0]], card_categorie)
               sound_2()
               time.sleep(3)
               if input ("\nGet another card? y/n ").lower() == "y":
                    print()
                    print("mixed.")
                    sound_1()
                    print("mixed..")
                    sound_1()
                    print("mixed...")
                    sound_1()
                    user_hand.append (random_card())
                    print_single_card(user_hand[-1], card_categorie)
                    sound_3()
                    time.sleep(2)
                    continue

               else:
                  while sum (computer_hand) <= 17:
                        if random.choice ([True , True, False]):

                           computer_hand.append (random_card())
                           calculate_score (computer_hand)

                        else:
                           break

                  # The computer points went over 21
                  if sum (computer_hand) > 21:
                     final_hand()
                     print ("Computer went over 21\n** you WIN ** \n \n")
                     time.sleep(3)
                     clear_terminal() 
                     break

                  # The computer arrived to 21 points (Blackjack)
                  elif sum (user_hand) == 21 and sum (computer_hand) < 21:
                       final_hand()
                       print ("||| BLACKJACK! |||\n** You Win ** \n \n")
                       time.sleep(3)
                       clear_terminal()
                       break 

                  # The computer arrived to 21 points (Blackjack)
                  elif sum (computer_hand) == 21 and sum (user_hand) < 21:
                       final_hand()
                       print ("||| BLACKJACK! |||\n** Computer Win **\n \n")
                       time.sleep(3)
                       clear_terminal()
                       break

                  # The computer and the user arrived to 21 points together
                  elif sum (computer_hand) == 21 and sum (user_hand) == 21:
                       final_hand()
                       print ("-- DRAW -- \n \n")
                       time.sleep(3)
                       clear_terminal()
                       break 
                        
                  # The computer has more points than the user at the end of the game
                  elif sum (computer_hand) < 21 and sum (user_hand) < 21 and sum (computer_hand) > sum (user_hand):
                       final_hand()
                       print ("** Computer WIN **\n \n")
                       time.sleep(3)
                       clear_terminal()
                       break

                  # The user has more points than the computer at the end of the game
                  elif sum (computer_hand) < 21 and sum (user_hand) < 21 and sum (user_hand) > sum (computer_hand):                  
                       final_hand()
                       print ("** You WIN **\n \n")
                       time.sleep(3)
                       clear_terminal()
                       break 

                  # The user and the computer have the same numbers of points at the end of the game
                  else:
                       final_hand()
                       print ("-- DRAW -- \n \n")
                       time.sleep(3)
                       clear_terminal()
                       break


while True:
      main_menu()