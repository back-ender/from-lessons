# name = 'Lebron'
# for smb in name:
#     print(smb)  #L
#                  e
#                  b
#                  r
#                  o
#                  n

# mix = ('23', 'LA', 2.3)
# for different in mix:
#     print(different) #23
#                       LA
#                       2.3


# numbers = (4, 6, '6')
# for nums in numbers:
#     print(nums+2)  #6
#                     8
#                     Error
#                         Because: can only concatenate str (not "int") to str


# *range() - number of iterations

# for smt in range(1, 20):
#     print(smt) #from 1
#                 to 19


# numbers = (2, 4, '6')
# for nums in range(1, 100):
#      print(f'{numbers}')  #(2, 4, '6')
#                            repeats 99 times



# clients = ['Lebron', 'Andy', 'Jordan']
# for smb in range(0, 20):
#     if 'Lebron' in clients:
#         print('Lebron is on the list')
#     else:
#         print('not found')  #Lebron is on the list
#                              repeats 20 times



# names = ['Lebron', 'Andy', 'Jordan']
# for smb in range(0, 20):
#     for name in names:
#         print(names)   #['Lebron', 'Andy', 'Jordan']
#                         repeats 20 times


# spam = 'Hello world'
#
# while spam == 'Hello world':
#     print(spam) #Hello world   (spamming endlessly)
#                   ..........



# different = [1, 2, 'no', 'yes']
#
# while 'yes' in different:
#     different.append('All correct')
#     print(different)


# different = [1, 2, 'no', 'yes']
# while len(different) < 5:
#     different.append('different less than 5')
#     print(different)


# Technical task: Customer registrar

# names = ['Lebron', 'Andy', 'Jordan', 'Koby']
#
# while True:
#     add = input('add name: ')
#     if add == 'list':
#         print(names)
#     else:
#         names.append(all)
#         print(f'{add} added')
#
#
# phone_numbers = ['999999999', '888888888', '777777777']
#
# while True:
#     add = input('add number: ')
#     if add == 'list':
#         print(phone_numbers)
#     else:
#         phone_numbers.append(add)
#         print(f'{add} added')
#
#
# servis = ['nurse', 'dentist', 'traumatologist']
#
# while True:
#     add = input('add servis: ')
#     if add == 'list':
#         print(servis)
#     else:
#         servis.append(add)
#         print(f'{add} added')
#
#     for all in range():



# name = []
# phone_number = []
# servis = []
#
# while True:
#     user = input('What you gonna do?: name, phone number, sevis\n ')
#     if user == 'name':
#         add = input('what is your name?\n')
#         name.append(add)
#         print(name)
#     elif user == 'phone number':
#         add = input('what is your telephone number?\n')
#         phone_number.append(add)
#         print(phone_number)
#     elif user == 'servis':
#         add = input('what servis do you provide?\n')
#         servis.append(add)
#         print(servis)
#     elif user == 'list':
#         print(name, phone_number, servis)

