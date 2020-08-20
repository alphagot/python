# __author:  xiaoxinpro13
# date:  2020/8/19

def outer():
    x = 10

    def inner():  # 条件1 inner就是内部函数

        print(x)  # 条件2 外部环境的一个变量

    return inner  # 结论：内部函数inner就是一个闭包


outer()()

f = outer()
f()

# 高阶函数
# 1.函数名可以作为参数输入
# 2.函数名可以作为返回值

# 闭包
# 闭包=函数块+定义函数是的环境
