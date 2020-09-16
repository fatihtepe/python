# Coding Challenge - 011: Create a "Rock, Paper, Scissors" Game

The purpose of this coding challenge is to write a program that plays the "Rock, Paper, Scissors" game with the user.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

- Implement conditional statements effectively to solve a problem.

- Implement lists and iterate through them with loops.

- Apply practical utilization of random numbers.

- Design functions to decompose a problem into smaller and simpler problems.

- Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

`Rock, Paper, Scissors` is a worldwide-popular game that is usually played by children. It has the following simple rules:

Either player chooses one of rock, paper, and scissors at the same time.

A certain object beats another object. Those combinations are as follows:

- Rock beats scissors.
- Paper beats rock.
- Scissors beat paper.
- If both users choose the same object, it is a tie.

In this coding challenge, you are going to make a game of `rock, paper, scissors` that is going to be played against the computer. The game will last until either the computer or user wins 3 times in total. At the end of the game, your program will display the scores and the winner. Throughout the game, the user will choose their weapon with an input (The input should be one of rock, paper, and scissors, otherwise the request for input should be repeated) and the computer will choose its weapon randomly.

- Example of user inputs and respective outputs.

```text
Please enter your weapon: rock
tie - no one wins

Please enter your weapon: paper
scissors beats paper - computer wins

Please enter your weapon: rock
rock beats scissors - user wins

Please enter your weapon: scissors
rock beats scissors - computer wins

Please enter your weapon: rock
paper beats rock - computer wins

User won 1 time(s) and computer won 3 time(s)
Computer has won the game!
```

## Solution

```python

from random import *

#A function to compare the weapons to decide the winner of that round.
def compareWeapons(comp_w, user_w, weapons, winning_weapons):
    if comp_w == user_w:
        print("tie - no one wins")
        return 0
    else:
        # find the index of comp_w
        for idx_comp in range(len(weapons)):
            if weapons[idx_comp] == comp_w:
                break
        # find the index of user_w
        for idx_user in range(len(weapons)):
            if winning_weapons[idx_user] == user_w:
                break
        # if those indices are the same --> user wins
        if idx_comp == idx_user:
            print(user_w, "beats", comp_w, "- user wins")
            return 1
        else:
            print(comp_w, "beats", user_w, "- computer wins")
            return 2

# main part

#Two lists, first one is the regular list to choose the weapon from and the second one is to make the comparison in order to decide on the winner.
weapons = ["rock", "paper", "scissors"]
winning_weapons = ["paper", "scissors", "rock"]

#Scores
user_count = 0
comp_count = 0

#So-called, "Game loop"
while user_count != 3 and comp_count != 3:
    #Choose the weapon of computer randomly.
    comp_w = weapons[randint(0,2)]
    #Users chooses a weapon until a valid input is entered.
    user_w = input("Please enter your weapon: ")
    while user_w not in weapons:
        user_w = input("Please enter your weapon: ")

    # 0: tie, 1: user, 2: comp
    winner = compareWeapons(comp_w, user_w, weapons, winning_weapons)
    if winner == 1:
        user_count += 1
    elif winner == 2:
        comp_count += 1

# The last score is printed after the game is over i.e one of the players has reached 3 in terms of score.
print("User won", user_count, "time(s) and computer won", comp_count, "time(s)")

#Winner is decided by comparing the last scores of either side.
if user_count == 3:
    print("User has won the game!")
else:
    print("Computer has won the game!")
```
