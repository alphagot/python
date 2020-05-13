# 计算1-100的和
# range(101)-->1-100
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = [x + x for x in a]
print(sum)
