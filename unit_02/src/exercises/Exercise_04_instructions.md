# Exercise 2.4

# === TASK ===
Copy the following code into ``Exercise_04.py``.
```python
first_name = input("Please enter your first name:\n")

print(f"Hi, your first name is {first_name}")
```
Currenlty asks the user for their first name and then prints it out.

Amend the program so it asks for the first, middle and last name and then prints the user's initials in the following format.

`` Hi, your initials are A.B.C ``.

For example,

```
Please enter your first name:
john
Please enter your middle name:
walter
Please enter your last name:
smith
Hi, your initials are J.W.S
```

Your program should not care whether the input from the user is upper or lower case.

For example,

```
Please enter your first name:
Nelson
Please enter your middle name:
Rolihlahla
Please enter your last name:
MANDELA
Hi, your initials are N.R.M
```

Assume for simplicity that everyone has a first, middle and last name.

Hint: you will need both string indexing and string methods for this.

***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***