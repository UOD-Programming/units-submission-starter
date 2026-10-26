# Address Book Exercise
def look_up(add_book, name):
    """returns the corresponding address (value) for name (key)"""
    pass

def add(add_book, name, address):
    """adds a name/address (key/value) to the address book"""
    pass

def edit(add_book, name, new_address):
    """edits the address entry for name (key) with a new address (value)"""
    pass

def delete(add_book, name):
    """deletes name (key) and the address (value) from the addressbook"""
    pass

def list_all(add_book):
    """prints out all the addresses

    e.g.

    address_book = {
      "Sam": "MS308, Markeaton St, Derby",
      "Sherlock": "221B Baker Street, London"
    }

    would print out:

    Name: Sam
    Address: MS308, Markeaton St, Derby

    Name: Sherlock
    Address: 221B Baker Street, London

    Make sure you include a new line after the address.
    """
    pass

def main():
    # define empty address book
    address_book = {}

    choice = None
    while choice != "0":
        print(
            """Address Book
0 - Quit
1 - Look Up an Address
2 - Add an Address
3 - Edit an Address
4 - Delete an Address
5 - List Addresses
"""
        )
        choice = input("Choice: ")
        print()
        # exit
        if choice == "0":
            print("Good-bye.")
            # get an address
        elif choice == "1":
            look_up_name = input("Please enter a name to look up their address:\n")
            if look_up_name in address_book:
                address = look_up(address_book, look_up_name)
                print(address)
            else:
                print(f"ERROR: No entry for {look_up_name} found.\n")
        # add a name-address pair
        elif choice == "2":
            name_to_add = input("Please enter a name you wish to add:\n")
            if name_to_add not in address_book:
                address = input("What's the address?: ")
                add(address_book, name_to_add, address)
                print(f"\n{name_to_add} has been added.\n")
            else:
                print("ERROR: Name already exists.\n")
        # change an existing address
        elif choice == "3":
            name_to_edit = input(
                "Please enter the name of the address you wish to edit: "
            )
            if name_to_edit in address_book:
                new_address = input("What's the new address?: ")
                edit(address_book, name_to_edit, new_address)
                print("\nAddress for ", name_to_edit, " has been edited.\n")
            else:
                print(f"\n{name_to_edit} is not in the address book.\n")
            # delete a name-addres pair
        elif choice == "4":
            name_to_del = input("What term do you want me to delete?: ")
            if name_to_del in address_book:
                delete(address_book, name_to_del)
                print(f"\nOkay, I deleted {name_to_del}\n")
            else:
                print(
                    f"\nI can't do that! {name_to_del} doesn't exist in the address book.\n"
                )
        elif choice == "5":
            list_all(address_book)
        else:
            print(f"Sorry, but {choice} isn't a valid choice.\n")

if __name__ == "__main__":
    main()