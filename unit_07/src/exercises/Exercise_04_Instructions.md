# Exercise 7.4

Write a program that reads in a file and counts the number of each letter in the file. Ignore anything that is not a letter and consider both upper case and lower case 

You should write your program in a function called ``count_letters`` which accepts a single parameter ``filename``.

## Example Output

You should print out the frequency of each of the letters seen as follows:

For the contents of ``Exercise_04_test.txt``:
```
The count of the letters for the file is:

A: 1
T: 1
W: 1
a: 3
c: 1
d: 3
e: 5
f: 2
g: 1
h: 2
i: 7
l: 3
m: 2
n: 3
o: 2
p: 2
s: 6
t: 1
w: 1
```

For the contents of ``Exercise_04_words.txt``:

```
The count of the letters for the file is:

A: 2
C: 4
D: 5
E: 1
F: 2
I: 3
L: 1
M: 6
N: 4
P: 7
Q: 1
S: 3
U: 1
V: 2
a: 164
b: 26
c: 87
d: 52
e: 251
f: 20
g: 40
h: 7
i: 171
j: 1
l: 123
m: 84
n: 130
o: 84
p: 40
q: 26
r: 94
s: 144
t: 141
u: 153
v: 25
x: 5
```

## Getting Started

Copy and paste the following into ``Exercise_04.py``.

```python
def count_letters(filename):
  pass

if __name__ == "__main__":
  count_letters("./src/exercises/Exercise_04_words.txt")
```

## Hint

It is the **Modules and Files** unit, you may want to search the internet to see if there is a module that might help you with the counting.