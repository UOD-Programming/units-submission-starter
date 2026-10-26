import random

def rand_num_list_gen(num=100, lower=1, upper=50):
    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list

def main():
    rand_num_list = rand_num_list_gen()
    print("I have generated 100 random numbers between 1 and 50.")
    pass

def advanced_main():
    num_to_gen = input(
        "Please enter the number of integers to generate from the range:\n\n"
    )
    ranges = input(
        "Please enter the ranges in the following format 1..5,6..10,11..20\n\n"
    )
    rand_num_list = rand_num_list_gen(num=int(num_to_gen))

    print("The count in the given ranges is:\n")

if __name__ == "__main__":
    main()
    # advanced_main()