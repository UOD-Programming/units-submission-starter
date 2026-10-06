# Booleans  

# === TASK ===

For this program you should fix the single line instructed. You should also just run the tests directly to see if it works

Copy the following code into **Lesson_04.py**.

```python
# DO NOT TOUCH THESE LINES. THEY ARE USED BY THE TESTS
# If you want to test this program, when you hit Run, enter values of True or False via the console
is_raining = bool(int(input()))
no_hat = bool(int(input()))
#######################################################

# You should fix this line to by forming an expression using is_raining and no_hat to produce the correct result for takes_umbrella. 

# e.g takes_umbrella = is_raining or no_hat

# Note you only have to fix the following line to pass the tests. No if statements etc.. required!
takes_umbrella = True

print(takes_umbrella)
```
 
Sam doesn't like getting his hair wet and sometimes wears a hat.

* On days that it is raining and Sam is not wearing a hat, Sam takes his umbrella.
* On days that it is raining and Sam is wearing a hat, Sam does not take an umbrella.
* If it is not raining Sam does not take an umbrella.
&nbsp;

We use two variables ``is_raining`` and ``no_hat`` to represent whether it is raining and if Sam is wearing a hat.

* If it is raining ``is_raining = True``
* If Sam is **NOT** wearing a hat ``no_hat = True``.
&nbsp;

Using a third variable ``takes_umbrella`` determine if Sam should take his umbrella by combining ``is_raining`` and ``no_hat``.
 
For example, on days that it is raining and Sam is not wearing a hat the variables will have the following values:
* ``is_raining = True``
* ``no_hat = True``
* ``takes_umbrella = True``
&nbsp;

``is_raining`` and ``no_hat`` have been set up for you. Combine them with logical operators to get the correct value of ``takes_umbrella``.

HINT: You should consider the truth table and fill in the missing entries. This will then give you a hint to what the expression should be.

| `is_raining` | `no_hat`| `takes_umbrella` |
| :--: | :--: | :--: |
| `False` | `False` | ?|
| `False` | `True` |?|
| `True` | `False` |?|
| `True` | `True` | `True`|
***

[W3Schools - Python Booleans](https://www.w3schools.com/python/python_booleans.asp)

[W3Schools - Python Comparison Operators](https://www.w3schools.com/python/python_operators.asp)