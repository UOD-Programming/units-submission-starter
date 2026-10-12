# For Loops

Make sure you have read the lesson first - [For Loops](https://samtoneill.github.io/programming_in_python/unit_4/for_loops.html)

***
# === TASK ===
You can find the length of a string by using the ``len()`` function. 

For example:

```python
string1 = "for loop"
len_string = len(string1)
print(len_string)
# note you could do this in one line print(len(string1))
```
This will output the length of the ``str``, ``"for loop"``. That is, ``8``.


Copy the following into ``Lesson_03.py``:

```python
# Do not touch this line - It is just there to set up the string list from the input
# string_list will contain a list of strings that have been entered.
string_list = input("Please enter a list of numbers separated by a comma.\ne.g. Citreon,Ford,Audi,Mercedes\n").split(',')

print(string_list)
```

This code will accept a list of comma-separated strings. e.g. ``Citreon,Ford,Audi,Mercedes``.

If you try running the program and you enter a list of comma-separated strings they will be printed back to the console.

```
['Citreon','Ford','Audi','Mercedes']
```

The strings inputted are stored in the ``list`` named ``string_list``.

**Amend the program so that it prints out the following for each inputted string.**

```
The length of the string {string} is {length of string}.
```

For example, for the string ``"Ford"`` the program would print:

```
The length of the string Ford is 4.
```

For the input ``one,two,three,four,five``, the whole program acts as follows:
```
Please enter a list of numbers separated by a comma.
e.g. Citreon,Ford,Audi,Mercedes
one,two,three,four,five
The length of the string one is 3.
The length of the string two is 3.
The length of the string three is 5.
The length of the string four is 4.
The length of the string five is 4.
```

For the input ``Citreon,Ford,Audi,Mercedes``, the whole program acts as follows:
```
Please enter a list of numbers separated by a comma.
e.g. Citreon,Ford,Audi,Mercedes
Citreon,Ford,Audi,Mercedes
The length of the string Citreon is 7.
The length of the string Ford is 4.
The length of the string Audi is 4.
The length of the string Mercedes is 8.
```

**Note that to pass the tests you must have exactly the output above, apart from the input which will differ depending on what the user inputs.**
***
