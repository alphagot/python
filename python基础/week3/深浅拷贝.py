# __author:  xiaoxinpro13
# date:  2020/8/11
import copy

s = [[1, 2], "Tom", "Alic"]

s2 = s

s3 = s.copy()#浅copy

print(s)
print(s2)
print(s3)

a = 1
a2 = a
a = 3
print(a, a2)

s3[0][1] = 100
print(s)
print(s2)
print(s3)

s[2] = "abc"
print(s)
print(s2)
print(s3)

s4 = copy.deepcopy(s)#深copy
s[0][1] = 22
print('------------', s4, s)
