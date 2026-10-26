# Closures and Decorators (Advanced)

Make sure you have read the lesson first - [Closures and Decorators (Advanced)](https://samtoneill.github.io/programming_in_python/unit_8/closures_and_decorators.html)

Please note that this is a long lesson because there are a lot of details that you need to understand 
 closures and decorators.

# === TASK ===

If you have read everything and understand it, then this should be reasonably straight forward.

Create a logger for a function called ``logger()``. (I would use the examples below as your starting point.)

Your logger should decorate a function and do the following:

- print some stuff
- call the function
- print some more stuff

It should work on any function with any number of arguments or keyword arguments.

Note you will need to look up how to get access to a functions name. You can read the following to help - [Function Name](https://thispointer.com/how-to-get-a-function-name-as-a-string-in-python/)

The follwoing examples illustrate how the logger decorator should work. Currently the decorator does nothing but return the same function.

## Example 1
```python
def logger(func):
    # write your code here
    return func

@logger
def add_three(x, y, z):
    print(x + y + z)

if __name__ == "__main__":
    add_three(3,4,5)
```

The above code should print the following:

```
Logging function...
The functions name is add_three
Calling the function...
12
Ending logging...
```
## Example 2
```python
def logger(func):
    # write your code here
    return func

@logger
def hello():
    print("hello")

if __name__ == "__main__":
    hello()
```

The above code should print the following:

```
Logging function...
The functions name is hello
Calling the function...
hello
Ending logging...
```
## Example 3
```python
def logger(func):
    # write your code here
    return func

@logger
def keyword(a=1, b=2, c=3):
    print(a+b+c)

if __name__ == "__main__":
    keyword(a=2)
```

The above code should print the following:

```
Logging function...
The functions name is keyword
Calling the function...
7
Ending logging...
```

To get started copy and paste the following into ``Lesson_06.py``. Currently the ``logger`` function just returns the function undecorated.

```python
def logger(func):
    # write your code here
    return func

@logger
def funky_func(x, y, z=1):
    print(x)
    print(y)
    print(z)

@logger
def add_three(x, y, z):
    print(x + y + z)

@logger
def hello():
    print("hello")

@logger
def keyword(a=1, b=2, c=3):
    print(a + b + c)

if __name__ == "__main__":
    funky_func(3, 4, z=10)
    print()
    funky_func(3, 4)
    print()
    add_three(3, 4, 5)
    print()
    hello()
    print()
    keyword()
```

It should output the following if implemented correctly.

```
Logging function...
The functions name is funky_func
Calling the function...
3
4
10
Ending logging...

Logging function...
The functions name is funky_func
Calling the function...
3
4
1
Ending logging...

Logging function...
The functions name is add_three
Calling the function...
12
Ending logging...

Logging function...
The functions name is hello
Calling the function...
hello
Ending logging...

Logging function...
The functions name is keyword
Calling the function...
6
Ending logging...
```
