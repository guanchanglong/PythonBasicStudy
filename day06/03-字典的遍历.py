my_dict = {'name': '小明', 'age': '18','sex': '男'}

# for循环直接遍历字典，遍历的是字典的key值
for key in my_dict:
    print(key, my_dict[key])

# 字典.keys() 获取字典中所有的key值，得到的类型是dict_keys，该类型具有的特点是
# 1、可以使用list()进行类型转换，即将其转换为列表类型
# 2、可以使用for循环遍历
result = my_dict.keys()
print(result, type(result))
for key in result:
    print(key)

# 字典.values() 获取所有的value值，类型是dict_values
result = my_dict.values()
print(result, type(result))
for value in my_dict.values():
    print(value)

# 字典.items() 获取所有的键值对，类型是dict_items，(key,value)组成元组类型
# 1、可以使用list()进行类型转换，即将其转换为列表类型
# 2、可以使用for循环遍历
result = my_dict.items()
print(result, type(result))
for item in my_dict.items():
    print(item[0], item[1])

for key,value in my_dict.items():
    print(key, value)
