# Exercise 5.1  

You will find the following code in ``Exercise_01.py``. NOTE: You will have to update the function signature for ``calc_retail_price``.
```python
def calc_retail_price():
    # remove the following line and write your function here
    pass

def main():
    # remove the following line and write your main program here
    pass

# This is needed for the tests. This is now the first bit of code Python will run.
# Please ask if you are curious, but it is enough to understand that this calls the main() function and runs whatever code you have in there.
if __name__ == "__main__":
    main() # calls the main function
    
    # uncomment the following lines to test calc_retail_price when you run the program.You will need to comment out main()
    # print(calc_retail_price(3.00, 100)) # should print 6.0
    # calc_retail_price(5.00, 50) # should print 7.5
```
Write a program that asks the user to enter an item’s wholesale cost and its markup percentage. It should then display the retail price for the item. For example:
* If the wholesale cost is £3.00 and the markup percentage is 100%, the retail price will be £6.00 and the program should run as follows:

```
Please enter a wholesale cost:
3.00
Please enter a markup percentage:
100
The retail price is £6.00.
```
* If the wholesale cost is £5.00 and the markup percentage is 50%, the retail price will be £7.50 and the program should run as follows:

```
Please enter a wholesale cost:
5.00
Please enter a markup percentage:
50
The retail price is £7.50.
```

* Make sure you print out the retail price to 2 decimal places. e.g.

```python
x = 6.5
print(f"The value of x is {x:.2f}")
# prints The value of x is 6.50
```

The main program must be written in the ``main()`` function and must use a function called ``calc_retail_price``.

The function should be passed the wholesale cost and markup percentage as arguments and return the retail price..

Below are what ``calc_retail_price`` should return for given values,

``calc_retail_price(3.00, 100)`` should return ``6.0``.

``calc_retail_price(5.00, 50)`` should return ``7.5``.

I would suggest getting ``calc_retail_price()`` working first and then building the program.

You should then print out the correct output to 2 decimal places in the ``main()`` function.

