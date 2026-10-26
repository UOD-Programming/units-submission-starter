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