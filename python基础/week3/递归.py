# __author:  xiaoxinpro13
# date:  2020/8/19

def func(n):
    if n == 1:
        return 1
    return n * func(n - 1)


print(func(5))


# 关于递归的特性：
# 1.调用自身函数
# 2.有一个结束条件


# 0 1 1 2 3 5 8 13 21 34
def fibo(n):
    before = 0
    after = 1
    if n == 0:
        return before
    for i in range(1, n):
        bflag = before
        before = after
        after = bflag + before

    return after


print(fibo(5))


def fibo1(n):
    if n == 0 or n == 1:
        return n

    return (fibo1(n - 1) + fibo1(n - 2))


print(fibo1(5))


