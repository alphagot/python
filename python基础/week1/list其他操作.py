# __author:  xiaoxinpro13
# date:  2020/7/30

# index 查找位置

a = ['de', 'of', 'de', 'to', 'for', 'in', 'on', 'up', 'on']

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
b.sort()
print(b)
