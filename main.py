from game_mechanism import *      # To access function in game_mechanism module created by me.

print('Welcome to the Rock Paper Scissors Game!!')
user = 'dummy'      # variable to store user input

while True:
    try:
        user = int(input('Type 0 for Rock, 2 for Scissors, 5 for Paper: '))
    except ValueError:
        print('Invalid entry!! Try again')
        continue
    else:
        if user not in [0, 2, 5]:   # the user entered value can only be 0 or 2 or 5. If other values are given, it's invalid
            print('Value not in range! Try again!!')
            continue
        break

game(user)  
