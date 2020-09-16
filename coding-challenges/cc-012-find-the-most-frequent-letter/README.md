# Coding Challenge - 012: Find the Most Frequent Letter

The purpose of this coding challenge is to write a program that finds the most frequent letter in a string.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

- Implement conditional statements effectively to solve a problem.

- Implement loops to solve a problem.

- Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

Write a program that takes inputs of strings from the user (until the user enters "exit", case-insensitive), and then prints the most frequent letter (excluding "exit") and its occurrence count in these strings.

Please note that you cannot make any assumptions on the capitalization of the letters of strings, thus lowercase and uppercase of the same letters should be counted in the same occurrence.

- Example of user inputs and respective outputs.

```text
Enter a string: Elderberry
Enter a string: melon
Enter a string: peach
Enter a string: lemon
Enter a string: exit
e -> 4
```

## Solution

```python
counts = [0] * 26

check = True
while check:
  word = input("Enter a string: ")
  word = word.lower()
  if word == "exit":
    check = False
  else:
    for ch in word:
      index = ord(ch) - ord("a")
      counts[index] += 1

maxCount = max(counts)

for i in range(len(counts)):
  if counts[i] == maxCount:
    index = i
    break

maxChar = chr(ord("a") + index)
print(maxChar, "->", maxCount)
```
