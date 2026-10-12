# Find the Bugs 2  
The program below has a number of bugs. Note that there are better ways to do this program, but this is an exercise in debugging and seeing if you can fix the program.

The program should take in a comma-separated list of strings and then let the user know the minimum length, maximum length, and average length.

For the input ``the,quick,brown,fox,jumped,over,the,lazy,dog`` the program should work as follows,
```
Please enter a list of strings separated by a comma.
e.g. one,two,three,four,five

the,quick,brown,fox,jumped,over,the,lazy,dog
The minimum length of a string is 3
The maximum length of a string is 6
The average length of the strings in the list is 4.0
```

Copy the following code into ``Exercise_06.py``.

```python
# Do not touch this line
input_list = list(input("Please enter a list of strings separated by a comma.\ne.g. one,two,three,four,five\n\n").split(','))

min_index = 1
max_index = 1
total = 0

i = 2

while i < len(input_list):
  total += len(input_list[i])
  if len(input_list[i]) < len(input_list[max_index]):
    max_index = i

  if len(input_list[i]) len(input_list[min_index]):
    min_index = i
  i+= 1

print(f"The minimum length of a string is {len(input_list[max_index])}")
print(f"The maximum length of a string is {len(input_list[max_index])}")
print(f"The average length of the strings in the list is {total/len(input_list):.2f}")
```

***
# === TASK ===
Fix the program so that it correctly prints out as the example and passes the tests. There are a number of bugs!

## Tips
1. You should try and understand what the code is doing. Yes, there are bugs, but it still has a structure and is almost correct.
2. Try a few sets of input that you know the answer to. Can you spot anything obvious? You could use the tests for this.
3. Print out some of the variables, maybe in the output, you can spot what is wrong.
4. Use the debugger to inspect your code.

**This might be a frustrating exercise, but that is sort of the point. Debugging code can be unbelievably frustrating, but it is a critical skill to becoming a good programmer.**
***
