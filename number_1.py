import re
import random

not_gost = []  # список для генерации автомобильных номеров
gost = []  # список автомобильных номеров по госту
str1 = 'АВЕКМНОРСТУХ'
str2 = '0123456789'

print('Пожалуйста укажите сколько номеров вы хотите сгенерировать в списке')
while 1:
    count = input()
    try:
        count = int(count)
        inf = count
        break
    except ValueError:
        print('Введите целое число')

for j in range(count):
    str3 = ''.join([random.choice(str1) for x in range(random.randint(1, 5))])
    str4 = ''.join([random.choice(str2) for x in range(random.randint(1, 5))])
    str5 = ''.join([random.choice(str1) for x in range(random.randint(1, 5))])
    str6 = ''.join([random.choice(str2) for x in range(random.randint(1, 5))])
    not_gost.append(str3 + str4 + str5 + str6)

for i in not_gost:
    match = re.findall('[АВЕКМНОРСТУХ]{1}\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}(?<!00)', i)
    if match != []:
        gost.append(match)

print("Начальный список автомобильных номеров:")
print(not_gost)
print("Список автомобильных номеров по госту:")
print(gost)

if __name__ == '__main__':
    print('Завершение программы')

