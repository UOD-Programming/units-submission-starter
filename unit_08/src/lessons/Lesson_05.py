import timeit

def no_paths(x,y):
  if x == 0 and y == 0:
    return 1
  elif x == 0:
    return no_paths(0, y-1)
  elif y == 0:
    return no_paths(x-1, 0)
  else:
    return no_paths(x-1, y) + no_paths(x, y-1)

def no_paths_memo(x, y, memo):
  pass


if __name__ == "__main__":
  # This times the paths method
  start_time = timeit.default_timer()
  # walk a grid 13 by 13. This takes approximately 2.5 seconds
  print(f"Number of paths for a 13x13 grid is {no_paths(12,12)}")  
  end_time = timeit.default_timer()
  print(f"Time taken: {end_time - start_time}")
  
  # This times the paths_memo method
  start_time = timeit.default_timer()
  # walk a grid 13 by 13. This should take a fraction of a second
  print(f"Number of paths for a 13x13 grid is {no_paths_memo(12,12, {})}")  
  end_time = timeit.default_timer()
  print(f"Time taken: {end_time - start_time}")