# Decomposition and Abstraction

Make sure you have read the lesson first - [Decomposition and Abstraction](https://samtoneill.github.io/programming_in_python/unit_8/decomposition_and_abstraction.html)

***
# === TASK ===

Rewrite the code below so that it uses the functions specified in the remainder of the TASK.
```python
# main program
# list of strings
str_list = ["ABBA", "snake", "Peep", "this", "kayak"]
pal_list = []
for s in str_list:
  lower_s = s.lower()
  if len(lower_s) > 1:
    is_pal = True
    start_index = 0
    end_index = len(lower_s) - 1
    while start_index <= end_index and is_pal:
      if not lower_s[start_index] == lower_s[end_index]:
        is_pal = False
      start_index += 1
      end_index -= 1

    if is_pal:
      pal_list.append(s)

print(pal_list) # prints ['ABBA', 'Peep', 'kayak']
```

You will note that there are specifications written for each of the functions.

When decomposed properly, your main program should just be 3 lines long.

Copy the following into ``Lesson_01.py`` to get started. You can always delete the docstrings to make it easier to read your code.

```python
def is_palindrome(s):
  """ Tests if a string is a palindrome, ignore upper/lower case

  e.g. ABBA returns True
  AbBa returns True
  snake returns False

  Parameters
  ----------
  s: str
    String to test as palindrome

  Returns
  -------
  bool:
    Return True if s in a palindrome; False otherwise.
  """
  pass

def filter_palindromes(items):
  """ Filters a list for palindromes.

  e.g. ["ABBA", "snake", "Peep", "this"] returns ["ABBA", "Peep"]

  Parameters
  ----------
  items: list
    List of strings.

  Returns
  -------
  list:
    Filtered list of palindromes
  """
  pass

if __name__ == "__main__":
  # main program when decomposed
  str_list = ["ABBA", "snake", "Peep", "this"]
  pal_list = filter_palindromes(str_list)
  print(pal_list) # prints ['ABBA', 'Peep']
```

HINT: You should be calling the ``is_palindrome()`` function from inside the ``filter_palindromes()`` function.

***


# References

[1] Guttag, J.V. (2021) Introduction to Computation and Programming Using Python, third edition: With Application to Computational Modeling. The MIT Press.

[2] https://cs.stanford.edu/people/nick/py/python-style-decomposition.html