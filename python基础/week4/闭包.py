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

# 高阶函数
# 1.函数名可以作为参数输入
# 2.函数名可以作为返回值

# 闭包
