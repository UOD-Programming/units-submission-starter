def logger(func):
    # write your code here
    return func

@logger
def funky_func(x, y, z=1):
    print(x)
    print(y)
    print(z)

@logger
def add_three(x, y, z):
    print(x + y + z)

@logger
def hello():
    print("hello")

@logger
def keyword(a=1, b=2, c=3):
    print(a + b + c)

if __name__ == "__main__":
    funky_func(3, 4, z=10)
    print()
    funky_func(3, 4)
    print()
    add_three(3, 4, 5)
    print()
    hello()
    print()
    keyword()