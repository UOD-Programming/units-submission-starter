# Exercise 5.5

You will find the following code in ``Exercise_05.py``. 

```python
import random

def get_user_guess():
    """ gets the user input"""
    # remove the following line and write the function here
    pass

def print_feedback(no_guesses, max_guesses, secret_num):
    """ prints the end feedback """
    # remove the following line and write the function here
    pass

def main():
    secret_num = random.randint(1, 10)
    keep_going = True
    max_guesses = 3
    no_guesses = 0

    while keep_going:
        if no_guesses < max_guesses:
            guess = get_user_guess()
            if guess == "q":
                keep_going = False
            else:
                if int(guess) == secret_num:
                    keep_going = False
                else:
                    print("Incorrect, please try again\n")
        else:
            keep_going = False

        no_guesses += 1

    if guess == "q":
        print("User exited the program.")
    else:
        print_feedback(no_guesses, max_guesses, secret_num)



if __name__ == "__main__":
    # call the main() function to run the whole program
    main()
    
    # Uncomment any of these lines to test the functions on their own. You will probably want to comment out the call to main() as well.
    
    #get_user_guess()
    # print_feedback(2, 3, 5) # should print Well done, you used 2/3 guesses to guess the secret number 5.
    # print_feedback(4, 3, 6) # should print Sorry, better luck next time.
```

This is a version of the number guessing game. The difference here is that we now use two functions for two parts of our code.

The code in the function ``main()`` will work correctly if you implement the functions ``get_user_guess()`` and ``print_feedback()`` correctly.

``get_user_guess()`` is responsible for asking the user for a number between ``1`` and ``10``. It should return a string that is either a number between ``"1"`` and ``"10"`` or the character ``"q"``. For all other inputs it should ask the user for input again by outputting ``Invalid input: Please enter a whole number between 1 and 10 or q to quit``

``print_feedback()`` is responsible for printing out the feedback at the end of the game and has two possible scenarios. 

1. If the ``no_guesses`` is greater than the ``max_guesses`` then the user didn't win and it should print ``Sorry, better luck next time.``
2. If the ``no_guesses`` is less than or equal to the ``max_guesses`` then the user won, so it should print ``Well done, you used num_guesses/max_guesses guesses to guess the secret number secret_num.``
   <br><br>
   e.g. ``Well done, you used 2/3 guesses to guess the secret number 5.``

You can test the functions by calling them at the bottom of the code. You will see a few lines at the bottom that are commented out. Uncomment these to test the functions on their own.

Here are three complete outputs for the program that you can use to check your program is working as expected.

```
Please enter a whole number between 1 and 10 or q to quit
11
Invalid input

Please enter a whole number between 1 and 10 or q to quit
3
Incorrect, please try again

Please enter a whole number between 1 and 10 or q to quit
5
Well done, you used 2/3 guesses to guess the secret number 5.
```

```
Please enter a whole number between 1 and 10 or q to quit
hello
Invalid input

Please enter a whole number between 1 and 10 or q to quit
q
User exited the program.
```

```
Please enter a whole number between 1 and 10 or q to quit
1
Incorrect, please try again

Please enter a whole number between 1 and 10 or q to quit
2
Incorrect, please try again

Please enter a whole number between 1 and 10 or q to quit
3
Incorrect, please try again

Sorry, better luck next time.
```
