# 字典(dict)是键值对的形式，类似于map的形式
# 变量 = {key1:value1, key2:value2} 一个键值对算是一个元素
# 字典的key可以是字符串类型和数字类型，不能是列表
# value值可以是任何类型

# 1、定义空字典
my_dict = {}
my_dict1 = dict()
print(my_dict, type(my_dict))    # {} <class 'dict'>
print(my_dict1, type(my_dict1))  # {} <class 'dict'>

# 2、定义带数据的字典
my_dict2 = {'name': '小明', 'age': 18, 'like': ['学习', '游戏'], 1: [2, 3.14, 8]}

# 3、访问value值，在字典中没有下标的概念，使用key值访问对应的value值
print(my_dict2['age'])  # 18
print(my_dict2['like'][1])  # 游戏

# 4、如果key值不存在
# print(my_dict2['hello'])  # 会报错
print(my_dict2.get('hello'))  # 不会报错，但是会返回None

# 字典.get(key, 数据值) 如果key存在，返回可以对应的value值，如果key不存在，返回书写的数据值
print(my_dict2.get('hello', 'haha'))
print(my_dict2.get('age', '年龄不存在'))



