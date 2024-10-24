
import time
import os
from pygame import mixer

mixer.init()

CARDS_CATEGORIES = ['♠', '♥', '♦', '♣']

def clear_terminal():
    os.system("cls")

def mixed():
     print()
     print("mixed.")
     sound_1()
     print("mixed..")
     sound_1()
     print("mixed...")
     sound_1() 

def sound_1(seconds: float = 0.5):
     mixer.music.load("sounds\\card-mixing-48088_1.mp3")
     mixer.music.play()
     time.sleep(seconds)
     
def sound_2(seconds: float = 0.3):
     mixer.music.load("card-sounds-35956.mp3")
     mixer.music.play()
     time.sleep(seconds)
     
def sound_3(seconds: float = 0.2):
     mixer.music.load("sounds\\flipcard-91468.mp3")
     mixer.music.play()
     time.sleep(seconds)

def sound_4(seconds: float = 0.2):
     mixer.music.load("sounds\\card-shuffle-94662_1.mp3")
     mixer.music.play()
     time.sleep(seconds)

def print_single_card(rank, suit):
    CARDS = {
    1 : ("┌─────────┐",
         "│ 1       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       1 │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│ 2       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       2 │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│ 3       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       3 │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│ 4       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       4 │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│ 5       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       5 │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│ 6       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       6 │",
         "└─────────┘"),
    7 : ("┌─────────┐",
         "│ 7       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       7 │",
         "└─────────┘"),
    8 : ("┌─────────┐",
         "│ 8       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       8 │",
         "└─────────┘"),
    9 : ("┌─────────┐",
         "│ 9       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       9 │",
         "└─────────┘"),
    10 : ("┌─────────┐",
         "│ 10      │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│      10 │",
         "└─────────┘"),
    11 : ("┌─────────┐",
         "│ 11      │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│      11 │",
         "└─────────┘"),
    }
    
    for line in range(7):
        print(CARDS.get(rank)[line])
    print()

def print_multiple_card(ranks, suit):
    
    HALF_CARDS = {
    0 : ("┌────",
         r"│\\\\",
         r"│\\\\",
         r"│\\\\",
         r"│\\\\",
         r"│\\\\",
         "└────"),
    1 : ("┌────",
         "│ 1  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    2 : ("┌────",
         "│ 2  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    3 : ("┌────",
         "│ 3  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    4 : ("┌────",
         "│ 4  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    5 : ("┌────",
         "│ 5  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    6 : ("┌────",
         "│ 6  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    7 : ("┌────",
         "│ 7  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    8 : ("┌────",
         "│ 8  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    9 : ("┌────",
         "│ 9  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    10 : ("┌────",
         "│ 10 ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    11 : ("┌────",
         "│ 11 ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    }
    CARDS = {
    1 : ("┌─────────┐",
         "│ 1       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       1 │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│ 2       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       2 │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│ 3       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       3 │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│ 4       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       4 │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│ 5       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       5 │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│ 6       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       6 │",
         "└─────────┘"),
    7 : ("┌─────────┐",
         "│ 7       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       7 │",
         "└─────────┘"),
    8 : ("┌─────────┐",
         "│ 8       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       8 │",
         "└─────────┘"),
    9 : ("┌─────────┐",
         "│ 9       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       9 │",
         "└─────────┘"),
    10 : ("┌─────────┐",
         "│ 10      │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│      10 │",
         "└─────────┘"),
    11 : ("┌─────────┐",
         "│ 11      │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│      11 │",
         "└─────────┘"),
    
    }

    for line in range(7):
        for rank in ranks :
            if rank == ranks[-1]:
                print(CARDS.get(rank)[line], end="")
            else:
                print(HALF_CARDS.get(rank)[line], end="")
        print()

def blackjack_ascii():
     CARDS = {
    1 : ("┌─────────┐",
         "│ ┌────   │",
         r"│ ││   \  │",
         r"│ ││ __/  │",
         r"│ ││   \  │",
         r"│ ││___/  │",
         "└─────────┘"),
    2 : ("┌─────────┌─────────┐",
         "│ ┌────   │ __      │",
         r"│ ││   \  │/  \\    │",
         r"│ ││ __/  │\  ││    │",
         r"│ ││   \  │   ││    │",
         r"│ ││___/  │  ─┘└─── │",
         "└─────────└─────────┘"),
    3 : ("┌─────────┌────────┌─────────┐",
         "│ ┌────   │ __     │    ^    │",
         r"│ ││   \  │/  \\   │   / \   │",
         r"│ ││ __/  │\  ││   │  /   \  │",
         r"│ ││   \  │   ││   │ \ ___ / │",
         r"│ ││___/  │  ─┘└───│   /_\   │",
         "└─────────└────────└─────────┘"),
    4 : ("┌─────────┌────────┌────────┌─────────┐",
         "│ ┌────   │ __     │    ^   │   ____  │",
         r"│ ││   \  │/  \\   │   / \  │  //  \\ │",
         r"│ ││ __/  │\  ││   │  /   \ │ ││      │",
         r"│ ││   \  │   ││   │ \ ___ /│ ││      │",
         r"│ ││___/  │  ─┘└───│   /_\  │  \\__// │",
         "└─────────└────────└────────└─────────┘"),
    5 : ("┌─────────┌────────┌────────┌────────┌─────────┐     ",
         "│ ┌────   │ __     │    ^   │   ____ │  ││ //  │     ",
         r"│ ││   \  │/  \\   │   / \  │  //  \\│  ││//   │     ",
         r"│ ││ __/  │\  ││   │  /   \ │ ││     │  ││\\   │     ",
         r"│ ││   \  │   ││   │ \ ___ /│ ││     │  ││ \\  │     ",
         r"│ ││___/  │  ─┘└───│   /_\  │  \\__//│  ││  \\ │     ",
         "└─────────└────────└────────└────────└─────────┘     "),
    6 : ("┌─────────┌────────┌────────┌────────┌─────────┐     ┌────────┐",
         "│ ┌────   │ __     │    ^   │   ____ │  ││ //  │     │   _____│",
         r"│ ││   \  │/  \\   │   / \  │  //  \\│  ││//   │     │     ││ │",
         r"│ ││ __/  │\  ││   │  /   \ │ ││     │  ││\\   │     │     ││ │",
         r"│ ││   \  │   ││   │ \ ___ /│ ││     │  ││ \\  │     │ \\  ││ │",
         r"│ ││___/  │  ─┘└───│   /_\  │  \\__//│  ││  \\ │     │  \\__│ │",
         "└─────────└────────└────────└────────└─────────┘     └────────┘"),
    7 : ("┌─────────┌────────┌────────┌────────┌─────────┐     ┌────────┌─────────┐",
         "│ ┌────   │ __     │    ^   │   ____ │  ││ //  │     │   _____│    ^    │",
         r"│ ││   \  │/  \\   │   / \  │  //  \\│  ││//   │     │     ││ │   / \   │",
         r"│ ││ __/  │\  ││   │  /   \ │ ││     │  ││\\   │     │     ││ │  /   \  │",
         r"│ ││   \  │   ││   │ \ ___ /│ ││     │  ││ \\  │     │ \\  ││ │ \ ___ / │",
         r"│ ││___/  │  ─┘└───│   /_\  │  \\__//│  ││  \\ │     │  \\__│ │   /_\   │",
         "└─────────└────────└────────└────────└─────────┘     └────────└─────────┘"),
    8 : ("┌─────────┌────────┌────────┌────────┌─────────┐     ┌────────┌────────┌─────────┐",
         "│ ┌────   │ __     │    ^   │   ____ │  ││ //  │     │   _____│    ^   │   ____  │",
         r"│ ││   \  │/  \\   │   / \  │  //  \\│  ││//   │     │     ││ │   / \  │  //  \\ │",
         r"│ ││ __/  │\  ││   │  /   \ │ ││     │  ││\\   │     │     ││ │  /   \ │ ││      │",
         r"│ ││   \  │   ││   │ \ ___ /│ ││     │  ││ \\  │     │ \\  ││ │ \ ___ /│ ││      │",
         r"│ ││___/  │  ─┘└───│   /_\  │  \\__//│  ││  \\ │     │  \\__│ │   /_\  │  \\__// │",
         "└─────────└────────└────────└────────└─────────┘     └────────└────────└─────────┘"),
    9 : ("┌─────────┌────────┌────────┌────────┌─────────┐     ┌────────┌────────┌────────┌─────────┐",
         "│ ┌────   │ __     │    ^   │   ____ │  ││ //  │     │   _____│    ^   │   ____ │  ││ //  │",
         r"│ ││   \  │/  \\   │   / \  │  //  \\│  ││//   │     │     ││ │   / \  │  //  \\│  ││//   │",
         r"│ ││ __/  │\  ││   │  /   \ │ ││     │  ││\\   │     │     ││ │  /   \ │ ││     │  ││\\   │",
         r"│ ││   \  │   ││   │ \ ___ /│ ││     │  ││ \\  │     │ \\  ││ │ \ ___ /│ ││     │  ││ \\  │",
         r"│ ││___/  │  ─┘└───│   /_\  │  \\__//│  ││  \\ │     │  \\__│ │   /_\  │  \\__//│  ││  \\ │",
         "└─────────└────────└────────└────────└─────────┘     └────────└────────└────────└─────────┘"),
    }
     
     mixed()
     for card in list(range(1, 10)):
          clear_terminal()
          for line in range(7):
               print(CARDS[card][line])
          sound_4()
          time.sleep(0.02)
     sound_2() 
          
def print_multiple_card_on_line(ranks, suit, width):
    
    HALF_CARDS = {
    0 : ("┌────",
         r"│\\\\",
         r"│\\\\",
         r"│\\\\",
         r"│\\\\",
         r"│\\\\",
         "└────"),
    1 : ("┌────",
         "│ 1  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    2 : ("┌────",
         "│ 2  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    3 : ("┌────",
         "│ 3  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    4 : ("┌────",
         "│ 4  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    5 : ("┌────",
         "│ 5  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    6 : ("┌────",
         "│ 6  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    7 : ("┌────",
         "│ 7  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    8 : ("┌────",
         "│ 8  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    9 : ("┌────",
         "│ 9  ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    10 : ("┌────",
         "│ 10 ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    11 : ("┌────",
         "│ 11 ",
         "│    ",
         "│    ",
         "│    ",
         "│    ",
         "└────"),
    }
    CARDS = {
    1 : ("┌─────────┐",
         "│ A       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       A │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│ 2       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       2 │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│ 3       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       3 │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│ 4       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       4 │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│ 5       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       5 │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│ 6       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       6 │",
         "└─────────┘"),
    7 : ("┌─────────┐",
         "│ 7       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       7 │",
         "└─────────┘"),
    8 : ("┌─────────┐",
         "│ 8       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       8 │",
         "└─────────┘"),
    9 : ("┌─────────┐",
         "│ 9       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       9 │",
         "└─────────┘"),
    10 : ("┌─────────┐",
         "│ 10      │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│      10 │",
         "└─────────┘"),
    11 : ("┌─────────┐",
         "│ A       │",
         "│         │",
        f"│    {suit}    │",
         "│         │",
         "│       A │",
         "└─────────┘"),
    
    }

    for line in range(7):
        for rank in ranks[0] :
            if rank == ranks[0][-1]:
                print(CARDS.get(rank)[line], end="")
            else:
                print(HALF_CARDS.get(rank)[line], end="")
        for rank in ranks[1] :
            if rank == ranks[1][-1]:
                print(CARDS.get(rank)[line], end="")
            else:
                print(" "*width + HALF_CARDS.get(rank)[line], end="")
     
        print()

