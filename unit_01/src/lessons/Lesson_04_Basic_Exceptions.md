# Basic Exceptions  

# === TASK ===

1. Copy and paste the following code into ``Lesson_04.py``.

```python
# You need to fix the following lines
# Run the code and then use the error messages to fix each line

# This line has a SyntaxError
print(hello world)

# This line has a NameError
printf("Hello World!")

# The following lines cause a TypeError
int1 = 100
str1 = "10"
print(int1 / str1)
``` 

3. You will see a ```SyntaxError``` on line 5 because of some missing ```""``` around the string.
   
```python
print(hello world)
```
Fix this so that it prints out ``hello world``.

2. Once you have completed this run the code. You will see a ``NameError`` on line 8 because ```printf``` is not a valid name.

```python
printf("Hello World!")
```
Fix this so that it prints out ``Hello World``.

3. Once you have completed this run the code. You will see a ``TypeError`` on line 13 because we are tring to divide ```/``` an ```int``` by a ```string```.
```python
int1 = 100
int2 = "10"
print(int1 / int2)
```
Fix this so that it prints out `10.0`.

# References

[Python Exceptions](https://docs.python.org/3/library/exceptions.html)
