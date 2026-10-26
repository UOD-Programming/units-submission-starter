# ``*args`` and ``**kwargs``

Make sure you have read the lesson first - [``*args`` and ``**kwargs``](https://samtoneill.github.io/programming_in_python/unit_8/args_and_kwargs.html)

***
# === TASK ===
Create a function called initials that takes in a persons names and then returns the initials. You should pass the names using ``*args``.

For example for ``James Marshall Hendrix`` it should return ``J.M.H``. 

Or, for John Ronald Reuel Tolkien it should return ``J.R.R.T`` (one ``*args`` to rule them all).

Copy and pased this code into ``Lesson_02.py`` to get started.

```python
def initials(*args):
  pass

if __name__ == "__main__":
  print(initials("James", "Marshall", "Hendrix")) # should print the return value of "J.M.H"
  print(initials("John", "Ronald", "Reuel", "Tolkien")) # should print the return value of "J.R.R.T"
  
```
