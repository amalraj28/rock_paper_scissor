import random
from game_outcome import *

# Dictionary with number key and their corresponding symbol as values
def game(user):
    elements = {
        0: 'Rock',
        2: 'Scissor',
        5: 'Paper'
    }

    # Idea is to access the values of the dictionary using values method and make them into list
    # Then using 'choice' method of random module, a random value from this list is chosen.
    # This value is then passed onto the outcome function of game_outcome module to verify the result

    random_symbol = random.choice(list(elements.values()))
    outcome(random_symbol, elements[user])
