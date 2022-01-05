# 类型转换，将原始数据转换成我们需要的数据类型
# price = input('请输入苹果的价格：')
# weight = input('请输入重量：')
# result = float(price) * float(weight)  # 类型转换
# print(f'苹果单价为{price}元/斤，购买了{weight}斤，需要支付{result}元')

# 转换为int类型
# float转换为int
pi = 3.54
# 注意：这里的类型转换是直接取整数部分，不管小数部分
num = int(pi)
print(num)  # 输出：3

# 函数eval() ：将字符串还原成原来的数据类型，去掉字符串的引号
num2 = eval('100')
print(type(num2))  # <class 'int'>
num3 = eval('3.14')
print(type(num3))  # <class 'float'>

type1 = eval('True')
print(type(type1))  # <class 'bool'>

# 注意：如果字符串去掉引号之后的值是变量名的话就会输出那个变量
# 如果不是变量名，也不是其他类型的话，直接报错
type2 = eval('type1')
print(type(type2))
