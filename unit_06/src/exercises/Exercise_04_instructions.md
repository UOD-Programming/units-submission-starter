# Exercise 6.4  

Write a program that will calculate the change to be given by a drink dispensing machine. 

All items cost less than one pound and one pound (100p) is the highest value that can be inserted into the machine. 

The program must ask the user for the cost of the item and the amount inserted (in pence). 

The amount inserted must not be more than 100 and the cost of the item must not be more than than the amount inserted.

The coins that can be given in change are 50p, 20p, 10p, 5p, 2p and 1p. Your program must use the minimum amount of coins to produce the change. 

For example, if the user enters 100 for the amount given and 42 for the cost of the item, the program will display (because the change is 58p):
```
Please enter the amount inserted (1 to 100):
100
Please enter the cost of the item:
42
Number of 50p coins is 1
Number of 20p coins is 0
Number of 10p coins is 0
Number of 5p coins is 1
Number of 2p coins is 1
Number of 1p coins is 1
```
Here are some additional examples.
```
Please enter the amount inserted (1 to 100):
66
Please enter the cost of the item:
33
Number of 50p coins is 0
Number of 20p coins is 1
Number of 10p coins is 1
Number of 5p coins is 0
Number of 2p coins is 1
Number of 1p coins is 1
```

```
Please enter the amount inserted (1 to 100):
75
Please enter the cost of the item:
80
Item costs more than amount inserted
```

```
Please enter the amount inserted (1 to 100):
105
Invalid amount
```

```
Please enter the amount inserted (1 to 100):
-10
Invalid amount
```

Note:

- Do not have to worry about other input that isn't a number for this exercise.
- If the above examples work as written then you will pass the test.
- You should not loop around for valid input either.

**Hint 1.** Using integer division will really help in this program. I would think about it on paper first.

**Hint 2** Use a function to calculate the change and get it to return a list containing the number for each coin.

**Hint 3.** Try to get the program working without worrying about invalid input or maximum amounts. Then add these in.

Copy and paste the following into ``Exercise_04.py`` to get started.

```python
def main():
    pass

if __name__ == "__main__":
    main()
```

## Additional

**The following is not tested, but is a good exercise for you to attempt. I suggest you do it in a new Python file so as to not affect your existing code.**

Try using a list to hold the values of the coins, so that you can write a general purpose change calculator that can be used for any coinage simply by changing the contents of the list (you might want to use a variable of type char to hold the coinage (‘p’ for UK, ‘c’ for US, etc)).

For example, once you have it working with UK coins (50, 20, 10, 5, 2, 1), try changing the contents of the list so that it contains the US coin values (25, 10, 5 and 1). Changing the contents of the list and the contents of the char variable that contains the name of the currency in use should be the only change you need to make to your program.