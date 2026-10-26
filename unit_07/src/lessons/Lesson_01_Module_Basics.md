# Module Basics

Make sure you have read the lesson first - [Module Basics](https://samtoneill.github.io/programming_in_python/unit_7/module_basics.html)


# === TASK ===
Import the ``os`` module 

Amend the function ``get_current_working_directory()`` so that it returns the current working directory as a string.

HINT: Search for "current working directory" on the following URL - [Python Docs - os Module](https://docs.python.org/3/library/os.html#module-os)

Implement the functions ``encode_string()`` and ``decode_string()`` using the ``base64`` module so that they encode and decode a string using base64.

You can find out more via the following URLs. You will be required to read at least one of these links to implement the functions.

[Base64 Encoding](https://www.python-engineer.com/posts/base64-module/)

[Encoding and Decoding Base64 Strings in Python - G4G](https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/#:~:text=In%20Python%20the%20base64%20module,strings%20isn%27t%20base64%20characters.)

Copy and paste this into ``Lesson_01.py`` to get started.

```python
def get_current_working_directory():
  pass

def encode_string(str_to_encode):
  """ Encodes a string using base64"""
  pass

def decode_string(base64_str_to_decode):
  """ Decodes a string encoded in base64"""
  pass
  

if __name__ == "__main__":
  print(get_current_working_directory())
  print(encode_string("Python is a cool programming language!"))
  # should print UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE=
  str_to_decode = "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE="
  print(decode_string(str_to_decode))
  # should print Python is a cool programming language!
```
***

# References 

[1. Python Docs - Built-in Modules][1]

[2. W3schools - Python Built-in Modules][2]

[3. Matplotlib - Plotting Library][3]

[4. Numpy][4]

[1]: <https://docs.python.org/3/py-modindex.html> "Python Docs - Built-in Modules"

[2]: <https://www.w3schools.com/python/python_ref_functions.asp> "W3schools - Python Built-in Modules"

[3]: <https://matplotlib.org/> "Matplotlib - Plotting Library"

[4]: <https://numpy.org/> "Numpy - The fundamental package for scientific computing with Python"