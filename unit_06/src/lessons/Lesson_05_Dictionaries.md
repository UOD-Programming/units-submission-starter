# Dictionaries  

Make sure you have read the lesson first - [Dictionaries](https://samtoneill.github.io/programming_in_python/unit_6/dictionaries.html)

*** 
# === TASK ===

Copy the following into ``Lesson_05.py`` to get started.

```python
def add_from_list(d, items_to_add):
    pass
  
if __name__ == "__main__":
    test_dict = {
        "a":1,
        "b":2
    }
    print(test_dict) # prints {'a':1, 'b':2}
    items_to_add = [("e", 5), ("z", 26)]
    add_from_list(test_dict, items_to_add)
    print(test_dict) # prints {'a':1, 'b':2, 'e':5, 'z':26}
```

The function ``add_from_list()``, should take in a dictionary and a list of tuples and then add these as key value pairs to the dictionary. It should not return anything.

For example,
```python
test_dict = {
    "a":1,
    "b":2
}
print(test_dict) # prints {'a':1, 'b':2}
items_to_add = [("e", 5), ("z", 26)]
add_from_list(test_dict, items_to_add)
print(test_dict) # prints {'a':1, 'b':2, 'e':5, 'z':26}
```

HINT: You can loop through a list of paired values as follows. You might want to try this code out if you don't quite understand it.
```python
for x,y in [(1,2), (5,1), (2,3)]:
    print(x,y)
```

***

# References

[Python Dictionaries - W3schools](https://www.w3schools.com/python/python_dictionaries.asp)