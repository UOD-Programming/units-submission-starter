# Exercise 3.4

A software company sells a product for £99. It gives a discount on the total price of the order if more than one copy is purchased. 

The discounts are as follows:

| Quantity | Discount |
| -- | -- |
| 5 – 9 | 10% |
| 10 – 19 | 20% |
| 20 – 49 | 30% |
| 50 – 99 | 40% |
| 100 or more | 50% |

Write a program that asks the user to enter the number of copies purchased.

The program should then display the amount of the discount (if any) and the total price of the purchase after the discount has been applied.

For example if the user enters ``25``. The program output would be as follows.
```
Please enter the number of copies of the software you wish to purchase:
25
You have been given a 30% discount on the normal price of £99.
The total cost is £1732.50.
```

Here the calculation works by:

- Work out the total price `99*25 = 2475`.
- Work out the discount, here 30% of 2475 which is calculated by `2475*0.3 = 742.5`.
- Calculate the final price by subtracting the discount from the total.

You will need to display the final total to 2 decimal places. 

You can force python to print to 2 decimal places by using the following in an f-string.

```python
x = 25.2
print(f"{x:.2f}") # prints 25.20
 
```

***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
