# Coding Challenge - 002 : Convert Milliseconds into Hours, Minutes, and Seconds

Purpose of the this coding challenge is to write program that converts the given milliseconds into hours, minutes, and seconds.

## Learning Outcomes

At the end of the this coding challenge, students will be able to;

- analyze a problem, identify and apply programming knowledge for appropriate solution.

- design, implement `while` loops effectively in Python to solve the given problem.

- control loops effectively by using `if` and `control` statements.

- apply arithmetic operations on basic data types in Python.

- demonstrate their knowledge of string manipulations and formatting in Python.

- demonstrate their knowledge of algorithmic design principles by using function effectively.

   
## Problem Statement

- Write program that converts the given milliseconds into hours, minutes, and seconds. The program should convert only from milliseconds to hours/minutes/seconds, not vice versa and during the conversion following notes should be taken into consideration.

   - If the calculated time of hours is 0, it should not be shown in the output.

   - If the calculated time of minutes is 0, it should not be shown in the output.

   - If the calculated time of seconds is 0, it should not be shown in the output.

   - If the milliseconds is greater than 1000, remainder milliseconds should not be shown in the output.

   - If milliseconds given is less than 1000, only milliseconds should be shown in the output.

   - Output should always be string in the format shown in the examples.

- Program should ask user for the input, after giving information text show as below.

```text
###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) :  
```

- User input can be either integer or string, thus the input should be checked for the followings,

   - The input should be a decimal number greater then zero.
   
   - If the input is less then 1, user should be warned and asked for input again.

   - If the input is string and can not be converted to decimal number, user should be warned and asked for input again.

- Program should run until the user types `exit` in case insensitive manner.
   
- Example for user inputs and respective outputs

```
Input             Output
(milliseconds)    (Calculated Time) 
--------------    -----------------
555               just 555 millisecond/s
2001              2 second/s
60011             1 minute/s
122011            2 minute/s 2 second/s
3661011           1 hour/s 1 minute/s 1 second/s
7200011           2 hour/s
7322011           2 hour/s 2 minute/s 2 second/s
-8                "Not Valid Input !!!"
Ten               "Not Valid Input !!!"
Exit              "Exiting the program... Good Bye"
```

## Solution

```python
# write a function that converts the given milliseconds into hours, minutes, and seconds
def convert(milliseconds):
    # one hour in milliseconds
    hour_in_milliseconds = 60*60*1000
    # calculate the hours within given milliseconds
    hours = milliseconds // hour_in_milliseconds
    # calculate milliseconds left over when hours subtracted
    milliseconds_left = milliseconds % hour_in_milliseconds
    # one minute in milliseconds
    minutes_in_milliseconds = 60*1000
    # calculate the minutes within remainder milliseconds
    minutes = milliseconds_left // minutes_in_milliseconds
    # calculate milliseconds left over when minutes subtracted
    milliseconds_left %= minutes_in_milliseconds
    # calculate the seconds within remainder milliseconds
    seconds = milliseconds_left // 1000
    # format the output string
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)
    

# flag to show warning to the user, default is False.
is_invalid = False

# start endless loop to get user input continuously
while True:
    # info text to be shown to the user
    info = """
###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) : """

    # get the user input after showing info text.
    # if is_invalid set to True then show additional warning to the user
    # pass the input the alphanum variable after stripping white space characters
    alphanum = input('\nNot Valid Input !!!\n'*is_invalid + info).strip()
    # if the input is not decimal number
    if not alphanum.isdecimal():
        # then check, if it is the "exit" keyword
        if alphanum.lower() == 'exit':
            # if it is "exit", then say goodbye and terminate the program
            print('\nExiting the program... Good Bye')
            break
        # if it is a string other than "exit"
        else:
            # then set to invalid flag to True to show warning and continue with next cycle
            is_invalid = True
            continue
    # convert the given string to the integer
    millisecs = int(alphanum)
    # if the milliseconds is greater than 0
    if 0 < millisecs:
        # then convert milliseconds and print out the user
        print(
            f'\nMilliseconds of "{alphanum}"" is equal to {convert(millisecs)}')
        # and set invalid flag to the False, it might be set the True in previous cycle
        is_invalid = False
    # if the millisecond is out of bounds
    else:
        # then set to invalid flag to True to show warning
        is_invalid = True
```
