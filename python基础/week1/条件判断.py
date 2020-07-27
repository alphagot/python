# 输入用户年龄，根据年龄打印不同的内容。

age = 10
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

state = 'adult' if age >= 18 else "teenager" if age >= 6 else 'kid'
print(state)
