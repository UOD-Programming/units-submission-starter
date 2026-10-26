# Writing to Files

Make sure you have read the lesson first - [Writing to Files](https://samtoneill.github.io/programming_in_python/unit_7/writing_to_files.html)

# === TASK ===

Write a function called ``write_nums()`` that outputs the first positive n numbers to a txt file called ``Lesson_04_nums.txt``

For example,

```python
write_nums(10)
```
Should output the first 10 numbers to the file ``Lesson_04_nums.txt``. Remember you will need to use the relative path. ``./src/lessons/Lesson_04_nums.txt``.

```
1
2
3
4
5
6
7
8
9
10
```

Copy and paste this code into ``Lesson_04.py``

```python
def write_nums(n):
  pass

if __name__ == "__main__":
  write_nums(10) 
  # writes out the first 10 positive numbers to nums.txt
```