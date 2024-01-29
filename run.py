import random

# We are going to utilize Unicode characters for building the dice structure

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")

 #● ┌ ─ ┐ │ └ ┘ 
 
print("Welcome to my roll dice game! 🎲 🎲 ")
print("Rules are as follows: there are two players each using one dice 🎲")
print("Winner is the player who gets the higher dice. 🎲 ")
print("In case of a draw they need to throw the dice again until one of them gets the higher number! ")
print("In order to play use the 'ENTER' key.  ")
print("I wish you good luck!! ☘️☘️☘️ \n")


dices = [ ''' 

    ┌─────────┐
    │         │
    │    ●    │
    │         │
    └─────────┘ ''' , '''


    ┌─────────┐
    │      ●  │
    │         │
    │  ●      │
    └─────────┘ ''' , '''


    ┌─────────┐
    │       ● │
    │    ●    │
    │ ●       │
    └─────────┘ ''' , '''


    ┌─────────┐
    │ ●     ● │
    │         │
    │ ●     ● │
    └─────────┘ ''' , '''




    ┌─────────┐
    │ ●     ● │
    │    ●    │
    │ ●     ● │
    └─────────┘ ''' , '''


    ┌─────────┐
    │ ●     ● │
    │ ●     ● │
    │ ●     ● │
    └─────────┘ ''' 
                        ]

while True:

    input("Press ENTER to start the game!🏁 ")

    die1 = random.randint(0,5)
    die2 = random.randint(0,5)

    print(f"Player one: 🎲 {dices[die1]}\nVS\nPlayer two: 🎲 {dices[die2]} ")

    if(die1 > die2):
        print("Player one is the winner! 🔥")
    elif(die2 > die1):
        print("Player two is the winner! 🔥 ")
    else:
        print("It is a draw! 🟰 ")
    