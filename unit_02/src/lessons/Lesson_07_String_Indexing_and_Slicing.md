# String Indexing and Slicing  

# === TASK===
Copy the following code into ``Lesson_07.py``.

```python
# DO NOT EDIT THESE TWO LINES
firstname = input("Please enter a first name: \n")  # leave this alone!
surname = input("Please enter a surname: \n")  # leave this alone!

# -------------------------------------------------------

# Edit the following line so that it prints out the first character of the first name
print(f"The first character of the first name is {firstname}")

# Edit the following line so that it prints out the last character of the surname (negative indexing)
print(f"The last character of the surname is {surname}")

# Edit the following line so that it prints the initials of the person. e.g. Mary Smith would result in M.S
print(f"The person's initials are {firstname}.{surname}")

# Edit the following line so that it prints the first 3 characters of the first name. For example Mary would print out Mar
print(f"The first 3 characters of the first name are {firstname}")

# Edit the following line so that it prints the last 4 characters of the surname
print(f"The last 4 characters of the surname are {surname}")
```


1. Edit the following line so that it prints out the first character of the first name
```python
print(f"The first character of the first name is {firstname}")
```
2. Edit the following line so that it prints out the last character of the surname (negative indexing)
```python
print(f"The last character of the surname is {surname}")
```
3. Edit the following line so that it prints the initials of the person. e.g. Mary Smith would result in M.S
```python
print(f"The person's initials are {firstname}.{surname}")
```
4. Edit the following line so that it prints the first 3 characters of the first name. For example, Mary would print out Mar
```python
print(f"The first 3 characters of the first name are {firstname}")
```
5. Edit the following line so that it prints the last 4 characters of the surname (note we assume for simplicity that the surname contains at least 4 characters, what happens if it is less than 4?)
```python
print(f"The last 4 characters of the surname are {surname}")
```
An example of the correct program for the input ``Mary Smith`` is given below.
```
Please enter a first name:
Mary 
Please enter a surname:
Smith
The first character of the first name is M
The last character of the surname is h
The person's initials are M.S
The first 3 characters of the first name are Mar
The last 4 characters of the surname are mith
```
***