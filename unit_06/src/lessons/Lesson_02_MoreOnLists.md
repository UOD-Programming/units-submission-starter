# More on Lists  

Make sure you have read the lesson first - [More on Lists](https://samtoneill.github.io/programming_in_python/unit_6/more_on_lists.html)

*** 
# === TASK ===

Copy the following into ``Lesson_02.py`` to get started.
```python
def change_list(my_list):
    pass

if __name__ == "__main__":
    fruit_list = ["Pear", "Orange", "Peach", "Apple"]
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    new_fruit_list = change_list(fruit_list)
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    print(new_fruit_list) # prints ["Apple", "Banana", "Peach", "Pear"]
```

There is a function called ``change_list()`` that you need to update.

The function should remove the second item, add "Banana" to the list and then sort the list. 

The function should return the modified list without affecting the original list.

An example of how the function should work is given below.
```python
fruit_list = ["Pear", "Orange", "Peach", "Apple"]
print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
new_fruit_list = change_list(fruit_list)
print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
print(new_fruit_list) # prints ["Apple", "Banana", "Peach", "Pear"]
```

***