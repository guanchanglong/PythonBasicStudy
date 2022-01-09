# my_str.replace(old_str,new_str,count) 字符串的替换
# old_str:将要被替换的字符串
# new_str:新的字符串，替换成的字符串
# count:替换的次数，默认是全部替换
# 返回值:得到一个新的字符串，不会改变原来的字符串

my_str = 'F:/Code/GithubRepository/PythonBasicStudy/day03/04-字符串的替换.py'
my_str1 = my_str.replace('day03', 'day04')  # F:/Code/GithubRepository/PythonBasicStudy/day04/04-字符串的替换.py
print(my_str1)

print(my_str.replace('o', '1', 5))  # F:/C1de/GithubRep1sit1ry/Pyth1nBasicStudy/day03/04-字符串的替换.py

# 就算替换的次数超过了字符串出现的次数，也不会报错，而是能替换多少个就替换多少个
print(my_str.replace('0', '5', 5))  # F:/Code/GithubRepository/PythonBasicStudy/day53/54-字符串的替换.py



