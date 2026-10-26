# Recursion 101

Make sure you have read the lesson first - [Recursion 101](https://samtoneill.github.io/programming_in_python/unit_8/recursion_101.html)

***
# ===TASK ===
Create the functions ``string_list_concat()`` and ``string_list_concat_with_space()`` so that it takes a list of strings as input and concatenates (joins) them into one string as per the function docstring.

**YOUR FUNCTION SHOULD USE RECURSION AND USE THE MINIMAL AMOUNT OF RECURSIVE CALLS**.

HINT: Section 2 on summing numbers is an excellent place to start. You should consider how this task is similar to the recursive program given in Section 2.

Copy and paste the following into ``Lesson_04.py`` to get started.

```python
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
```
***
