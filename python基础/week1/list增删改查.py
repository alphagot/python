# __author:  xiaoxinpro13
# date:  2020/7/28

list_name = ['xiaoming', 'xiaohua', 'xiaozhang']
# 增删改查
# 查  切片（另外，元组只能切片查找和删除不能增改）

print(list_name[0])

print(list_name[1:3])  # 从下标1取到3的前一个值

print(list_name[1:-1])  # 从下标1取到第二个值

print(list_name[-2::1])  # 从倒数第二值取到最后

print(list_name[0::2])  # 从下标0取间隔值

print(list_name[-1::-2])

# 增 添加 append insert
list_name.append('xiaoli')  # 默认添加到列表最后

print(list_name)

list_name.insert(2, "xiaozhao")  # 插入到列表下标2的位置

print(list_name)

# 改
list_name[0] = 'xiaohu'

print(list_name)

list_name[0:2] = ["heh", 'hah']  # 修改list_name的0到1的值

print(list_name)

# 删 remove pop del
list_name.remove("hah")  # 删除具体的值
# list_name.remove(list_name[0])
print(list_name)

name = list_name.pop(0)  # 索引删除
print(list_name, name)

del list_name[0]
print(list_name)

del list_name  # 删除列表
