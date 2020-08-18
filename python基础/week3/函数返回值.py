# __author:  xiaoxinpro13
# date:  2020/8/18
# 1.没有返回值的，函数会返回None 执行return就函数结束了
# 2.如果return多个对象，那么python会把多个对象的返回值封装成一个元组。
def f():
    print('--------------')
    return 1, 1, "aa", (2, 3), [1, 2, 3]


print(f())
