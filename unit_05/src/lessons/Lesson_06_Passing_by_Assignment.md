# Passing by Assignment

Make sure you have read the lesson first - [Passing by Assignment](https://samtoneill.github.io/programming_in_python/unit_5/passing_by_assignment.html)

***
# === TASK ===

You will find the following in ``Lesson_06.py``.
```python
import copy

def update_list_item_one(items, x):
  pass

def new_list_item_one(items, x):
  pass

if __name__ == "__main__":
    list_one = [1,2,3,4]
    update_list_item_one(list_one, 0)
    print(list_one) # should print out [0,2,3,4]
    
    list_one = [1,2,3,4]
    new_list_item_one(list_one, 0)
    print(list_one) # should print out [1,2,3,4]
    
    list_one = [1,2,3,4]
    list_one = new_list_item_one(list_one, 0) # bind the new object to l
    print(list_one) # should print out [0,2,3,4]
```

Amend the two functions. The first function ``update_list_item_one()`` should take a list and a number and update the first item in the list with the number. It should operate on the original list. It does not require a return statement.

For example,

```python
list_one = [1,2,3,4]
update_list_item_one(list_one, 0)
print(list_one) # prints out [0,2,3,4]
``` 

The second function ``new_list_item_one()`` should create a copy of the list that is passed into the function (this will be a new object), update the first item in the new list and then return the new list.

For example,

```python
list_one = [1,2,3,4]
new_list_item_one(list_one, 0)
print(list_one) # prints out [1,2,3,4]
```
does not update the original list, however,

```python
list_one = [1,2,3,4]
list_one = new_list_item_one(list_one, 0) # bind the new object to list_one
print(list_one) # prints out [0,2,3,4]
``` 
reflects the changes made because the new object returned by ``new_list_item_one()`` was reassigned to ``list_one``.


***
