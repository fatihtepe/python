# Coding Challenge - 014: Check Consecutive Vowels

The purpose of this coding challenge is to write a program that checks if a word contains consecutive vowels or not.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

- Implement conditional statements effectively to solve a problem.

- Implement loops to solve a problem.

- Execute operations on strings.

- Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

In this coding challenge, you are going to write a program that takes a string and checks if it contains consecutive vowels or not. It should give `Positive` as an output if it contains consecutive vowels and `Negative` otherwise. For example `saetqi` string contains `a` adjacent to `e`, which means that it contains consecutive vowels. So it should give `Positive` as an output. On the other hand, if you take the string of `statoqag`, the output should be `Negative`.

- Expected Output:

```text
Please enter a string: gasdph
Negative

Please enter a string: aiou
Positive

Please enter a string: taoum
Positive

Please enter a string: a
Negative
```

## Solution

```python
word = input("Please enter a string: ")
word = word.lower()

vowels = ["a", "e", "i", "o", "u"]
exist = False

for i in range(len(word)-1):
  if word[i] in vowels:
    if word[i+1] in vowels:
      exist = True
      break

if exist:
  print("Positive")
else:
  print("Negative")
```

## Computational Thinking

### Abstraction

To be able to solve this problem using a programing language, you have to go as abstract as possible on the term `2 consecutive vowels`. First of all, vowels mean `"a","e","i","o","u"`. That being noted, consecutive means "next to each other", which means "the difference between the indexes is 1". So: ***You should check if the string contains 2 items from the given list whose positions differ by 1***.

### Algorithm Design

We are going to use the pattern that we have recognized to design the algorithm. So the algorithm should be as follows:

- Step 1: From the beginning of the string, pick a value one by one.

- Step 2: Check ***if*** the value, and the adjacent value are both in the list of vowels. If the answer is `Yes` then print `positive`, if the answer is `No` then continue to next step.

- Step 3: Move to `Step 1` to pick the next value.
