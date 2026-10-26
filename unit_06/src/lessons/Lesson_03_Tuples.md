# Tuples

Make sure you have read the lesson first - [Tuples](https://samtoneill.github.io/programming_in_python/unit_6/tuples.html)

*** 
# === TASK ===
Copy and paste the following into ``Lesson_03.py`` to get started.
```python
def tuple_search(t, search_index):
    pass

if __name__ == "__main__":
    # main code
    spaghetti_soup = ("a", "b", "g", "c", "a", "z", "g", "a", "g", "y")
    print(tuple_search(spaghetti_soup, "g")) # should print (3, 2)
```

There is a function called ``tuple_search()`` that you need to update.

The function should count the number of times an item occurs in the tuple and the index (position) of the first of these occurences.

``tuple_search(t, search_item)``

For example,

```python
spaghetti_soup = ("a", "b", "g", "c", "a", "z", "g", "a", "g", "y")
tuple_search(spaghetti_soup, "g")
```
Should return ``(3, 2)``

***

# References 

[Python Tuple Methods - W3schools](https://www.w3schools.com/python/python_tuples_methods.asp)