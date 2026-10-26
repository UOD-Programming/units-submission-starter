from tracer import trace

@trace
def string_list_concat(string_list):
  """ Concatenates a list of strings into a single string
  eg. ["This", "is", "a", "list", "of", "strings"] 
  returns
  "Thisisalistofstrings"
  """
  pass

@trace
def string_list_concat_with_space(string_list):
  """ Concatenates a list of strings into a single string
  eg. ["This", "is", "a", "list", "of", "strings"] 
  returns
  "This is a list of strings"
  """
  pass

if __name__ == "__main__":
  str_list = ["This", "is", "a", "list", "of", "strings"]
  print(string_list_concat(str_list)) # prints the return value of "Thisisalistofstrings"
  print(string_list_concat_with_space(str_list)) # prints the return value of "This is a list of strings"