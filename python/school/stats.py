# from tabulate import tabulate
from random import randint
from collections import defaultdict
import copy
import os

def main_function():
    clear_terminal()

    num_rand = input_num_rand()
    num_trials = input_num_trials()
    start = input_start()
    end = input_end()

    # representation_dict = assign_representation()
    # print(representation_dict)

    # req_outcome = successful_outcome(representation_dict)
    # print(req_outcome)
    
    trials = simulation(num_trials, num_rand, start, end)
    print(trials)


def input_num_rand():
    x = input("Enter number of generated random numbers per trial: ")
    x = int(x)

    return x

def input_num_trials():
    x = input("Enter number of trials for the simulation: ")

    return x

def input_start():
    x = input("Enter starting point for rand num: ")

    return x

def input_end():
    x = input("Enter end point for rand num: ")

    return x

def assign_representation():
    num_represent_dict =  defaultdict(dict)

    loop_active = True

    while loop_active:
        rep_name = input("Enter name of representation: ")
        assigned_num = input(
            "Enter assigned num for the representation separated into commas: ")
        [int(i) for i in assigned_num.split(',')]

        num_represent_dict["Representation"][rep_name] = assigned_num

        check = input("Insert another representation? (y/n): ")

        if check == "n":
            loop_active = False

    return num_represent_dict


def trials():
    num_trials = input("Enter number of trials: ")

    return num_trials


def successful_outcome(representation_dict):
    dict_copy = copy.copy(representation_dict)

    for i in representation_dict:
        for j in representation_dict[i]:
            finished = False
            while not finished:
                required = input(f"Enter whether fulfilling the  representation: '{j}' is a successful outcome (y/n): ")
                if required == "y":
                    dict_copy["Req Outcome"][j] = True
                    finished = True
                elif required == "n":
                    dict_copy["Req Outcome"][j] = False
                    finished = True
                else:
                    print("Please enter only the letter 'y' or 'n'")
                    continue

    return dict_copy

def clear_terminal():
    x = input("Clear terminal? (y/n) ")

    if x == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
    
def simulation(num_trials, num_rand, start, end):
    num_trials = int(num_trials)
    num_rand = int(num_rand)
    start = int(start)
    end = int(end)
    
    dict = {}
    for i in range(num_trials):
        value = []
        for y in range(num_rand):
            value.append(randint(start, end))
        dict[i] = value
    return dict


# def verify_outcome(x):

main_function()

# Repeat trial 10 times rand num lib repeated using while loop with num trials as argument

# data = [[1, 'Liquid', 24, 12],
# [2, 'Virtus.pro', 19, 14],
# [3, 'PSG.LGD', 15, 19],
# [4,'Team Secret', 10, 20]]
# print(tabulate(data, headers=["Pos", "Team", "Win", "Lose"]))
