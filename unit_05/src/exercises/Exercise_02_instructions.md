# Exercise 5.2

The formula for converting a temperature from Fahrenheit to Celsius is: 

``c = (5/9)*(f – 32)`` 

and Celsius to Fahrenheit

``f = (9/5)*c + 32``

where ``f`` is the temperature in Fahrenheit and ``c`` is the temperature in Celsius.

***

You will find the following code in ``Exercise_02.py``. NOTE: You will have to update the function signature for ``convert_temp``.

```python
def convert_temp():
  pass

if __name__ == "__main__":
    # I would comment some of these out as you build up parts of convert_temp
    # e.g. just start by getting convert_temp(20) to work
    print(convert_temp(20)) # Prints 68.0
    print(convert_temp(-10)) # Prints 14.0
    print(convert_temp(68, Fahrenheit=True)) # Prints 20.0
    print(convert_temp(-100, Fahrenheit=True)) # Prints -73.33
    print(convert_temp(-300)) # ValueError("Temperature below absolute zero is invalid for Celsius.")
    print(convert_temp(-500, Fahrenheit=True)) # ValueError("Temperature below absolute zero is invalid for Fahrenheit.")
```

Write a function that: 
* Converts Celsius to Fahrenheit. The Celsius temperature is passed as a parameter and it returns the corresponding Fahrenheit temperature. 
* Convert Fahrenheit to Celsius. The Fahrenheit temperature is passed as a parameter and it returns the corresponding Celsius temperature.
* Raises a ValueError if the input for Celsius is below absolute zero, -273.15°C. You can use the following to raise the appropriate value error.
  * `raise ValueError("Temperature below absolute zero is invalid for Celsius.")`
* Return ``None`` if the input for Fahrenheit is below absolute zero, -459.67°F. You can use the following to raise the appropriate value error.
  * `raise ValueError("Temperature below absolute zero is invalid for Fahrenheit.")`

This should be done with a keword argument ``Fahrenheit`` 

```python
convert_temp(20) # convert celsius to fahrenheit. Returns 68.0
convert_temp(-10) # convert celsius to fahrenheit. Returns 14.0
convert_temp(68, Fahrenheit=True) # convert fahrenheit to celsius. Returns 20.0
convert_temp(-100, Fahrenheit=True) # convert fahrenheit to celsius. Returns -73.33
```

You should round your answer to 2 decimal places using the ``round`` function. e.g. ``round(3.14159, 2)`` is ``3.14``.

To pass all the tests, your function should also take into account absolute zero, which is  -273.15°C, or -459.67°F and return ``None`` in either of these cases.

```python
convert_temp(-280) # convert celsius to fahrenheit. Returns None
convert_temp(-460, Fahrenheit=True) # convert fahrenheit to celsius. Returns None
```

I would leave this until you have the main conversion working then add this functionality.

I would also suggest that you test your function by printing out the result of calling it with some of the values above. e.g.

```python
print(convert_temp(20)) # should print 68.0 out to the console
```
Remember that the function needs to be above any print statement otherwise you will get a ``NameError``.
***
  
  
