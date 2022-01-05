# 在 Python 中的输出要使用print函数
# 基本输出
print('hello')

# 一次输出多个内容
print('hello', 18)

# 可以输出表达式
print(1+2)

# 格式化输出，格式化占位符
# %s 字符串
# %d int
# %f float
name = '开心'
print('他的名字是：%s' % name)
print('他的年龄是：%d' % 18)
height = 170.5
# %f 输出默认保留6位小数
print('他的身高是%f cm' % height)  # 他的身高是170.500000 cm
# %.nf 保留n位小数
print('他的身高是%.1f cm' % height)  # 他的身高是170.5 cm
print('他的名字是%s，年龄是%d，身高是%.1f cm' % (name, 18, height))

# 怎么输出%
# 想要输出%号的话得要两个%
print('及格人数占比为%d%%' % 50)

# python3.6版本开始使用f-string，占位统一使用{}占位，填充的数据直接写在{}里面
print(f'他的名字是{name}，他的年龄是{18}，他的身高是{height}cm')

# 转义字符 \n 换行
print('\n哈哈哈')
# 注意：print函数输出之后默认会添加一个换行，如果不想要这个换行可以去掉
# 设置最后是什么内容
# print('hello', end='最后的内容')
print('没有换行', end='')
print('哈哈哈', end='最后的内容')
print('666')
