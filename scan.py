import git

"""
клонирование репозитория с помощью библиотеки GitPython
"""
try:
    git.Git('/Ping2').clone('https://github.com/Zoltens/ping1.git')
except:
    pass

"""
Единственное что я смог придумать со своими знаниями.
При это прекрасно понимаю, что данное решение очень далеко от правильного.
Здесь я просто перебираю код на запрещенные слова и  символы и вывожу их.
При этом, если будет многострочный запрос,то будет показана только часть этого запроса, а не весь.
Конечно можно было использовать готовые решения, но думаю это тоже было бы неправильно
"""
def scan_sql(file):
    forbid_var = ['format', 'f"', '+', '%s']
    with open(file) as f:
        for i in f.readlines():
            for j in forbid_var:
                if j in i:
                    print(i)


scan_sql('./ping1/main.py')
scan_sql('./ping1/main2.py')
scan_sql('./ping1/main3.py')
