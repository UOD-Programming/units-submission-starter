# Exercise 6.1

The following exercise requires you to write the function ``find_max_row()`` which should take in a list of lists, e.g. ``[[1,2,3],[4,2,1],[4,5,4]]`` that represent a grid of numbers.

```
[1, 2, 3]
[4, 2, 1]
[4, 5, 4]
```

The function should calculate which row has the largest sum of it's items.

For the example above we have,

```
[1, 2, 3]  - Sums to 6
[4, 2, 1]  - Sums to 9
[4, 5, 4]  - Sums to 13
```
clearly the last row is the largest.

Rows are to be labelled from 1. So,

```
[1, 2, 3]  - Row 1
[4, 2, 1]  - Row 2
[4, 5, 4]  - Row 3
```

The function should return which row has the largest sum, so in this example the function should return ``3``.

## 1. Equal Rows

If two or more rows are equal it should return the first row.

For example, for the input ``[[1,2,3],[3,2,1],[2,1,3],[2,2,2]]`` all rows are equal, the function should return the first row that has the largest sum, i.e. ``1``.

## 2. Different Sized Rows

If the rows are of different sizes, your function should still work.

For example, for the input ``[[1,2,3],[3],[2,1,3,4]]`` the rows are of different sizes, the function should return the last row, i.e. ``3``, as it has the largest sum.

***
# === TASK ===
Write the function ``find_max_row()`` so that it does the above.

Copy the following code into ``Exercise_01.py`` to get started.

```python
def find_max_row(grid):
    # HINT: https://datagy.io/python-index-of-max-item-list/
    pass

def print_grid(grid):
    for row in grid:
        print(row)

if __name__ == "__main__":
    # main
    grid_one = [[1, 2, 3], [4, 2, 1], [4, 5, 4]]
    print_grid(grid_one)
    print(
        f"The maximum row for the grid_one is {find_max_row(grid_one)}"
    )  # should return 3

    print()

    grid_two = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
    print_grid(grid_two)
    print(
        f"The maximum row for the grid_two is {find_max_row(grid_two)}"
    )  # should return 1

    print()

    grid_three = [[1, 2, 3], [3], [2, 1, 3, 4]]
    print_grid(grid_three)
    print(
        f"The maximum row for the grid_three is {find_max_row(grid_three)}"
    )  # should return 3

```