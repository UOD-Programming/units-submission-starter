# Exercise 4.2

The distance a vehicle travels can be calculated as follows:

``Distance = Speed x Time``

For example, if a train travels 40 miles per hour for three hours, the distance travelled is 120 miles. 

***
# === TASK ===
Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of 
hours it has travelled. 

It should then use a loop to display the distance the vehicle has travelled for each hour of the time period. 

Here is an example of the required output:

```
What is the speed of the vehicle in mph?
40

How many hours has it travelled?
3

Hour | Distance Travelled
-----------------------
1    | 40
2    | 80
3    | 120
```

### Validation 

The program now checks if the speed or the number of hours is less than or equal to zero:
If the speed is less than or equal to zero, it prints an error: 

```ERROR: Speed must be a positive number.```

i.e.

```
What is the speed of the vehicle in mph?
-10

How many hours has it travelled?
3

ERROR: Speed must be a positive number.
```

If the number of hours is less than or equal to zero, it prints an error: 

```ERROR: Hours travelled must be a positive number.```


i.e.

```
What is the speed of the vehicle in mph?
50

How many hours has it travelled?
-3

ERROR: Hours travelled must be a positive number.
```

Make sure that you use spaces to format your table so it matches the output of the test.

You will have to probably experiment with the **tests** to get the format correct.

***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***