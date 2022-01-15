def func1(a, b):
    c = a + b
    d = a - b
    # return [c, d]  # 返回列表
    return c, d  # 默认是组成元组进行返回的，即(c, d)


result = func1(20, 10)
print(f"a+b的结果是{result[0]},a-b的结果是{result[1]}")
