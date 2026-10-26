def add_from_list(d, items_to_add):
    pass


if __name__ == "__main__":
    test_dict = {
        "a": 1,
        "b": 2
    }
    print(test_dict)  # prints {'a':1, 'b':2}
    items_to_add = [("e", 5), ("z", 26)]
    add_from_list(test_dict, items_to_add)
    print(test_dict)  # prints {'a':1, 'b':2, 'e':5, 'z':26}