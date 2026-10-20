# Exercise 5.3

You will find the following code in ``Exercise_03.py``. NOTE: You will have to update the function signature for ``num_digits``.
```python
def num_digits():
    # remove the following line and write the function here
    pass

def main():
    # remove the following line and write your program here
    pass

# This is needed for the tests. This is now the first bit of code Python will run.
if __name__ == "__main__":
    main() # calls the main function
```
Write a program that asks the user for a positive whole number. Your program should output the number of digits in the whole number. If the input is invalid the program ends with ``Invalid input.``

Your program must be written inside the ``main()`` function and work the same as the given examples:

```
Please enter a positive whole number:
3
3 has 1 digit.
```

```
Please enter a positive whole number:
345
345 has 3 digits.
```

```
Please enter a positive whole number:
345.6
Invalid input.
```

```
Please enter a positive whole number:
0
Invalid input.
```

```
Please enter a positive whole number:
Sam
Invalid input.
```

Your program must use a function ``num_digits`` that takes a ``int`` as a single parameter and returns the number of digits in a positive integer, ``n`` as a type ``int``. 

Hint. To determine the number of digits in a positive integer ``n``, divide it by ``10`` repeatedly. When ``n < 1``, the number of divisions to date indicates how many digits the number originally had.

```
345/10 = 34.5
Is this less than 1? No.
34.5/10 = 3.45
Is this less than 1? No.
3.45/10 = 0.345
Is this less than 1? Yes.

3 digits...
```

For example,

``num_digits(5467)`` should return ``4``.

``num_digits(100000)`` should return ``6``.

The skeleton of the program is set up for you. You will see the ``pass`` statement, this is just a placeholder for the function body. You should remove this and replace it with the correct code.
