# Find the Bugs 1

Copy the following program in **Exercise_05.py**.

```python
# This program converts a numeric grade to an alpha grade

input_bool = False

while not input_bool: 
  input_grade = int(input("Please enter the grade you wish to convert (0-100).\n"))
  if (input_grade >= 0) or (input_grade <= 100):
    input_bool = True

  print("ERROR: input not between 0 and 100\n")

output_grade = ""
if input_grade <= 35:
  output_grade = "F"
elif input_grade <= 40:
  output_grade = "MF"
elif input_grade <= 50:
  output_grade = "D"
elif input_grade <= 60:
  output_grade = "C"
elif input_grade <= 70:
  output_grade = "B"
elif input_grade <= 80:
  output_grade = "A-"
elif input_grade <= 90:
  output_grade = "A"
else:
  output_grade = "A+"

print(f"{input_grade} = {output_grade}.")
```

This program contains a number of bugs (errors). Note we use a ``while`` loop here which we will cover in unit 4, but exposure to this now will help.

The program should convert a whole number grade between ``0`` and ``100``.

Conversion is given by:

|Numeric | Alpha |
|---|---|
| 0 - 34 | F (Fail) |
| 35 - 39 | MF (Marginal Fail) |
| 40 - 49 | D|
| 50 - 59 | C |
| 60 - 69 | B |
| 70 - 79 | A- |
| 80 - 89 | A |
| 90 - 100 | A+ |


The following two examples show the current output for ``35`` and ``47``.

```
Please enter the grade you wish to convert (0-100).
35
ERROR: input not between 0 and 100

35 = F.
```

```
Please enter the grade you wish to convert (0-100).
47
ERROR: input not between 0 and 100

47 = D.
```

These should output:

```
Please enter the grade you wish to convert (0-100).
35
35 = MF.
```

```
Please enter the grade you wish to convert (0-100).
47
47 = D.
```

---

A number below ``0`` or above ``100`` should result in an error and ask the user for the input again.

For example:
```
Please enter the grade you wish to convert (0-100).
-10
ERROR: input not between 0 and 100

Please enter the grade you wish to convert (0-100).
2
2 = F.
```

Debug the program and fix the bugs so that it works as detailed above.

You should use the tests as a guide to help you debug the program.

Normally debugging requires that you understand what the program will do under a given set of inputs (circumstances).

As a start, why not run the program and enter some values? Try to see what the program is doing at the moment. Then work out what you need to fix.

Now would also be a great time to start using the debugger. If you aren't sure how then ask in the practical sessions.

You can read about the debugger in VS Code here - [https://code.visualstudio.com/Docs/editor/debugging](https://code.visualstudio.com/Docs/editor/debugging)

Or you can use [Python Tutor](https://pythontutor.com/)