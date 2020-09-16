# Coding Challenge - 013: Find the Non-Repeated Values

The purpose of this coding challenge is to write a program that finds the non-repeated (appears only once) values in a list.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

- Implement conditional statements effectively to solve a problem.

- Implement loops to solve a problem.

- Iterate through a list to gather data.

- Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

A book store is trying to find the books that are only left 1 in the stock. They have the book list and they ask you to find the books. You are going to write a computer program that finds the non-repeated values in the list. Also indicate how you have used **computational thinking concepts** to find the solution.

Sample list for the test runs is as follows:

```python
products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]
```

- Expected Output:

```text
To Kill a Mockingbird
In Cold Blood
Wide Sargasso Sea
I Capture The Castle
```

## Solution

```python
products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby", "One Hundred Years of Solitude", \
            "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea", \
            "One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World", \
            "I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby", \
            "One Hundred Years of Solitude", "Pride and Prejudice"]
for product_1 in products:
  count = 0
  for product_2 in products:
    if product_1 == product_2:
      count += 1
      if count > 1:
        break
  if count == 1:
    print(product_1)
```

## Computational Thinking

### Abstraction

Most of the information that is given in the question is useless. We don't need to know that it is a book store, that they give as a job to solve their issue and we are working through a list of books. ***All we need to know is that we are trying to find non-repeated values in a list***. We don't care whether the values are books, movies, animals or numbers.

### Pattern Recognition

To be able to check if a value is repeated in the list, we should pick one of the values and check if the identical value exists in the list. And to be able to find out all the non-repeated values, we should repeat this process for every value. So the pattern is: ***One by one, check for every book if it exists in the list again***.

### Algorithm Design

We are going to use the pattern that we have recognized to design the algorithm. So the algorithm should be as follows:

- Step 1: From the beginning of the list, pick a value.

- Step 2: Compare the value that you have picked with every value from the beginning of the list.

- Step 3: **If** you encounter a value that is the same with the value that you have picked in the beginning more than once, skip that value. Go back to `Step 1`.

- Step 4: **If** encountered a value only once, save or print the value that you have picked since it is non repeated. Go back to `Step 1`.

- Step 5: Print the list that you have saved throughout the iteration.
