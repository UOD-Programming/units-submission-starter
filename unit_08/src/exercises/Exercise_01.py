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