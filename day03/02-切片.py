# 切片是指对操作对象截取其中一部分的操作。字符串、列表、元组都支持切片操作
# 切片操作会生成新的对象
# 切片语法：变量[start:end:step]
# start：开始位置的下标
# end：结束位置的下标，不包含end对应下标
# step：步长，默认为1或者-1
my_str = 'hello'
my_str1 = my_str[2:5:1]  # llo
print(my_str1)

# step 如果是1，即默认值，可以不写
my_str2 = my_str[2:5]  # llo
print(my_str2)

# end 位置不写，表示是len()，即可以取到最后一个元素
my_str3 = my_str[3:]  # lo
print(my_str3)

# start 位置也可以省略不写，表示从0开始
my_str4 = my_str[:3]  # hel
print(my_str4)

# start和end都不写，但是冒号还是需要写
my_str5 = my_str[:]  # hello
print(my_str5)

print(my_str[-4:-1])
# 步长也可以是负数
print(my_str[3:1:-1])  # ll

# 字符串的逆置
print(my_str[::-1])  # olleh
