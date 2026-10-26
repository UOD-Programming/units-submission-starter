# Exercise 8.1

The following code is a version of the famous game WORDLE. You can play WORDLE via the following link:

[Wordle](https://www.nytimes.com/games/wordle/index.html)

Our version is called Derble (coded by Brad - PhD Student and now a lecturer elsewhere.).

You need to decompose this program so that it uses the three functions

``validate_input()``

``get_input()``

``check_word()``

Below you will find two programs:

1. Full Program Without Decomposition
2. A Template for Decomposition

## 0. How to Pass the Tests
**Your decomposed program should function exactly as the program without decomposition.**

Three of the tests are for the functions, the fourth tests the whole program contained within ``start_game()``.

You will need to make sure your decomposed output matches exactly that of the program without decomposition. 

You might want to make a new Python file and paste the program without decomposition into it so you can run both programs for comparison.

## 1. Full Program Without Decomposition

This is the full program and doesn't use the functions. You should copy and paste this into ``Exercise_01.py`` or a new Python file and play with it until you understand what it is doing.

You will also need to use this as a reference for the decomposed program.

```python
# Starts the game with a secret word passed as a parameter.
def start_game(secret_word):
  print("Welcome to Derble!")
  print("You have up to 6 attempts to guess the secret word!")
  running = True
  attempts = 0
  guess = ""
  while running:
    guess = input("Please enter your 5 letter guess: ")
    valid_input = False
    while not valid_input:
      passed_tests = True
      if len(guess) != 5:
        passed_tests = False
  
      for char in guess:
        if not char.isalpha():
          passed_tests = False
      
      if not passed_tests:
        print("You must enter a 5 letter word with no symbols or digits.")
        guess = input("Please enter your 5 letter guess: ")
        valid_input = False
      else:
        valid_input = True
    
    attempts += 1

    correct = True
    letter_index = 0
    feedback_string = ""
    while letter_index < 5:
      if guess[letter_index] == secret_word[letter_index]:
        # print in green if in the right place.
        feedback_string += "G"
      else:
        # test if letter in rest of word
        correct = False
        printed = False
        for character in secret_word:
          if guess[letter_index] == character:
            # print yellow if letter is in the word but in wrong position.
            feedback_string += "Y"
            printed = True
            break
        # print out the letter without colour if not found.
        if not printed:
          feedback_string += "*"
  
      letter_index += 1
    print(feedback_string)
    
    if correct:
      running = False
    elif attempts >= 6:
      running = False
    else:
      print(f"Incorrect! You have {6 - attempts} attempts remaining.")

  if correct:
    print(f"Congrats! You took {attempts} attempts.")
  else:
    print(f"The correct word was \"{secret_word}\". Better luck next time.")


if __name__ == "__main__":
  start_game("error")

```

## 2. Getting Started

Copy and paste the following program into ``Exercise_01.py`` to get started.

This is the decomposed program, my advice is to use the previous program as a reference and to try and build up the functionality so that it matches.

Below this program are examples of how the functions should operate to pass the tests. You should then use these functions in the ``start_game()`` function to build up the whole game.

```python
# Determine whether input retrieved from the user is valid.
# Return True if
#   - the word is 5 letters long
#   - the word only contains characters 
def validate_input(user_input):
  pass


# Get a valid input from the user and return this input.
# Should only return inputs that are valid.
# This should keep asking for input until a valid input is entered
def get_input():
  pass


# Test whether the guess entered by the user is the same as the secret word.
# Should return True if the word is completely correct otherwise return False
  
# Should print out the following for each of the letters as it checks them:

# G for any letter that is in the correct place in the word
# Y for any letter which is in the word but in an incorrect position
# * for any letter which is not in the word at all.
# For example, check_word("error", "steer") # returns False and prints out **YYG to the console
def check_word(secret_word, user_guess):
  pass

# Starts the game with a secret word passed as a parameter.
def start_game(secret_word):
  print("Welcome to Derble!")
  pass


if __name__ == "__main__":
  start_game("error")
```

## Examples of ``validate_input()``

```python
validate_input("thinking")     # return False
```
```python
validate_input("think")        # return True
```

```python
print(validate_input("12345")) # return False
```
```python
print(validate_input("Help&")) # return False
```

## Examples of ``get_input()``
Calling:
```python
get_input()
```
Should work as follows:
```
Please enter your 5 letter guess: test
You must enter a 5 letter word with no symbols or digits.
Please enter your 5 letter guess: 12345
You must enter a 5 letter word with no symbols or digits.
Please enter your 5 letter guess: Help&
You must enter a 5 letter word with no symbols or digits.
Please enter your 5 letter guess: earnt
```
And would return the value ``"earnt"``.
## Examples of ``check_word()``

Calling: 
```python
check_word("error", "tests") # returns False
```

Should also print:

```
*Y***
```
Calling: 
```python
check_word("error", "steer") # returns False
```

Should also print:

```
**YYG
```
Calling: 
```python
check_word("error", "arrow") # returns False
```

Should also print:

```
*GGG*
```
Calling: 
```python
check_word("error", "error") # returns True
```

Should also print:

```
GGGGG
```
