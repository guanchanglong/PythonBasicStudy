my_dict = {'name': '小明', 'age': 20, 1: 'float', 'second': 'hahaha', 'first': 'hello'}

# 根据key值删除数据
# del 字典名[key]
del my_dict[1]
print(my_dict)


# 字典.pop(key) 根据key值删除，返回值是删除的key对应的value值
result = my_dict.pop('age')
print(my_dict)
print(result)

# 字典.clear() 清空字典，删除所有的键值对
my_dict.clear()
print(my_dict)

# del 字典名 直接删除这个字典，不能再使用该字典了
del my_dict  # 后面的代码不能再使用这个变量了，除非再次定义
# print(my_dict)  # 代码报错



