a = list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6]))
b = tuple(filter(lambda x: x % 2 == 1, (1, 2, 3, 4, 5, 6)))
c = ["a", "b", "c"]
d = [1, 2, 3]
dic = dict(zip(c, d))

print(a, b, dic)
