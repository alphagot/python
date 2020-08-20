# __author:  xiaoxinpro13
# date:  2020/8/19

def outer():
    x = 10

    def inner():
        print(x)

    return inner


outer()()

f = outer()
f()

