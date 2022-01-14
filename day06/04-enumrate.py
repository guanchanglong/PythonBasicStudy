my_list = ['a', 'b', 'c', 'd', 'e']
for i in my_list:
    print(my_list.index(i), i)  # 这样用index的话 列表有重复数据就只会返回第一次出现相同数据的那个下标

# enumerate 将可迭代序列中元素所在的下标和具体元素组合在一起，变成元组
for i in enumerate(my_list):
    print(i)




