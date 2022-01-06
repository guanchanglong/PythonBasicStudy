import random

# 1、用户输入自己出拳的内容
user = eval(input('请输入要出的拳：1(石头) 2(剪刀) 3(布)'))
# 2、电脑随机出拳
computer = random.randint(1, 3)
if user == computer:
    print('平局')
elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print('恭喜你，胜利了')
else:
    print('你输了')
