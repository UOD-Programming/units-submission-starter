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