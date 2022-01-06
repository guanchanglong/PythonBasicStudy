# for i in 'hello':
#     # i 一次循环是字符串中的一个字符
#     print(i)


# range(n) 会生成[0,n)的数据序列，不包含n
# for i in range(5):
#     print(i)

# range(a,b) 会生成[a,b)的整数序,不包含b
# for i in range(3, 7):
#     print(i)

# range(a,b,step)会生成[a,b)的整数序列，但是每个数字之间的间隔(步长)是step
# for i in range(1, 10, 3):
#     print(i)

# break 和 continue
for i in range(1, 6):
    if i == 3:
        print('发现半条虫子，这个苹果不吃了，没吃饱，继续吃剩下的')
        continue
    if i == 4:
        print('吃饱了')
        break  # 终止循环的执行
    print(f'正在吃编号为{i}的苹果')
