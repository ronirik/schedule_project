# git

# sudo apt install git - установка гита
# git init - запуск
# it remote and origin git@github.com:ronirik/schedule_project.git - привязка
# git remote -v - проверка 
# git pull origin main - скачиваю себе файлы 
# git branch name - оздать новую ветку имя для нее 
# git branch -v  - проверить ветки 
# git checkout Roman - перейти в  папку
# git add . - прохождения процедуры упаковка моркировка отправка всех изменений 
# git commit -m 'name Schedule project'
# git push origin name -опубликовать

# def func():
#     flag = True
#     while flag:


# import csv
# reader_object = csv.reader(file, delimiter = ",")
# with open("classmates.csv", encoding='utf-8') as r_file:
#     file_reader = csv.reader(r_file, delimiter = ",")
    
#     count = 0
   
#     for row in file_reader:
#         if count == 0:            
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:            
#             print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
#         count += 1
#     print(f'Всего в файле {count} строк.')





# FILENAME = "users.csv"
 
# users = [input('name '), input('age ')]
 
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
     
 
# with open(FILENAME, "a", newline="") as file:
#     user = ["Sam", 31]
#     writer = csv.writer(file)
#     writer.writerow(user)


import csv

import time

import schedule

def write_csv():
    name = input('Name ')
    age = input('age ')
    with open('user.csv', 'a') as csv_file:
        write = csv.writer(csv_file, delimiter='/')
        write.writerow(
            (name,age)
        )

    answ = input('Continue? y on n: ')
    if answ == 'y':
        write_csv()
    else:
        print('Stop!')

def mailing():
    with open('user.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n', ' ') for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Cкидки сегодня! {name[0]}')


schedule.every(3).seconds.do(mailing)
while True:
    schedule.run_pending()
    time.sleep(1)


# mailing()