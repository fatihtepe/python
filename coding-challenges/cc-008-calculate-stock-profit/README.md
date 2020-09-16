# Coding Challenge - 008: Calculate Stock Profit

The purpose of this coding challenge is to write a program that calculates maximum profit you could get from a stock.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- analyze a problem, identify, and apply programming knowledge for appropriate solution.

- design, implement `arithmetic operators` effectively in Python to solve the given problem.

- demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

Given an array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. Note that you must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

Example of different list of stock prices and respective outputs.

```text
List = [75,73,60,100,120,130]
Output = 70
List = [10,20,23,22,17,30]
Output = 20
List = [1,6,19,59,30,60]
Output = 59
```

## Solution

### Coding 1

```python
def buy_and_sell(arr):
    max_profit = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            buy_price, sell_price = arr[i], arr[j]
            max_profit = max(max_profit, sell_price - buy_price)
    return max_profit
```

### Coding 2

```python
def buy_and_sell(arr):
    current_max, max_profit = 0, 0
    for price in reversed(arr):
        current_max = max(current_max, price)
        potential_profit = current_max - price
        max_profit = max(max_profit, potential_profit)
    return max_profit
```
