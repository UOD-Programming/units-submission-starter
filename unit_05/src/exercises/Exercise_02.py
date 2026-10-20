def convert_temp():
  pass

if __name__ == "__main__":
    # I would comment some of these out as you build up parts of convert_temp
    # e.g. just start by getting convert_temp(20) to work
    print(convert_temp(20)) # Prints 68.0
    print(convert_temp(-10)) # Prints 14.0
    print(convert_temp(68, Fahrenheit=True)) # Prints 20.0
    print(convert_temp(-100, Fahrenheit=True)) # Prints -73.33
    print(convert_temp(-300)) # ValueError("Temperature below absolute zero is invalid for Celsius.")
    print(convert_temp(-500, Fahrenheit=True)) # ValueError("Temperature below absolute zero is invalid for Fahrenheit.")
