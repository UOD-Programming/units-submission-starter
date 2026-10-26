def is_palindrome(s):
    """ Tests if a string is a palindrome, ignore upper/lower case

  e.g. ABBA returns True
  AbBa returns True
  snake returns False

  Parameters
  ----------
  s: str
    String to test as palindrome

  Returns
  -------
  bool:
    Return True if s in a palindrome; False otherwise.
  """
    pass


def filter_palindromes(items):
    """ Filters a list for palindromes.

  e.g. ["ABBA", "snake", "Peep", "this"] returns ["ABBA", "Peep"]

  Parameters
  ----------
  items: list
    List of strings.

  Returns
  -------
  list:
    Filtered list of palindromes
  """
    pass


if __name__ == "__main__":
    # main program when decomposed
    str_list = ["ABBA", "snake", "Peep", "this"]
    pal_list = filter_palindromes(str_list)
    print(pal_list)  # prints ['ABBA', 'Peep']
