# Lambda Functions, Map and Filter

Make sure you have read the lesson first - [Lambda Functions, Map and Filter](https://samtoneill.github.io/programming_in_python/unit_8/lambda_functions,_map_and_filter.html)

***
# === TASK ===
For a list of strings, filter out the strings that are odd in length and then reverse each of these strings and return the resulting list.
 
You can reverse a string using:

```python
str_one = "test"
print(str_one[::-1])
```

A function has been created for you that takes a string and returns a reversed string.

You should update the ``task_answer()`` function so that it returns the correct list.

Copy and paste the following into ``Lesson_03.py`` to get started.

```python
def reverse_string(str_to_reverse):
  return str_to_reverse[::-1]

def task_answer(string_list):
  """ you should filter out odd length strings and reverse these here.
  
  return the result as a list """
  pass

if __name__ == "__main__":
  str_list = ["this", "IS", "a", "list", "of", "a", "few", "strings"]
  result = task_answer(str_list)
  print(result) # should print ['a', 'a', 'wef', 'sgnirts']
```
***