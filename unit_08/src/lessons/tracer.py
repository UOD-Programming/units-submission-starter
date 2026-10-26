from functools import wraps

def trace(func):
  trace.recursion_depth = 0

  @wraps(func)
  def traced_func(*args, **kwargs):
    trace.recursion_depth += 1
    print(f"Entering recursive call {trace.recursion_depth}")
    result = func(*args, **kwargs)
    print(f"Exiting recursive call {trace.recursion_depth}")
    trace.recursion_depth -= 1
    return result

  return traced_func