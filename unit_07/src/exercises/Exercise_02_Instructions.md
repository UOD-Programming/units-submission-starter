# Exercise 7.2

The following is a simple application that should display a menu and let the user add menu items.

Copy and paste the following into ``Exercise_02.py``.

```python
import json


def add_item(menu_dict, name, price):
  """ Adds a new item to the menu"""
  pass


def load(filename):
  """ loads the file into a dictionary and returns dictionary"""
  pass


def save(filename, menu_dict):
  """ save out the menu to the filename"""
  pass


def list_options():
  print("Option 1: List Menu")
  print("Option 2: Add Menu Item")
  print("Option 3: Quit")


def print_menu(menu_dict):
  print("\nMENU")
  print("----\n")
  for key, value in menu_dict["menu"].items():
    print(f"Item {key}\n")
    print(f"Name: {value['Name']}")
    print(f"Price: {value['Price']}\n")


def main():
  filename = "./src/exercises/Exercise_02_menu.json"
  menu = load(filename)
  list_options()
  option = input("\nPlease select an option:\n")
  while option != "3":
    if option == "1":
      print_menu(menu)
    elif option == "2":
      name = input("\nPlease enter a name:\n")
      price = input("\nPlease enter a price:\n")
      add_item(menu, name, price)
      save(filename, menu)
    option = input("\nPlease select an option:\n")


if __name__ == "__main__":
  main()

```

## Guidance

The menu is stored in ``Exercise_02_menu.json``.

Currently the application is missing 3 key functions. When implmented the rest of the code will work fine. 

**DO NOT CHANGE THE CONTENTS OF:**

- ``main()``
- ``list_options()``
- ``print_menu()``

You need to use the JSON module to load the data from ``Exercise_02_menu.json``, you should do this by implementing the ``load()`` function so that it loads the JSON data and returns it from the function

There is also an ``add_item`` function that adds a menu item to the menu and then saves it out to the JSON.

You should also implement the ``save()`` function to that it saves the dictionary that is passed into ``save()`` into the filename that is also passed into ``save()``.

I would start by implementing the functions in the following order:

1. ``load()``
2. ``add_item()``
3. ``save()``


## How the functions should work

I would use these to test each of the functions separately. You can use the code snippets in ``if __name__ == "__main__"`` instead of calling the ``main()`` function.

### Load Function

The ``load()`` function should take in a filename, e.g. ``Exercise_02_menu.json``, load the file and then return a Python dictionary.

```python
filename = "./src/exercises/Exercise_02_menu.json"
menu_dict = load(filename)
print(menu_dict)
```

Would print out:

```
{'next_id': 4, 'menu': {'1': {'Name': 'Burger and Fries', 'Price': 5.99}, '2': {'Name': 'Chicken and Rice', 'Price': 6.99}, '3': {'Name': 'Saag Aloo', 'Price': 8.99}}}
```

### Save Function

The ``save()`` function should save the passed in dictionary ``menu_dict`` to a file of the name ``filename``.

```python
menu_two = {
  "next_id": 2,
  "menu": {
    "1": {"Name": "Sweet and Sour Chicken", "Price": 5.99}  
  }
}
save("./src/exercises/Exercise_02_menu.json", menu_two)
```

Would save out to a file called ``./src/exercises/Exercise_02_menu.json`` with the contents
```json
menu_test_two = {
  "next_id": 2,
  "menu": {
    "1": {"Name": "Sweet and Sour Chicken", "Price": 5.99}  
  }
}
```

## Add Item Function
The ``add_item()`` function should add an item to the passed in dictionary ``menu_dict``. It should use the value of ``"next_id"`` as the ``key`` for the new item.

In the following case, the next menu item will have a ``key`` of ``2``

Note it should also increment the value of ``"next_id"`` by ``1``.

```python
menu_test_two = {
  "next_id": 2,
  "menu": {
    "1": {"Name": "Sweet and Sour Chicken", "Price": 5.99}  
  }
}
add_item("Onion Soup", "3.99")
```
Would result in an update to ``menu_test_two`` of:

```python
menu_test_two = {
  "next_id": 3,
  "menu": {
    "1": {"Name": "Sweet and Sour Chicken", "Price": 5.99},  
    "2": {"Name": "Onion Soup", "Price": 3.99}  
  }
}
```

Note that the value of ``"next_id"`` was incremented by ``1``

## Starting Data - ``Exercise_02_menu.json``

If you mess up ``Exercise_02_menu.json``, this is the starting data.
```json
{
    "next_id": 4,
    "menu": {
        "1": {
            "Name": "Burger and Fries",
            "Price": 5.99
        },
        "2": {
            "Name": "Chicken and Rice",
            "Price": 6.99
        },
        "3": {
            "Name": "Saag Aloo",
            "Price": 8.99
        }
    }
}
```