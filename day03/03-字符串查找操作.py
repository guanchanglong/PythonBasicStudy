my_str = 'F:/Code/GithubRepository/PythonBasicStudy/day03/02-切片.py'
# find() 在字符串中查找是否存在某个字符串
# my_str.find(sub_str,start,end)
# sub_str:要在字符串中查找的内容
# start:开始的位置，从哪里开始查找，默认是0
# end:结束的位置，查找到哪里结束，默认是len()
# 返回值:如果找到了sub_str，返回sub_str在my_str中的下标；如果没有找到则返回-1
index = my_str.find('day03')  # 42
print(index)

# 从下标为20的位置，开始查找字符串day03
print(my_str.find('day03', 20))  # 42

# 查找不到返回-1
print(my_str.find('04', 10))  # -1

# 从右边开始查找
print(my_str.rfind('day03'))  # 42

# index() 在字符串中查找是否存在某个字符串
# my_str.index(sub_str,start,end)
# sub_str:要在字符串中查找的内容
# start:开始的位置，从哪里开始查找，默认是0
# end:结束的位置，查找到哪里结束，默认是len()
# 返回值:如果找到了sub_str，返回sub_str在my_str中的下标；如果没有找到会报错
print(my_str.index('day03'))  # 42

# 报错的情况
# print(my_str.index('day04'))  # 报错

# 从右往左查找
print(my_str.rindex('day03', 22))

# count(sub_str,start,end)统计出现的次数
print(my_str.count('a'))  # 2
print(my_str.count('a', 10, 20))  # 0
