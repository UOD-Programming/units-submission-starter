# Keyword Arguments and Default Values

Make sure you have read the lesson first - [Keyword Arguments and Default Values](https://samtoneill.github.io/programming_in_python/unit_5/keyword_arguments_and_default_values.html)

***
# === TASK ===

You will find the following in ``Lesson_04.py`` to get started.

```python
def print_list():
    pass

if __name__ == "__main__":
    print_list([4,1,6,7], multiple = 2)
    print_list([4,1,6,7], multiple = 3)
    print_list([4,1,6,7])
```

Amend the function called ``print_list`` that prints the multiple of each item in the list

For example ``print_list([4,1,6,7], multiple = 2)``

```
8
2
12
14
```

For example ``print_list([4,1,6,7], multiple = 3)``

```
12
3
18
21
```

By default your function when called without the **keyword argument**  ``multiple``, i.e. ``print_list([4,1,6,7])`` should output:

```
4
1
6
7
```
