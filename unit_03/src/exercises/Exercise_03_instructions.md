# Exercise 3.3

This is a further extension of 3.1 and 3.2. 

The formula to convert a temperature given in Celsius to Fahrenheit is:

```Fahrenheit = (9/5) * Celsius + 32```

Using a bit of algebra, the formula to convert a temperature given in Fahrenheit to Celsius is:

```Celsius = (5/9) * (Fahrenheit - 32)```

## Plan your program!
The following task is a bigger program than we've dealt with before and requires some thought. 

You should try and plan your program on a piece of paper. You could create a flow diagram or write pseudocode.

***
Write a program that asks the user if they want to convert Celsius to Fahrenheit or Fahrenheit to Celsius.

The program should then wait for the user's response and then do the correct calculation and display the correct output.

The program should do the above as follows:

* Prompt the user to choose by asking the following:
```
Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:
```

* If the user does not enter ``1`` or ``2``, but a different number, the program should display the following error message:

```
ERROR: Invalid option
```
* If the user enters ``1`` then convert Celsius to Fahrenheit by prompting the user with:
```
Please enter the temperature in Celsius:
```
and display:
```
A Celsius is equivalent to B Fahrenheit.
```   
* If the user enters ``2`` then convert Fahrenheit to Celsius by prompting the user with:
```
Please enter the temperature in Fahrenheit:
```
and display:
```
X Fahrenheit is equivalent to Y Celsius.
```   
* NOTE: If the user enters a value for the number to be converted that is less than ``0``, the program should display the following:
```
ERROR: You must enter a value of 0 or greater.
```
Really we can have input less than ``0`` for both Fahrenheit and Celsius, but for convenience we will ignore this.

## Example Output (Use This!) 
Example output for the different scenarios is given below:

```
Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:
3
ERROR: Invalid option
```
```
Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:
1
Please enter the temperature in Celsius:
20.2
20.2 Celsius is equivalent to 68.36 Fahrenheit.
```
```
Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:
1
Please enter the temperature in Celsius:
-2
ERROR: You must enter a value of 0 or greater.
```
```
Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:
2
Please enter the temperature in Fahrenheit:
70.25
70.25 Fahrenheit is equivalent to 21.25 Celsius.
```
```
Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:
2
Please enter the temperature in Fahrenheit:
-2
ERROR: You must enter a value of 0 or greater.
```
 
***Note that to pass the tests you must have exactly the output given by the example output, apart from the numbers which will differ depending on what the user inputs.***

