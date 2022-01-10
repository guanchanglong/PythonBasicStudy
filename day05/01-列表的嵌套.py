school_name = [['北京大学', '清华大学'],
               ['南开大学', '天津大学', '广西大学'],
               ['山东大学', '中国海洋大学']]
print(school_name[1])  # ['南开大学', '天津大学', '广西大学']
print(school_name[1][1])  # 天津大学

for shcools in school_name:
    for name in shcools:
        print(name)

