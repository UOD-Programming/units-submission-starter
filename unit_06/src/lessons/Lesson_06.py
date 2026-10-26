def sum_div_3(n):
    """you should update div_by_3_list to generate the list of numbers divisible by 3 and return their sum.

    e.g. for n = 10 it should look at 1,2,3,4,5,6,7,8,9,10 and the list should contain [3,6,9]. The function should then return the sum of this list, in this case 18"""
    div_by_3_list = []
    return sum(div_by_3_list)


if __name__ == "__main__":
    print(sum_div_3(10))  # should print 18
    print(sum_div_3(12))  # should print 30
    print(sum_div_3(100))  # should print 1683