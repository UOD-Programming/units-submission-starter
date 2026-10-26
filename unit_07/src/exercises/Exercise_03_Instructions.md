# Exercise 7.3

Using the ``random`` module create a coin toss simulation that lets the user simulate ``n`` coin tosses. 

Your program should then print out the number of coin tosses that are heads and the number that are tails. It should also print the percentage of heads seen and tails seen. 

You should generate your coin tosses using the function coin_tosses which accepts n and returns a list of ``0``s and ``1``s. 

You should:

- Use the count function to generate the count as a tuple.
- Use the percentage function to generate the percentage as a tuple.
- Round your percentages to the nearest whole number.

## The Main Function

``main()`` should use these functions to run a coin toss simulation for the user.

For example,

```
How many coin tosses would you like to simulate?
15

No. of Heads: 8
No. of Tails: 7

%   of Heads: 53
%   of Tails: 47
```

```
How many coin tosses would you like to simulate?
333

No. of Heads: 159
No. of Tails: 174

%   of Heads: 47.75
%   of Tails: 52.25
```

## The Coin Tosses Function

The ``coin_tosses`` function should take in a number ``n`` and return a random list of ``0``s and ``1``s.

For example,

```python
tosses = coin_tosses(11)
print(tosses)
```
may print out:

```
[0,1,1,0,0,1,0,1,0,1,0]
```

## The Count Function

```python
tosses = [0,1,1,0,0,1,0,1,0,1,0]
count_tosses = count(tosses)
print(count_tosses)
```
would print out:

```
(5,6)
```

## The Percentage Function

```python
count_tosses = (5,6)
percentage_tosses = percentage(count_tosses)
print(percentage_tosses)
```
would print out:

```
(45.45, 54.55)
```

## Getting Started

Copy and paste the following code into ``Exercise_03.py`` to get started.

```python
def coin_tosses(n):
  pass

def count(tosses):
  pass

def percentage(count_of_tosses):
  pass

def main():
  x = input("How many coin tosses would you like to simulate?\n")
  
if __name__ == "__main__":
  main()
```