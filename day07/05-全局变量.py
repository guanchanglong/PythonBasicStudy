num = 10
# 1、可以在函数内部访问全局变量
def func1():
    print(num)

# 2、不能在函数内部修改全局变量的值
def func2():
    # num = 200  # 这里并没有修改全局变量的值，而是重新创建了一个局部变量
    # print(num)
    # 想要在函数内部修改全局变量的值，需要使用global关键字声明这个变量为全局变量
    global num
    num = 300



func1()
func2()
print(num)






