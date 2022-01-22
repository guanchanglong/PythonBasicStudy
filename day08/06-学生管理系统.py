stu_list = []

def show_menu():
    print('1、添加学生信息')
    print('2、删除学生信息')
    print('3、修改学生信息')
    print('4、查询学生信息')
    print('5、退出系统')


def insert_student():
    name = input('请输入学生名字：')
    age = input('请输入学生年龄：')
    sex = input('请输入学生性别：')
    stu_dict = {'name': name, 'age': age, 'sex': sex}
    stu_list.append(stu_dict)
    print('======学生信息添加成功======')


def show_all_info():
    if len(stu_list):
        for student in stu_list:
            print(f'姓名：{student["name"]}, 年龄：{student["age"]}, 性别：{student["sex"]}')
    else:
        print('目前没有学生信息')


while True:
    show_menu()
    opt = input('请输入用来选择的操作编号：')
    if opt == '1':
        insert_student()
    elif opt == '2':
        print('2、删除学生信息')
    elif opt == '3':
        print('3、修改学生信息')
    elif opt == '4':
        show_all_info()
        # print('4、查询学生信息')
    elif opt == '5':
        print('5、退出系统')
        break
    else:
        print('输入有误，请再次输入')
        continue
    input('......输入回车键继续......')






















