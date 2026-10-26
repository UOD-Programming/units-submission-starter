#  Exercise 7.5

Write a program that reads in a square grid of numbers and find the largest ``n`` digit number that occurs left-to-right

## Load Grid Function

The ``load_grid()`` function takes a filename, reads the contents of the file and returns the square grid as a list of lists.

```python
filename = "Exercise_05_grid_5_by_5.txt"
grid = load_grid(filename)
# returns [[8, 3, 6, 8, 9], [8, 4, 4, 5, 1], [9, 1, 2, 3, 2], [2, 7, 5, 6, 7], [7, 7, 1, 3, 3]]
```

## Print Grid Function
There is a ``print_grid()`` function that will take a list of lists representing a grid containing either strings or numbers. This will help you visualise the grid. 

```python
grid = [[1, 2], [3, 4]]
print_grid(grid)
```

```
1  2

3  4
```

## Max Number in Rows Function

The ``max_num_in_rows()`` function takes in a square grid of numbers as a list of lists and the number of digits ``n`` to search for. 

It should find the maximum n-digit number. Here is an example for the following grid.

```
8  3  6  8  9  

8  4  4  5  1  

9  1  2  3  2  

2  7  5  6  7  

7  7  1  3  3
```
The function should work as follows:
```python
# grid stored in Exercise_05_grid_5_by_5.txt
grid = [[8, 3, 6, 8, 9], [8, 4, 4, 5, 1], [9, 1, 2, 3, 2], [2, 7, 5, 6, 7], [7, 7, 1, 3, 3]]
print(max_num_in_rows(grid, 2))  # prints 91
print(max_num_in_rows(grid, 3))  # prints 912
print(max_num_in_rows(grid, 4))  # prints 9123
```

## Advanced

The ``max_num_adv()`` function is similar to the ``max_num_in_rows()`` function but should find the largest n-digit number that occurs either:

- left-to-right
- top-to-bottom
- diagonally top-left-to-bottom-right
- diagonally bottom-left-to-top-right

For the 5x5 grid example,
```
8  3  6  8  9  

8  4  4  5  1  

9  1  2  3  2  

2  7  5  6  7  

7  7  1  3  3 
```

the function should work as follows:
```python
# grid stored in Exercise_05_grid_5_by_5.txt
grid = [[8, 3, 6, 8, 9], [8, 4, 4, 5, 1], [9, 1, 2, 3, 2], [2, 7, 5, 6, 7], [7, 7, 1, 3, 3]]
print(max_num_adv(grid, 2))  # prints 97
print(max_num_adv(grid, 3))  # prints 971
print(max_num_adv(grid, 4))  # prints 9127
```

## Getting Started

Copy and paste the following into ``Exercise_05.py``.

```python
def load_grid(filename):
  pass

def max_num_in_rows(grid, num_digits):
    pass

def max_num_adv(grid, num_digits):
  pass

def print_grid(grid):
  for line in grid:
    for x in line:
      print(f"{x}  ", end="")
    print("\n")

if __name__ == "__main__":
  filename = "./src/exercises/Exercise_05_grid_5_by_5.txt"
  grid = load_grid(filename)
  print_grid(grid)  # print the grid
  print(max_num_in_rows(grid, 3))  # prints 912
  print(max_num_adv(grid, 3))  # prints 971
```

## Checking Your Own Code

You should use the three files given to check your functions:

- ``Exercise_05_grid_3_by_3.txt``
- ``Exercise_05_grid_5_by_5.txt``
- ``Exercise_05_grid_10_by_10.txt``

 I have not provided the correct answers other than those given above, you should work out some example answers that you can then test your functions with.

Running the unit tests will test against a different grid. So your code should work on any square grid.