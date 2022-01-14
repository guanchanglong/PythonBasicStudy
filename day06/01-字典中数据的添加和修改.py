my_dict = {'name': '小明'}

# 字典中添加和修改数据，使用key值进行修改和修改
# 字典[key] = 数据值;    如果key值存在，就是修改，如果key值不存在，就是添加

my_dict['age'] = 18  # key值不存在，添加
print(my_dict)

my_dict['age'] = 20  # key值已经存在，就是修改数据
print(my_dict)

# 注意：key值int的1和float的1.0代表一个key值
my_dict[1] = 'int'
print(my_dict)  # {'name': '小明', 'age': 20, 1: 'int'}
my_dict[1.0] = 'float'
print(my_dict)  # {'name': '小明', 'age': 20, 1: 'float'}




