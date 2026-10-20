# Specification and Docstrings

Make sure you have read the lesson first - [Specification and Docstrings](https://samtoneill.github.io/programming_in_python/unit_5/specification_and_docstrings.html)

***
# === TASK ===
You will find the following into ``Lesson_05.py``. You won't have to understand this code to pass the task, but you will need to read on.

```python
def add(x, y):
    """
    Adds up two numbers and returns the result.

    Parameters
    ----------
    x: int or float
        First number to add.
    y: int or float
        Second number to add.

    Returns
    -------
    int or float
        Sum of x and y.
    """
    return x + y


# Example from Guttang (2021)
def find_root(x, power, epsilon=0.01):
    """
    Find a y such that y**power = x (within epsilon x).

    e.g. For x = 27 and power = 3 then y = 3 as 3**3 = 27.
    i.e. the cubed root of 27 is 3.

    Parameters
    ----------
    x :int or float
        Number we want the root of.
    power: int
        Root number e.g. square root, power = 2.
    epsilon: int or float, default 0.01 
        Error tolerance for the answer.

    Returns
    -------
    float or None
    """
    # if x is negative and power even. No root exists
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    # check if the answer is close enough
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans    
        ans = (high + low) / 2.0
    return ans
   
if __name__ == "__main__":
    # add the line of code here
    pass
```

The built-in ``help()`` function allows us to print out the docstring of a function. 

You will see that you get the docstring for the function. 

You will also see a more complicated function called ``find_root``. 

For now, it doesn't matter how it works, but the docstring does tell us what it does and requires a longer description.

Add a line of code to the bottom of **main.py** that prints out the docstring for ``find_root`` by using the ``help()`` function. Make sure you don't use any indentation so that the code isn't inside a function.

Think carefully, ``help()`` is a function that prints out to the console and returns ``None``.
***
