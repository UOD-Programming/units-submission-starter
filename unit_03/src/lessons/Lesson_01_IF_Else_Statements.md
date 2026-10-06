# If ... Else Statement  

# === TASK ===
You can test if a number is ***even*** or ***odd*** using the modulus operator ``%``.

For example, ``4 % 2 = 0`` evaluates to ``0`` because ``2`` divides ``4`` with no remainder.

However, `` 7 % 2 = 1`` evaluates to ``1`` because ``2`` divides ``7`` with remainder ``1``.

We can use this to evaluate if a number is ***odd*** or ***even***. The expression ``x % 2 == 0`` evaluates to ``True`` if ``x`` is ***even*** and ``False`` if it is ***odd***.

The expression ``x % 2 == 0`` compares the left side ``x % 2`` to the right side ``0`` to see if they are equal.

For example,
 
| ``x`` | ``x % 2`` | ``x % 2 == 0`` |
| --- | --- | --- |
| ``4`` | ``0`` | ``True`` |
| ``7`` | ``1`` | ``False`` |

I suggest you try some even and odd examples out in the console if you don't understand this.

E.g. Try:

```python
# test 4 to see if it is even
4 % 2 == 0  # will print out True as 4 % 2 evaluates to 0
```

```python
# test 7 to see if it is even
7 % 2 == 0  # will print out False as 7 % 2 evaluates to 1
```

Write a program that asks a user for a number and then prints out whether it is ***even*** or ***odd***.

Your program should work as follows:
```
Please enter a whole number:
7
Your number is odd!
```

```
Please enter a whole number:
4
Your number is even!
```
***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***