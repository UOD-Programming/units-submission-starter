def and_many(*args):
  pass


def or_many(*args):
  pass


if __name__ == "__main__":
  print(and_many(True))  # prints True
  print(and_many(True, True))  # prints True
  print(and_many(True, True, True))  # prints True
  print(and_many(True, True, True, True))  # prints True
  print(and_many(False, True))  # prints False
  print(and_many(True, False, True))  # prints False
  print(and_many(True, True, True, False))  # prints False

  print(or_many(True))  # prints True
  print(or_many(False, True))  # prints True
  print(or_many(True, False, True))  # prints True
  print(or_many(True, True, True, False))  # prints True
  print(or_many(False))  # prints False
  print(or_many(False, False))  # prints False
  print(or_many(False, False, False))  # prints False
  print(or_many(False, False, False, False))  # prints False