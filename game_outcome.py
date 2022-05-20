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

    key = winning_combo[random_symbol]  # Winning combination of randomly chosen element is stored in the variable "key".

    """
    The idea applied here is that only one winning combination exists for each of the 3 values.
    These winning combinations are stored as a key-value pair in dictionary.
    So compare the user inputted values with these key-value pairs and decide the winner.
    """
    if random_symbol == user:
        print('Result: Game drawn!')
    elif key == user:
        print('Result: You lost!')
    else:
        print('Result: You won!!!')

