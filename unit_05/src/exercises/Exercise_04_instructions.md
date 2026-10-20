# Exercise 5.4

You will find the following code in ``Exercise_04.py``. NOTE: You will have to update the function signature for ``arithmetic_sum``.

```python
def arithmetic_sum():
    pass

if __name__ == "__main__":
    print(arithmetic_sum(1,1,100))   # prints the return value - 5050
    print(arithmetic_sum(3,2,15))    # prints the return value -  255
    print(arithmetic_sum(10,4,5))    # prints the return value -  90
    print(arithmetic_sum(-5, -2, 20))    # prints the return value -  -480
```

Amend the ``arithmetic_sum`` function so that it takes in integers ``a``, ``d``, and ``n``  and prints out the sum of the sequence, known as a series.

```
a + (a+d) + (a+2*d) + ... + (a+(n-1)*d)
```

``a`` is the first term, ``d`` is the difference between terms, and ``n`` is the number of terms in the series.

For example, the values ``a = 1``, ``d = 1`` and ``n = 100`` is just the sum of the first 100 numbers.

``
1 + 2 + 3 + ... + 99 + 100
``

For ``a = 3``, ``d = 2`` and ``n = 6`` we would have,

``
3 + 5 + 7 + 9 + 11 + 13
``

One last example, ``a = 10``, ``d = 4`` and ``n = 5``

``
10 + 14 + 18 + 22 + 26
``

Calling the function with the following arguments (values) should result in the following.

| function call | series | return value |
| -- | -- | -- |
| ``arithmetic_sum(1,1,100)`` |``1 + 2 + ... + 99 + 100``| ``5050`` |
| ``arithmetic_sum(3,2,15)`` |``3 + 5 + ... + 29 + 31``| ``255`` |
| ``arithmetic_sum(10,4,5)`` |``10 + 14 + 18 + 22 + 26``| ``90`` |
| ``arithmetic_sum(-5, -2, 20)`` |``-5 -7 - ... - 41 - 43``| ``-480`` |
