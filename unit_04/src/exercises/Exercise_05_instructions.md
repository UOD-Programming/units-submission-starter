# Exercise 4.5

Earlier we saw the [Number Guessing Game](https://samtoneill.github.io/programming_in_python/unit_4/the_number_guessing_game.html).

## 1. Number Guessing Game

The basic program in Python is given below.

```python
# The Number Guessing Game 
import random

# randomly generate a number between 1 and 10
secret_guess = random.randint(1,10)

print("Welcome to the Number Guessing Game!")
print("You need to try and guess the number between 1 and 10...")
print("If you wish to exit the game enter 0...")

guess = int(input("Please enter a guess:\n"))

while guess != secret_guess:
  print("That is not correct, please try again.")
  guess = int(input("Please enter a guess:\n"))

print(f"Well done the correct answer was {secret_guess}")
```

This program generates a random number and then asks the user to input a guess.

The guess is then tested in the ``while`` condition and if it is not the correct number we repeat the step. If it is the correct number we exit the ``while``.

## 2. Adding Better Feedback

If you try the program above you will get pretty frustrated by the lack of feedback. 

To improve the game we can let the user know if there guess is too low or to high. 

We can also keep track of the number of guesses made.

The basic pseudocode for this program is:

```
welcome the player to the game and explain it
pick a random number between 1 and 100
get a guess from the player
set the number of guesses to 1

while the player’s guess does not equal the secret number
    if the guess is greater than the number
        tell the player to guess lower
    else
        tell the player to guess higher
    get a new guess from the player
    increase the number of guesses by 1
    
congratulate the player on guessing the number
let the player know how many guesses it took
```

## 3. Allowing the User to Exit

Imagine that we change the game to be a number between 1 and 1000.

It would then be useful if the user could exit the game. We can add this in by updating the ``while`` condition to:

```
while (player’s guess does not equal the secret number) and (guess not equal to 0)
```

Now if the user enters ``0`` the program will exit.

***
# === TASK ===

Make the changes outlined in Section 2 and Section 3 to the basic program outlined in Section 1.

To pass the tests please comment out the line,
```python
secret_guess = random.randint(1,10)
```
and add the following line.
```python
# randomly generate a number between 1 and 10
#secret_guess = random.randint(1,10)
secret_guess = 3
```
Otherwise the random number generated will cause your output to differ to the tests.

Examples of how the program should run for a ``secret_guess = 3`` are given below:

```
Welcome to the Number Guessing Game!
You need to try and guess the number between 1 and 10...

If you wish to exit the game enter 0...

Please enter a guess:
2
Your guess is too low, please try again.
Please enter a guess:
5
Your guess is too high, please try again.
Please enter a guess:
3
Well done the correct answer was 3
You took 3 guesses.
```
```
Welcome to the Number Guessing Game!
You need to try and guess the number between 1 and 10...

If you wish to exit the game enter 0...

Please enter a guess:
0
Program exited. The correct answer was 3
```
```
Welcome to the Number Guessing Game!
You need to try and guess the number between 1 and 10...

If you wish to exit the game enter 0...

Please enter a guess:
2
Your guess is too low, please try again.
0
Program exited. The correct answer was 3
```

***NOTE that your output must exactly match the output expected for the tests.***

***
  
