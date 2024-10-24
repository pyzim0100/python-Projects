
import time
from pygame import mixer
mixer.init()

def sound_1():
     mixer.music.load("sounds\\card-mixing-48088_1.mp3")
     mixer.music.play()
     time.sleep(0.5)
     
def sound_2():
     mixer.music.load("card-sounds-35956.mp3")
     mixer.music.play()
     time.sleep(0.3)
     
def sound_3():
     mixer.music.load("sounds\\flipcard-91468.mp3")
     mixer.music.play()
     time.sleep(0.2)

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
    for i, rank in enumerate(ranks):
        if rank == 10:  # Ten is the only rank with two digits
            rank_right = rank
            rank_left = rank
        elif rank == 11:  # eleven is the only rank with two digits
            rank_right = rank
            rank_left = rank
        else:
            rank_right = f"{rank} "
            rank_left = f" {rank}"
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
        for rank in ranks:
            if rank == ranks[-1]:
                print(CARDS.get(rank)[line], end="")
            else:
                print(HALF_CARDS.get(rank)[line], end="")
        print()

def blackjack_ascii(black_jack):
     CARDS = {
    1 : ("┌─────────",
         "│ ┌────   ",
         r"│ ||   \  ",
         r"│ || __/  ",
         r"│ ||   \  ",
         r"│ ||___/  ",
         "└─────────"),
    2 : ("┌────────",
         r"│ __     ",
         r"│/  \\   ",
         r"│\  ||   ",
         r"│   ||   ",
         "│  ─┘└───",
         "└────────"),
    3 : ("┌────────",
         "│    ^   ",
         r"│   / \  ",
         r"│  /   \ ",
         r"│ \ ___ /",
         r"│   /_\  ",
         "└────────"),
    4 : ("┌────────",
         "│   ____ ",
         r"│  //  \\",
         r"│ ||     ",
         r"│ ||     ",
         r"│  \\__//",
         "└────────"),
    5 : ("┌─────────┐",
         "│  || //  │",
         r"│  ||//   │",
         r"│  ||\\   │",
         r"│  || \\  │",
         r"│  ||  \\ │",
         "└─────────┘"),
    6 : ("    ┌────────",
         "    │   _____",
         r"    │     || ",
         r"    │     || ",
         r"    │ \\  || ",
         r"    │  \\__| ",
         "    └────────"),
    7 : ("┌────────",
         "│    ^   ",
         r"│   / \  ",
         r"│  /   \ ",
         r"│ \ ___ /",
         r"│   /_\  ",
         "└────────"),
    8 : ("┌────────",
         "│   ____ ",
         r"│  //  \\",
         r"│ ||     ",
         r"│ ||     ",
         r"│  \\__//",
         "└────────"),
    9 : ("┌─────────┐",
         "│  || //  │",
         r"│  ||//   │",
         r"│  ||\\   │",
         r"│  || \\  │",
         r"│  ||  \\ │",
         "└─────────┘"),
    }
     
     
     print("mixed.")
     sound_1()
     print("mixed..")
     sound_1()
     print("mixed...")
     sound_1()
     for line in range(7):
          for card in black_jack:
               print(CARDS.get(card)[line], end="")     
          print()
     
     sound_2()