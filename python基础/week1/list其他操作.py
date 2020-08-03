# __author:  xiaoxinpro13
# date:  2020/7/30

a = ['de', 'of', 'de', 'to', 'for', 'in', 'on', 'up', 'on']

# count 出现次数
print(a.count('of'))

# index 查找位置
print(a.index('for'))

first_de = a.index('de')

small_a = a[first_de + 1:]

second_de = small_a.index('de') + 1

print(a[first_de], a[second_de])

# reverse 位置反向存取

a.reverse()
print(a)

# sort 排序
b = [1, 21, 4, 34, 5, 78, 53, 12]
b.sort(reverse=True)
print(b)
# b.reverse()
# print(b)

# 身份判断

print(type(b) is list)
