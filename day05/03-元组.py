# 元组和列表相似，都可以存放多个数据，可以存放不同数据类型的数据
# 列表中的数据可以修改，元组中的数据不能被修改
my_list = [18, 3.14, True, 'hello']
my_tuple = (18, 3.14, True, 'hello')
print(my_tuple, type(my_tuple))  # (18, 3.14, True, 'hello') <class 'tuple'>

# 元组支持下标和切片操作
print(my_tuple[1])  # 3.14

# 可以定义空元祖，定义空元祖没啥意义
my_tuple1 = ()
print(my_tuple1, type(my_tuple1))  # () <class 'tuple'>

# 定义一个数据元素的元组时需要后面再加一个逗号
my_tuple2 = (3)  # 错误示范
print(my_tuple2, type(my_tuple2))  # 3 <class 'int'>
my_tuple3 = (3,)  # 正确姿势
print(my_tuple3, type(my_tuple3))  # (3,) <class 'tuple'>


