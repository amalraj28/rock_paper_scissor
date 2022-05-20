import drawings

# Dictionary showing the winning combinations as key-value pairs
def outcome(random_symbol, user):
    winning_combo = {
        'Rock': 'Scissor',
        'Paper': 'Rock',
        'Scissor': 'Paper'
    }

    print(f'\nComputer showed {random_symbol}')
    print(drawings.image(random_symbol))   # Prints the image corresponding to random value chosen earlier.

    print(f'You showed {user}')
    print(drawings.image(user))     # Prints image corresponding to user input

    value = winning_combo[random_symbol]  # Winning combination of randomly chosen element is stored in the variable "value".

    """
    The idea applied here is that only one winning combination exists for each of the 3 values.
    These winning combinations are stored as a key-value pair in dictionary.
    So compare the user inputted values with these key-value pairs and decide the winner. Here the random symbol generated is taken as key of winning_combo dictionary.
    If the random symbol and user input are same, the game is drawn. Otherwise if winning combination of random symbol and user input are same, it means the user has lost
    If the above conditions fail, then user wins
    """
    if random_symbol == user:
        print('Result: Game drawn!')
    elif value == user:
        print('Result: You lost!')
    else:
        print('Result: You won!!!')

