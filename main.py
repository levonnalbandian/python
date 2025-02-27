# for i in range(10):
#     for a in '123456789':
#         print(i,*'*',a, end=' ')
#     print()


# n = int(input('Enter the number: '))
# for i in range(n):
#     for a in range(n):
#         if i == a or n == i + a:
#             print('^', end=' ')
#         else:
#             print('', end=' ')
#     print()

# for i in range(5):
#     print(i, end='')
#     for j in range(5):
#         print(j, end='')
#     print()

# summ = 0
# count = 0
# while True:
#     n = int(input('Enter the number: '))
#     if n == 0:
#         break
#     elif n != 0:
#         summ += n
#         count += 1
# print(summ/count)

# for i in range(5,20, 5):
#     i -= 0.05
#     discount = round((i / 0.4), 2)
#     print('Old price is',discount,'discounted price is',i)

# money = 0
# while True:
#     age = int(input('Enter the age: '))
#     if 3 < age < 12:
#         money += 14
#     elif age > 65:
#         money += 18
#     elif 13 < age < 65:
#         money += 23
#     elif age == '':
#         break
# print(money)

# n = int(input('Enter number count: '))
# for i in range(n):
#     number = int(input('Enter the number: '))
#     a = str(number)

# a = int(input('Enter the number: '))
# for i in range(a):
#     for j in range(i):
#         j *= 2 * a - 1
#         print(j)

# fahrenheit = 1
# for i in range(1):
#     for j in range(10, 101, 10):
#         fahrenheit = (j - 32) / (9/5)
#         print(j,'C = ',fahrenheit,'F')


# total = 0
# while True:
#     p = (input('Enter the price: '))
#     if p == '':
#         break
#     else:
#         total += p
#         p_total = 100 * total
#         p_total % 5
    # print('Your total is',total,'in cent it is',p_total)

# for i in range(6):
#     for j in range(i, 11 + i, 2):
#         print(j, end=' ')
#     print()

# n = int(input('Enter the number:'))
# for i in range(1, n):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()

# l = []
# while True:
#     t = input('Enter the text: ')
#     if t == '':
#         break
#     else:
#         if t not in l:
#             l.append(t)
# print(l)

# for n in range(1, 10000):
#     nlist = ([i for i in range(1, n // 2 + 1) if n % i == 0])
#     if sum(nlist) == n:
#         print(n)

# text = "Contractions. include don’t isn’t and wouldn’t"
# text = text.split(' ')
# for i in range(len(text)):
#     while True:
#         if not text[i][0].isalpha():
#             text[i] = text[i][1:]
#         elif not text[i][-1].isalpha():
#             text

# morza = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-'}
#
# text = input('Enter the text: ')


# text = input('Enter the text: ').upper()
# for i in text:
#     for n in a:
#         print(a[])

# num = 0
# char = 0
# s = ['!', '@', '#', '$', '%', '&', '*']
# p = input('Enter your password: ')
# for i in p:
#     if len(p) > 8:
#         pass
#     else:
#         if i.isdigit():
#             num += 1
#         elif i.isalpha():
#             continue
#         else:
#             char += 1

# sdict = {
#     'student1': 1,
#     'student2': 8,
#     'student3': 6,
#     'student4': 7,
#     'student5': 5,
#     'student6': 8,
#     'student7': 9,
#     'student8': 4,
#     'student9': 7,
#     'student10':8,
# }
# summ = 0
# for i in sdict.values():
#     summ += i
# print(summ / 10)

# sdict = {
#     'student1': 'good',
#     'student2': 'good',
#     'student3': 'bad',
#     'student4': 'good',
#     'student5': 'bad',
#     'student6': 'bad',
#     'student7': 'bad',
#     'student8': 'bad',
#     'student9': 'good',
#     'student10':'good',
# }
#
# print(sdict, end=' ')

# sdict = {
#     'student1': 1,
#     'student2': 8,
#     'student3': 6,
#     'student4': 7,
#     'student5': 5,
#     'student6': 8,
#     'student7': 9,
#     'student8': 4,
#     'student9': 7,
#     'student10':8,
# }
#
# for i,n in sdict.items():
#     if n >= 5:
#         print(i)
#
# for i,n in sdict.items():
#     if n <= 5:
#         print(i)

# sdict = {
#     'student1': 1,
#     'student2': 8,
#     'student3': 6,
#     'student4': 7,
#     'student5': 5,
#     'student6': 8,
#     'student7': 9,
#     'student8': 4,
#     'student9': 7,
#     'student10':8,
# }
# print(sdict['student1'])

# s = 'a,2,b,5,c,8,a,4,e,11'
# s = s.split(',')
# ndict = {}
# for i in range(0, len(s), 2):
#     if s[i] in ndict:
#         ndict[s[i]] += int(s[i + 1])
#     else:
#         ndict[s[i]] = int(s[i + 1])
# print(ndict)

# text = 'exercises'

# for i in range(5, 25, 5):
#     disc_price = (i - 0.05) / 0.4
#     print(i, disc_price)

# import random
#
# bingo = {
#     'B': random.sample(range(1, 15), 5),
#     'I': random.sample(range(16, 30), 5),
#     'N': random.sample(range(31, 45), 5),
#     'G': random.sample(range(46, 60), 5),
#     'O': random.sample(range(61, 75), 5)
# }

# count = 0
# while True:
#     n = (input('Enter the age: '))
#     a = int(n)
#     if n == '':
#         break
#     elif a < 3:
#         count += 0
#     elif 3 < a < 12:
#         count += 14
#     elif a > 65:
#         count += 18
#     elif 13 < a < 64:
#         count += 23
#
# print(count)

# text1 = 'live'
# text2 = 'ilev'
# d1 = {}
# d2 = {}
# for i in text1:
#     d1[i] = text1.count(i)
# for i in text2:
#     d2[i] = text2.count(i)
# print(d1 == d2)

# s = 'a,2,b,3,c,4,e,11,a,4,b,5'
# s = s.split(',')
# d = {}
# for i in range(0, len(s), 2):
#     let = s[i]
#     number = int(s[i + 1])
#     if let in d:
#         d[let] += number
#     else:
#         d[let] = number
# print(d)

# dict1 = {'a' : 2, 'b' : 2,'c' : 1}
# x = {}
# for i in dict1:
#     if dict1[i] not in x:
#         x[dict1[i]] = i
# print(dict1)


