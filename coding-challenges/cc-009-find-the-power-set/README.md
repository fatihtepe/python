# Coding Challenge - 009: Find the Power Set

The purpose of this coding challenge is to write a program that finds the power set of a given set.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- analyze a problem, identify, and apply programming knowledge for appropriate solution.

- design, implement `arithmetic operators` effectively in Python to solve the given problem.

- demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

```text
List = ["a","b","C"]
Output = [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]

List = ["a","b","c","d"]
Output = [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c'], ['d'], ['a', 'd'], ['b', 'd'], ['a', 'b', 'd'], ['c', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd']]

List = ["a","b"]
Output =[['a'], ['b'], ['a', 'b']]
```

## Solution

### Coding 1

```python
def func (arr):
  power_set = []
  smalllist =[]
  for i in arr:
    smalllist = []
    smalllist.append(i)
    power_set.append(smalllist)
    
    for a in power_set:     
      tmp = a.copy()
      if i not in a:
        tmp.append(i)
        power_set.append(tmp)
  

  print(power_set)
```
