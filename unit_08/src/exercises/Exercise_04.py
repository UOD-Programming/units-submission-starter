from tracer import trace

# do not remove @trace, this will trace the recursive calls
@trace
def base_10_convertor_rec(num_string, convert_from_base):
  pass


if __name__ == "__main__":
  print(base_10_convertor_rec("1011", 2)) # prints 11
  print(base_10_convertor_rec("00341", 5)) # prints 96
  print(base_10_convertor_rec("00341", 6)) # prints 133
  print(base_10_convertor_rec("00341", 10)) # prints 341