"""This is the code file for the basic operation portion of HW2."""


# Part a
def prisoners_dilemma()->int:
    """
    This function simulates the game Prisoners' Dilemma where it asks for
    strategies of both player A and B. If they have different responses,
    the game continues. Otherwise the game ends and this function returns
    the number of rounds played.
    """
    num_games = 0
    different_choice = True
    while different_choice:
        a_strategy = input("Player A, what is your strategy, cooperate or defect? ")
        b_strategy = input("Player B, what is your strategy, cooperate or defect? ")
        if a_strategy == "cooperate" and b_strategy == "defect":
            print("A: -20, B: 0")
            num_games += 1
        elif a_strategy == "defect" and b_strategy == "cooperate":
            print("A: 0, B: -20")
            num_games += 1
        elif a_strategy == "cooperate" and b_strategy == "cooperate":
            print("A: -3, B: -3")
            num_games += 1
            different_choice = False
        elif a_strategy == "defect" and b_strategy == "defect":
            print("A: -10, B: -10")
            num_games += 1
            different_choice = False
        else:
            print("invalid input!")
            prisoners_dilemma()
    return num_games


# Part b
def factorial(n_arg: int)->int:
    """
    This function returns n! for any positive integer n.
    """
    if n_arg == 1:
        return n_arg
    return n_arg * factorial(n_arg-1)


# Part c
def compute_frequency(words: [str])->dict:
    """
    This function takes a list of strings and returns a dictionary
    of how many times each unique string has appeared.
    """
    dictionary = {}
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary
