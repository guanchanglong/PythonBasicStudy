# 向列表添加数据的方法
# 向列表中添加数据的方法，都是直接在原列表中进行添加的，不会返回新的列表
my_list = ['小明', '小红', '小金', '筱筱']
print(my_list)
# 列表.append(数据)  向列表的尾部追加数据
my_list.append('小黄')
print(my_list)
result = my_list.append(12)  # 返回空
print(result)  # None
print(my_list)
# 列表.insert(下标, 数据)  在指定的下标位置进行添加数据
my_list.insert(0, '小花')
print(my_list)
my_list.insert(5, 3.14)
print(my_list)
# 列表.extend(可迭代对象)  会将可迭代对象中的数据逐个添加到原列表的末尾
my_list.extend('hello')
print(my_list)
my_list.extend([1, 'python', 3.14])
print(my_list)

# 列表中的数据查询操作
my_list1 = [1, 3.14, 'hello', True, False]
# index()  根据数据值查找元素所在的下标，找到返回元素的下标，没有找到，程序报错
print(my_list1.index(3.14))  # 1
# print(my_list1.index(1000)) 程序报错，列表中不存在该数据
# count()  统计出现的次数
# 这里要注意，布尔类型在这里会被当成整数来对待，所以结果是2
print(my_list1.count(1))  # 2
print(my_list1.count(0))  # 1
# in / not in  判断是否存在，存在是True，不存在时False
flag = 3.14 in my_list1  # True
print(flag)
flag = 1 not in my_list1  # Flase
print(flag)

# 列表的删除操作
my_list2 = [1, 3, 4, 5, 8, 12]
# 1、根据元素的数据值删除 remove()，直接删除原列表中的数据，删除不存在的数据会报错
my_list2.remove(4)
print(my_list2)  # [1, 3, 5, 8, 12]

# 2、根据下标删除
# 2.1、pop()默认删除最后一个数据，返回删除的内容
num = my_list2.pop()  # 删除最后一个数据
print(num)
print(my_list2)

num = my_list2.pop(2)
print(num)
print(my_list2)

# 2.2、del 列表[下标]
# 删除不存在的下标会报错
del my_list2[1]
print(my_list2)


