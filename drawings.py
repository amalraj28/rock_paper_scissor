def image(element):
    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """

    paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """

    scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
    if element.lower() == 'rock':
        return rock
    elif element.lower() == 'paper':
        return paper
    else:
        return scissor
