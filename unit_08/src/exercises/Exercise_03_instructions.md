# Exercise 8.3 :sunglasses:

***To view this correctly it either view on GitHub or you can install the following extension in VS Code - [Markdown Emoji](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-emoji).***

***p.s. it is also looks really nice when rendered properly!***

Capman :sunglasses: has a sweet tooth and is very fond of sweets.

Capman starts at the top left of a grid and can only move right and down. Help Capman collect as the best combination of sweets possible as he moves to the bottom left of the grid.

There are three types of sweet, these are given in the table below:

| Sweet | Emoji | Worth |
| -- | -- | -- |
| Chocolate | :chocolate_bar: | 1 |
| Candy | :candy: | 2 |
| Lollipop | :lollipop: | 3 |


## Example 1

:sunglasses: --- &nbsp;:chocolate_bar: --- :white_circle: --- :white_circle: --- :white_circle:<br>
&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :lollipop: --- :white_circle: --- :white_circle: --- :white_circle:<br>&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :candy: --- :candy: --- :white_circle: --- :white_circle:<br>&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :lollipop: --- &nbsp;&nbsp;:chocolate_bar: --- :white_circle: --- :candy:<br>&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :white_circle: --- :white_circle: --- :white_circle: --- :red_circle:<br>

Here the best path is clearly :chocolate_bar: -:lollipop: - :candy: - :lollipop: - :chocolate_bar: - :white_circle: - :candy: - :red_circle:. This is worth ``1 + 3 + 2 + 3 + 1 + 0 + 2 = 12``.

The data structure to represent a grid is a dictionary that contains the size of the grid and the co-ordinate points of the sweets and their value.

To understand the co-ordinates, in the above example Capman starts in position ``(0,0)`` and finishes in position ``(4,4)``. The :chocolate_bar: to Capman's right is in position ``(1,0)``.

For the above example here is the full dictionary. The grid is a 5 by 5 grid.

```python
grid = {
  "size": (5,5),
  (1,0): 1,
  (1,1): 3,
  (1,2): 2,
  (1,3): 3,
  (2,2): 2,
  (2,3): 1,
  (4,2): 2
}
```

## Example 2

For example,

:sunglasses: --- &nbsp;:chocolate_bar: --- :candy: --- :white_circle: --- :white_circle:<br>
&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :lollipop:  --- :lollipop: --- :lollipop: --- :lollipop:<br>&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :candy: --- :candy: --- :white_circle: --- :white_circle:<br>&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :white_circle: --- &nbsp;&nbsp;:chocolate_bar: --- :white_circle: --- :candy:<br>&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :white_circle: --- :white_circle: --- :white_circle: --- :white_circle:<br>&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>:white_circle: --- :lollipop: --- :white_circle: --- :candy: --- :red_circle:

Here the best path is clearly :chocolate_bar: - :lollipop: - :lollipop: - :lollipop: - :lollipop: - :white_circle: - :candy: - :white_circle: - :red_circle:. This is worth ``1 + 3 + 3 + 3 + 3 + 0 + 2 + 0 = 15``.

```python
grid = {
  "size": (5,6),
  (1,0): 1,
  (1,1): 3,
  (1,2): 2,
  (1,5): 3,
  (2,0): 2,
  (2,1): 3,
  (2,2): 2,
  (2,3): 1,
  (3,1): 3,
  (3,5): 2,
  (4,1): 3,
  (4,3): 2
}
```

# === TASK ===

You should write a function called ``find_best_path()`` that finds the best combination of sweets (path) and returns the value of the sweets (path).

There are many ways to do this, some are very inefficient. You can use either recursion or loops, but recursion is quite elegant for this problem.

You will see two tests. One tests that you generate the right answer, the other tests whether you have done this relatively efficiently (under 1 second). 

I have also included two templates below, one is for the iterative (loop) method, the other is the recursive method. You are free to choose which you use, I prefer recursion for this problem.

The tests test the method ``find_best_path()``, so as long as that function takes in a grid and returns the value of the best path it will pass the tests.

For the examples above:

```python
grid = {
  "size": (5,5),
  (1,0): 1,
  (1,1): 3,
  (1,2): 2,
  (1,3): 3,
  (2,2): 2,
  (2,3): 1,
  (4,2): 2
}
find_best_path(grid) # returns 12
```
```python
grid = {
  "size": (5,6),
  (1,0): 1,
  (1,1): 3,
  (1,2): 2,
  (1,5): 3,
  (2,0): 2,
  (2,1): 3,
  (2,2): 2,
  (2,3): 1,
  (3,1): 3,
  (3,5): 2,
  (4,1): 3,
  (4,3): 2
}
find_best_path(grid) # returns 15
```

### Extra Thought :bulb:

You should consider why this would be problematic if Capman could move in any direction!

## Iterative Template

Copy and paste this into ``Lesson_03.py`` to get started.

```python
import timeit

def find_best_path(grid):
  pass
  
if __name__ == "__main__":
  grid = {
    "size": (5,5),
    (1,0): 1,
    (1,1): 3,
    (1,2): 2,
    (1,3): 3,
    (2,2): 2,
    (2,3): 1,
    (4,3): 2
  }
  print(find_best_path(grid)) # should print 12

  grid = {
    "size": (5,6),
    (1,0): 1,
    (1,1): 3,
    (1,2): 2,
    (1,5): 3,
    (2,0): 2,
    (2,1): 3,
    (2,2): 2,
    (2,3): 1,
    (3,1): 3,
    (3,5): 2,
    (4,1): 3,
    (4,3): 2
  }
  
  print(find_best_path(grid)) # should print 15

  # efficiency test
  # ---------------
  # uncomment the code below to test with a 100 by 100 grid (uncomment a selection using Ctrl + r on windows or Cmd + r on a Mac)
  # this should complete in a fraction of a second, to pass the test you will need it to complete in less that 1 second

  # grid = {
  #   "size": (99,99),
  #   (1,0): 1,
  #   (1,1): 3,
  #   (1,2): 2,
  #   (1,5): 3,
  #   (2,0): 2,
  #   (2,1): 3,
  #   (2,2): 2,
  #   (2,3): 1,
  #   (3,1): 3,
  #   (3,5): 2,
  #   (4,1): 3,
  #   (4,3): 2,
  #   (98,98): 3
  # }
  # start_time = timeit.default_timer()
  # print(find_best_path(grid)) # should return and print 18
  # end_time = timeit.default_timer()

  # time_taken = end_time - start_time
  # print(time_taken)
```

## Recursion Template

Copy and paste this into ``Lesson_03.py`` to get started.

```python
import timeit

# This just calls the recursive method to start it
def find_best_path(grid):
  return find_best_path_rec(grid["size"][0] - 1, grid["size"][1] - 1, grid)

# recursive method
def find_best_path_rec(x, y, grid):
  pass

if __name__ == "__main__":
  grid = {
    "size": (5,5),
    (1,0): 1,
    (1,1): 3,
    (1,2): 2,
    (1,3): 3,
    (2,2): 2,
    (2,3): 1,
    (4,3): 2
  }
  print(find_best_path(grid)) # should return 12

  grid = {
    "size": (5,6),
    (1,0): 1,
    (1,1): 3,
    (1,2): 2,
    (1,5): 3,
    (2,0): 2,
    (2,1): 3,
    (2,2): 2,
    (2,3): 1,
    (3,1): 3,
    (3,5): 2,
    (4,1): 3,
    (4,3): 2
  }
  
  print(find_best_path(grid)) # should return 15
  
  # efficiency test
  # ---------------
  # uncomment the code below to test with a 100 by 100 grid (uncomment a selection using Ctrl + r on windows or Cmd + r on a Mac)
  # this should complete in a fraction of a second, to pass the test you will need it to complete in less that 1 second

  # grid = {
  #   "size": (99,99),
  #   (1,0): 1,
  #   (1,1): 3,
  #   (1,2): 2,
  #   (1,5): 3,
  #   (2,0): 2,
  #   (2,1): 3,
  #   (2,2): 2,
  #   (2,3): 1,
  #   (3,1): 3,
  #   (3,5): 2,
  #   (4,1): 3,
  #   (4,3): 2,
  #   (98,98): 3
  # }
  # start_time = timeit.default_timer()
  # print(find_best_path(grid)) # should return and print 18
  # end_time = timeit.default_timer()

  # time_taken = end_time - start_time
  # print(time_taken)
```