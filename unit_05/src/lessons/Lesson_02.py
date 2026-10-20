
def reverse(str_to_reverse):
    raise NotImplementedError("You have not implemented the reverse function")

def get_character(string_one, i):
    raise NotImplementedError("You have not implemented the get_character function")

if __name__ == "__main__":
    print(reverse("This is a string")) # prints "gnirts a si sihT"
    print(reverse("Hello World")) # prints "dlroW olleH"
    print(get_character("This is a string", 3)) # prints "i"
    print(get_character("Hello World", 5)) # prints "o"