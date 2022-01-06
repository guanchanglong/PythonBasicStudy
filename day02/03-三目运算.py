a = eval(input('请输入一个数字：'))
b = eval(input('请输入一个数字：'))
# 三目判断，这个三目判断看着有点绕，最好不要使用
result = a - b if a > b else b - a
print(result)
