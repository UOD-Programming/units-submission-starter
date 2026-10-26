# Serialisation with JSON  

Make sure you have read the lesson first - [Serialisation with JSON](https://samtoneill.github.io/programming_in_python/unit_7/serialisation_with_json.html)

# === TASK ===

This should be a nice easy one.

Create a ``load()`` function that takes in a filename and loads the data stored in the filename.


Copy and paste the following into a new Python file to get started.
```python
import json
def load(filename):
  pass

if __name__ == "__main__":
  print(load("./src/lessons/Lesson_05_items.json"))
```

The contents of ``Lesson_05_items.json`` is below in case you corrupt the file.

```json
{
  "name": "John",
  "age": 30,
  "married": true,
  "divorced": false,
  "children": ["Ann","Billy"],
  "pets": null,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
```

***
