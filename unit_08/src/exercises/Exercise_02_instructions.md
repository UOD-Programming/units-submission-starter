# Exercise 8.2

Write two functions ``and_many()`` and ``or_many()`` that take an arbitary number of Boolean arguments through ``*args``. 

The functions should then return result of applying the boolean operators ``and`` and ``or`` to all the arguments.

For example for ``and_many()``,

``and_many(True, True, True)`` should computes ``True and True and True`` which results in ``True`` and therefore should return ``True``.

``and_many(True, False, True)`` should computes ``True and False and True`` which results in ``False`` and therefore should return ``False``.

``and_many(True, False, True, True)`` should computes ``True and False and True and True`` which results in ``False`` and therefore should return ``False``.

For example for ``or_many()``,

``or_many(True, True, True)`` should computes ``True or True or True`` which results in ``True`` and therefore should return ``True``.

``or_many(True, False, True)`` should computes ``True or False or True`` which results in ``True`` and therefore should return ``True``.

``and_many(False, False, False, False)`` should compute ``False or False or False or False`` which results in ``False`` and therefore should return ``False``.

Copy and paste the following into ``Exercise_02.py`` to get started:

```python
def and_many(*args):
  pass


def or_many(*args):
  pass


if __name__ == "__main__":
  print(and_many(True))  # prints True
  print(and_many(True, True))  # prints True
  print(and_many(True, True, True))  # prints True
  print(and_many(True, True, True, True))  # prints True
  print(and_many(False, True))  # prints False
  print(and_many(True, False, True))  # prints False
  print(and_many(True, True, True, False))  # prints False

  print(or_many(True))  # prints True
  print(or_many(False, True))  # prints True
  print(or_many(True, False, True))  # prints True
  print(or_many(True, True, True, False))  # prints True
  print(or_many(False))  # prints False
  print(or_many(False, False))  # prints False
  print(or_many(False, False, False))  # prints False
  print(or_many(False, False, False, False))  # prints False
```
  