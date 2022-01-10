import random

# 1、定义学校列表
schools = [[], [], []]  # 三个小列表就是三个办公室
# 2、定义老师列表
teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
# 3、让老师抓阄
# 3.1、遍历老师列表
for teacher in teachers:
    # 3.2、抓阄，产生随机数
    num = random.randint(0, 2)
    # 3.3、老师进入办公室，将老师名字添加到办公室列表中
    schools[num].append(teacher)

print(schools)
for office in schools:
    print(f'该办公室的老师个数为{len(office)}')
    for teacher in office:
        print(teacher, end=" ")
    print()


