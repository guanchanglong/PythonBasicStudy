# if语句的使用
# age = input('请输入你的年龄：')
# age = eval(age)
# if age >= 18:
#     print('可以进入网吧')
# else:
#     print('禁止未成年人进入网吧')

# elif的使用
# score = input('请输入你的成绩：')
# score = eval(score)
# if score >= 90:
#     print('优秀')
# elif (score >= 80) and score < 90:
#     print('良好')
# elif score >= 60:
#     print('及格')
# else:
#     print('不及格')

# 判断条件的嵌套
money = eval(input('请输入你拥有的零钱：'))
if money >= 2:
    print('我上车了')
    seat = eval(input('车上的空位个数：'))
    if seat >= 1:
        print('有座位坐')
    else:
        print('没有座位，只能站着')
else:
    print('没钱，只能走路')
