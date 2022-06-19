#переменные
# name = 'Temur'
# age = 22
# print(name, age)
#
# name, age = 'Темур', 22
# print(name, age)
#
# name=age= 'Temur 22'
# print(name)

#Ввод
#vvod = input('Введите текст: ')
#print(vvod)



# england = 'liverpool'
# number_of_players = 11
# state = 0.25
# print(england, number_of_players, state)

#Условные операторы
# a = int(input('write number: '))
# if a >100:
#     print('a is greater than 100')
# elif a <100:
#     print('a is smaller than 100')
# else:
#     print('a is 100')

#1й проект(1st project)

first_number =int(input('Введите число: '))
action = input('Введите оператор: ')
second_number = int(input('Введите число: '))

if action == '+':
    print(first_number + second_number)
elif action == '-':
    print(first_number-second_number)
elif action == '*':
    print(first_number*second_number)
elif action == '/':
    print(first_number/second_number)
else:
    print('in process')

