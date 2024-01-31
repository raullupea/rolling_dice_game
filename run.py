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


score1 = 0
score2 = 0



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

    input("Press ENTER to start the game!🏁\n")

    die1 = random.randint(0,5)
    die2 = random.randint(0,5)

    print(f"Player one: 🎲 {dices[die1]}\nVS\nPlayer two: 🎲 {dices[die2]} ")


    if(die1 > die2):
        print("Player one is the winner! 🔥")
        score1 = score1 + 1
        print(score1)
    elif(die2 > die1):
        print("Player two is the winner! 🔥 ")
        score2 = score2 + 1
        print(score2)
    else:
        print("It is a draw! 🟰 ")
    
    if score1 + score2 in range(1,10):
         print(f"Live score: {score1} : {score2} ")
    else:
        print(f" Total: {score1} wins vs {score2} wins ")
        break