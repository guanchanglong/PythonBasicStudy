# 对象 + 对象 支持字符串、列表、元组进行操作，得到一个新的容器
my_list = ['name', '小明', 'age', 18]
my_list = my_list + my_list
print(my_list)

# 对象 * 整数 复制，支持字符串、列表、元组进行操作，得到一个新的容器
my_str = 'hahaha'
my_str1 = my_str * 10
print(my_str1)

# in/not in 判断存在或是不存在，支持字符串、列表、元组、字典进行操作，注意：如果是字典的话，判断是key值是否存在或不存在
print('ha' in my_str)  # True

# Python内置函数
my_dict = {'b': 10, 'a': 20, 'c': 30}
# 1、len(item) 返回容器中元素个数
print(len(my_dict))

# 2、max(item) 返回容器中元素的最大值，对于字典来说，比较的是字典key值的大小
print(max(my_dict))

# 3、min(item) 返回容器中元素的最小值，对于字典来说，比较的是字典key值的大小
print(min(my_dict))

# 4、del(item) 删除变量











