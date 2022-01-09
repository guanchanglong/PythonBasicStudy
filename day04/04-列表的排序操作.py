# 要想对列表中的数据进行排序操作，前提是列表中的数据类型都是一样的
my_list = [1, 5, 7, 4, 2, 3, 1]

# 列表.sort() 直接在原列表中进行排序
# my_list.sort() 默认是从小到大的升序排序
# my_list.sort()
# print(my_list)

# 通过reverse = True 进行降序排序
# my_list.sort(reverse=True)
# print(my_list)

# sorted(列表) 排序，不会再原列表中进行排序，会得到一个新的列表
my_list1 = sorted(my_list)  # 升序
my_list2 = sorted(my_list, reverse=True)  # 降序
print(my_list1)
print(my_list2)




