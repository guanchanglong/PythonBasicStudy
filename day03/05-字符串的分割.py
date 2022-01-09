my_str = 'F:/Code/GithubRepository/PythonBasicStudy/day03/05-字符串的分割.py'

# my_str.split(sub_str,count) 将my_str字符串按照sub_str进行切割
# sub_str:按照什么内容切割字符串，默认是空白字符，空格，tab键
# count:切割几次，默认是全部切割
# 返回值:列表[]

result = my_str.split('/')
print(result)

# 从右往左进行一次切割
print(my_str.rsplit('/', 1))


