# Creating a Module

Make sure you have read the lesson first - [Creating a Module](https://samtoneill.github.io/programming_in_python/unit_7/creating_a_module.html)


 # === TASK ===
Create a new module in the file called ``Lesson_02_hello.py``. Make sure it is in the same directory as ``Lesson_02.py``.

Your module should include two functions called ``hi()`` and ``goodbye()`` which take in a name and returns a string.

For example, ``hi()`` should operate as follows.

```python
hi("Joe") # returns "Hello Joe"
print(hi("Joe")) # prints Hello Joe
```
And, ``goodbye()`` should operate as follows.
```python
goodbye("Joe") # returns "Goodbye Joe"
print(goodbye("Joe")) # prints Goodbye Joe
```

I have included this code so that you can use it in ``Lesson_02.py`` to test your module.

```python
# Lesson_02.py
# import 
import Lesson_02_hello as hello

def main():
  print(hello.hi("Joe")) # prints Hello Joe
  print(hello.goodbye("Joe")) # prints Goodbye Joe

if __name__ == "__main__":
  main()
```

If you have done this correctly, the output of your program should be:

```
Hello Joe
Goodbye Joe
```

***