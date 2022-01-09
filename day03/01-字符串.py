# 单引号
# name = '小明'
# print(type(name), name)

# 双引号
# name = "小明"
# print(type(name), name)

# 三引号
# my_str = """hello world"""
# print(type(my_str), my_str)

# 可以使用转移字符来表示输出单双引号
# my_str = "\'"
# print(my_str)

# Python 中可以使用乘号来表示输出多少个字符
# my_str = '&' * 5
# print(my_str)  # &&&&&

# 字符串的输入和输出
# 输入
# my_str = input('输入字符串：')
# print(type(my_str), my_str)

# 输出
# print(f"刚刚输入的字符串为：{my_str}")

# 索引下标
# 下标可以是正数，也可以是负数
# 正数下标从0开始，负数下标最后一个字符是-1，往前依次递减
my_str = 'hello'
print(my_str[0])  # h
print(my_str[-1])  # o
print(my_str[-5])  # h

# 使用 len() 获取字符串长度
print(len(my_str))

