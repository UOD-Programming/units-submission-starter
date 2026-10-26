# List/Dictionary Comprehension

Make sure you have read the lesson first - [List/Dictionary Comprehension](https://samtoneill.github.io/programming_in_python/unit_6/list_and_dictionary_comprehension.html)

***
# === TASK ===

Copy and paste the following into ``Lesson_06.py``.
```python
def sum_div_3(n):
    """you should update div_by_3_list to generate the list of numbers divisible by 3 and return their sum.

    e.g. for n = 10 it should look at 1,2,3,4,5,6,7,8,9,10 and the list should contain [3,6,9]. The function should then return the sum of this list, in this case 18"""
    div_by_3_list = []
    return sum(div_by_3_list)


if __name__ == "__main__":
    print(sum_div_3(10))  # should print 18
    print(sum_div_3(12))  # should print 30
    print(sum_div_3(100))  # should print 1683

```

Use list comprehension to find the sum of all numbers that are divisable by ``3`` between ``1`` and an upper limit ``n``. If you are struggling, write this in a more "traditional" format first and then convert it to list comprehension.

You should update the function ``sum_div_3(n)`` so that it returns the correct sum.

For example, ``sum_div_3(12)`` should sum up ``3,6,9`` and ``12`` which totals to ``30``.

***