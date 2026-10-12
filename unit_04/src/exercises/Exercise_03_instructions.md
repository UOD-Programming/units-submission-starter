# Exercise 4.3

***
# === TASK ===
Write a program that asks the user to enter a series of non-zero integers, one at a time. 

The program should keep asking the user for a number until they enter a value of ``0``. 

The program should then display the largest of the numbers that have been entered. 

Be aware that the user could enter all negative integers and your program has to be able to handle this. 

For example if the user enters ``3,10,32,-1`` the required output of the program is:

```
This program calculates the largest number from a series of numbers entered.
Please enter a number. Enter 0 to stop
3
Please enter a number. Enter 0 to stop
10
Please enter a number. Enter 0 to stop
32
Please enter a number. Enter 0 to stop
-1
Please enter a number. Enter 0 to stop
0
The largest of the numbers entered is 32
```

If the user enters ``0``:
```
This program calculates the largest number from a series of numbers entered.
Please enter a number. Enter 0 to stop
0
No numbers entered.
```
***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***