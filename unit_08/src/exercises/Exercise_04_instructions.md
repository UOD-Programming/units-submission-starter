# Exercise 8.4

Copy and paste this into ``Exercise_04.py`` to get started.

```python
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
```

You will see a function called ``base_10_convertor_rec()``.

``base_10_convertor_rec()`` accepts a string of numbers and a base from which to convert to base 10.

For example,

| ``num_string`` | Convert From Base | Answer |
| -- | -- | -- |
| ``"1011"`` | ``2`` | ``11`` |
| ``"1111"`` | ``2`` | ``15`` |
| ``"00341"`` | ``5`` | ``96`` |
| ``"00341"`` | ``6`` | ``133`` |

Amend ``base_10_convertor_rec()`` so that it recursively returns the correct answer.

You will also see that if you are correct, when you call the function.

```python
print(base_10_convertor_rec("1011", 2)) # prints 11
```

it will print out:

```
Entering recursive call 1
Entering recursive call 2
Entering recursive call 3
Entering recursive call 4
Exiting recursive call 4
Exiting recursive call 3
Exiting recursive call 2
Exiting recursive call 1
11
```
This is because if written correctly it will call itself 4 times before returning each of the calls. ``@trace`` is a decorator that will print out each of the recursive calls. For now do not worry about this, it will be explained in the lesson on decorators.

You will note that the length of ``"1011"`` is also 4.

For the following,

```python
print(base_10_convertor_rec("00341", 5)) # prints 96
```

it will print out:

```
Entering recursive call 1
Entering recursive call 2
Entering recursive call 3
Entering recursive call 4
Entering recursive call 5
Exiting recursive call 5
Exiting recursive call 4
Exiting recursive call 3
Exiting recursive call 2
Exiting recursive call 1
96
```
Again notice that it calls itself 5 times and the length of ``"00341"`` is 5.


