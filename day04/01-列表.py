# 列表是Python中的一种数据类型，可以存放多个数据，列表中的数据可以是任意类型的
# 列表(list)，定义使用[]定义

# 定义空列表
my_list = []
print(my_list, type(my_list))  # [] <class 'list'>
my_list1 = list()
print(my_list1, type(my_list1))  # [] <class 'list'>

# 定义带数据的列表，数据元素之间使用逗号隔开
my_list2 = [1, 3.14, True, 'hello']
print(my_list2, type(my_list2))  # [1, 3.14, True, 'hello'] <class 'list'>

# 求列表中数据元素的个数，即列表的长度
num = len(my_list2)
print(num)  # 4

# 列表支持下标和切片操作
print(my_list2[1])  # 3.14
print(my_list2[-1])  # hello
print(my_list2[1:3])  # [3.14, True]

# 下标操作与字符串中不同的是：字符串不能通过下标修改其中的数据，但是列表可以使用下标修改列表中的数据
my_list2[0] = 18
print(my_list2)  # [18, 3.14, True, 'hello']
my_list2[-1] = 3.3
print(my_list2)  # [18, 3.14, True, 3.3]





