#!/user/bin/python3.5
#encoding: utf-8

user_list = {}
tpl = '|{:>10}|{:>10}|{:>15}|{:>10}'
keys = ('name','age','tel','passwd')
header = tpl.format(keys[0],keys[1],keys[2],keys[3])

fhandler = open('user.txt','rt')
for line in fhandler:
    name,age,tel,passwd = line.strip().split(':')
    user_list[name] = {'name':name,'age':age,'tel':tel,'passwd':passwd}
fhandler.close()

COUNT = 0
for i in range(3):
    name = input('请输入用户名:')
    passwd = input('请输入密码:')
    for line in user_list.values():
        if name == line['name'] and passwd == line['passwd']:
            COUNT = 1
            break
    if COUNT == 1:
        break


if COUNT == 0:
    print('用户名密码输错3次，请重新登录。')
else:
    while True:
        ACTION = input('请输入你需要的操作(find/dict/add/delete/update/exit): ')
        ACTION = ACTION.strip()
        if ACTION == 'add':
            user_text = input('请输入用户信息(用户名:年龄:联系方式:密码)：')
            user_text = user_text.strip()
            user_dict = dict(zip(keys,user_text.split(':')))
            user_name = user_dict.get('name')
            if user_name in user_list:
                print('用户已存在')
            else:
                user_list[user_name] = user_dict
                print('添加成功')


        elif ACTION == 'delete':
            name = input('请输入需要删除的用户名:')
            if user_list.pop(name.strip(),None):
                print('已删除')
            else:
                print('用户不存在')


        elif ACTION == 'update':
            user_text = input('请输入用户信息(用户名:年龄:联系方式:密码)：')
            user_text = user_text.strip()
            user_dict = dict(zip(keys,user_text.split(':')))
            user_name = user_dict.get('name')
            if user_name in user_list:
                user_list[user_name] = user_dict
                print('已更新')
            else:
                print('用户不存在')


        elif ACTION == 'find':
            name = input('请输入需要查找的用户名:')
            name = name.strip()
            if name in user_list:
                print(header)
                print(tpl.format(user_list[name]['name'],user_list[name]['age'],user_list[name]['tel'],'*' * len(user_list[name]['passwd'])))
            else:
                print('用户不存在')


        elif ACTION == 'dict':
            print(header)
            for i in user_list:
                print(tpl.format(user_list[i]['name'],user_list[i]['age'],user_list[i]['tel'],'*' * len(user_list[i]['passwd'])))


        elif ACTION == 'exit':
            fhandler = open('user.txt','wt')
            for line in user_list.values():
                fhandler.write('{0}:{1}:{2}:{3}\n'.format(line['name'],line['age'],line['tel'],line['passwd']))
            fhandler.close()
            print('退出')
            break

        else:
            print('命令错误')







