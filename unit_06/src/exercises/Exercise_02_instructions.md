# Exercise 6.2  

Write a program that randomly generates 100 integer values in the range 1 to 50. Your program should display the number of the numbers generated occurring in bins of 10, i.e. the ranges 1-10, 11-20, etc. 

For example, your program should display:

```
I have generated 100 random numbers between 1 and 50. 
The count in the following ranges is:
1..10: 20
11..20: 25
21..30: 12
31..40: 23
41..50: 20
```
Hint. Use a list or dictionary to hold the counts, one item for each range.

You can generate a list of random numbers using list comprehension.

```python
import random
rand_num_list = [random.randint(0,10) for _ in range(5)] # generates a list of 5 random numbers between 0 and 5.
```
The easiest way to write this program is to use if statements to determine if a number is within a particular range. 

You should write this code in the ``main()`` function.

Copy the following code into ``Exercise_02.py`` to get started.

```python
import random

def rand_num_list_gen(num=100, lower=1, upper=50):
    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list

def main():
    rand_num_list = rand_num_list_gen()
    print("I have generated 100 random numbers between 1 and 50.")
    pass

def advanced_main():
    num_to_gen = input(
        "Please enter the number of integers to generate from the range:\n\n"
    )
    ranges = input(
        "Please enter the ranges in the following format 1..5,6..10,11..20\n\n"
    )
    rand_num_list = rand_num_list_gen(num=int(num_to_gen))

    print("The count in the given ranges is:\n")

if __name__ == "__main__":
    main()
    # advanced_main()
```

## Advanced

You should now write your code in the ``advanced_main()`` function.

To test your code you should update the last three lines as follows:

```python
if __name__ == "__main__":
  # main()
  advanced_main()
```

The above program that you wrote in ``main()`` is acceptable for a first attempt. 

However, you should try modifying your program so that you can easily change the number of integers generated and the ranges of valid numbers (for example, the ranges could be changed to be 1..6, 7..12, 13..31, 32..50 or any other set of ranges). For example we might have overlapping ranges 1..30, 1..50.

To do this, you could use two lists to store the upper and lower bound of each of the ranges. You could also use a dictionary, or a list of lists, or a list of tuples.

Your program should work as follows:

```
Please enter the number of integers to generate between 1 and 50.:
100

Please enter the ranges in the following format: 
e.g. 1..5,6..10,11..20,21..30,31..40,41..50
1..20,21..30,31..45,46..50

The count in the given ranges is:
1..20: 45
21..30: 20
31..45: 25
46..50: 10
```

Here all 100 numbers are taken care of as our bins cover the whole range 1 - 50. There also do not overlap!

```
Please enter the number of integers to generate between 1 and 50.:
200

Please enter the ranges in the following format: 
e.g. 1..5,6..10,11..20,21..30,31..40,41..50
1..30,1..50

The count in the given ranges is:
1..30: 117
1..50: 200
```

Here all 200 numbers will be in the range 1..50, but only 117 fall within the range 1..30. In fact our ranges overlap. To pass the advanced test your code will need to work for both cases.

To simplify things do not worry about invalid input. In the case of invalid input your program should just fail.