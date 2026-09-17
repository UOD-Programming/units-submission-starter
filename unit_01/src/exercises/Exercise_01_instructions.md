# Exercise  1.1

In Python, you can print out the current date and time by using the ```datetime``` module. 

```python
import datetime

current_time = datetime.datetime.now()

print(f"The date and time is {current_time}")
```

Note the ``f`` in front of the string, this tells it to substitute the value of ``current_time`` into the string.

We will discuss modules later in the course, but they basically provide extra functionality for you to use.

You can print a blank line with,
```python
print()
```
or with:
```python
print("")
```


# === TASK ===

Copy and paste the following code into ``Exercise_01.py``.

```python
import datetime

current_time = datetime.datetime.now()
print("The current date and time is {}".format(current_time))
```

Edit the code so that it outputs the following:

```
Hello and Welcome to Programming in Python.

Python is a great general purpose language and is used by the likes of Google and Facebook.

The current date and time is {YOU SHOULD PUT THE CURRENT DATETIME HERE}
```
***Note that to pass the tests you must have exactly the output above, apart from the date and time.***

For example,

```
Hello and Welcome to Programming in Python.

Python is a great general purpose language and is used by the likes of Google and Facebook.

The current date and time is 2024-09-26 12:01:25.883605
```