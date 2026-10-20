# More About Functions

Make sure you read the lesson first - [More About Functions](https://samtoneill.github.io/programming_in_python/unit_5/more_about_functions.html)

***
# === TASK ===

You will find the following in ``Lesson_02.py``. You will need to remove the ``raise NotImplementedError`` and replace it with your own code. Make sure you read the whole of task.

```python
def reverse(str_to_reverse):
    raise NotImplementedError("You have not implemented the reverse function")

def get_character(string_one, i):
    raise NotImplementedError("You have not implemented the get_character function")

if __name__ == "__main__":
    print(reverse("This is a string")) # prints "gnirts a si sihT"
    print(reverse("Hello World")) # prints "dlroW olleH"
    print(get_character("This is a string", 3)) # prints "i"
    print(get_character("Hello World", 5)) # prints "o"
    
```

The first function is called ``reverse()`` and has a single parameter, a string. The function should output the reverse of the string.

You should do this using a loop. There is a simple way to do this in Python, but it is good practice to write your own ``reverse()`` method.


The second function is called ``get_character()`` and has a string and a number as parameters. It should return the ith character of the string.

The table below gives the return values of the functions for different calls.

| Function call | Expected return value |
| -- | -- |
| ``reverse("This is a string")`` | ``"gnirts a si sihT"`` |
| ``reverse("Hello World")`` | ``"dlroW olleH"`` |
| ``get_character("This is a string", 3)`` | ``"i"`` |
| ``get_character("Hello World", 5)`` | ``"o"`` |

**I suggest you test the above works correctly in the terminal, you should not rely on the tests as the feedback may not be useful.**
*** 
