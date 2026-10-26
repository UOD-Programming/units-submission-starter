# Lists  

Make sure you have read the lesson first - [Lists](https://samtoneill.github.io/programming_in_python/unit_6/lists.html)

*** 
# === TASK ===

Copy the following into ``Lesson_01.py`` to get started.

```python
def longest_word(string_list):
    pass # placeholder, delete and replace with your code
  
def num_characters(string_list):
    pass # placeholder, delete and replace with your code
  
if __name__ == "__main__":
    test_string = [["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]
    test_string2 = [["Hello", "World"], ["Apple", "Pears"]]
    print(longest_word(test_string)) # should print revolution
    print(num_characters(test_string)) # should print 105
    print(longest_word(test_string2)) # should print hello
    print(num_characters(test_string2)) # should print 20
```

The first function is called ``longest_word`` which takes in a list of a list of strings and returns the longest word in any of the lists. In the case of equal length words, return the first word you encounter. In the case of no words, e.g. an empty list ``[]`` return ``None``.

For example:

```python
longest_word([["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]) # return revolution
```

The second is called ``num_characters`` which takes in a list of a list of strings and returns the total number of characters in all of the strings in the list lists.

```python
num_characters([["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]) # return 105
```

***

# References 

[Python List Methods - W3schools](https://www.w3schools.com/python/python_lists_methods.asp)