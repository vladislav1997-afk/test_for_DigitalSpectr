from random import randint

class SearchPoint():
    '''Класс искомой точки'''

    def __init__(self, w, h):
        '''инициализация случайных координат искомой точки'''
        self.__x = randint(0, w)
        self.__y = randint(0, h)

    def where_is_point(self, x, y):
        '''Описывает положение искомой точки относительно текущей.
		Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D" , ""
		'''
        pos_x = pos_y = ''
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'D'
        elif y < self.__y:
            pos_y = 'U'
        return pos_x + pos_y

    def point_X(self, w, h):
        return self.__x

    def point_Y(self, w, h):
        return self.__y

# Создание точки:
print('Пожалуйста укажите координаты сетки')
while 1:
    W = input()
    H = input()
    try:
        W = float(W)
        H = float(H)
        break
    except ValueError:
        print('Пожалуйста введите числа')

print('Пожалуйста укажите координаты текущей точки')
while 1:
    X0 = input()
    Y0 = input()
    try:
        X0 = float(X0)
        Y0 = float(Y0)
        break
    except ValueError:
        print('Пожалуйста введите числа')

SP = SearchPoint(W, H)
position = SP.where_is_point(X0, Y0)
X = SP.point_X(W, H)
Y = SP.point_Y(W, H)
Y_test = Y0
X_test = X0
print(position)

if position == 'RU':
    while Y_test < Y:
        X_test += 1
        while Y_test < Y:
            Y_test += 1
    X_test = X0
    while X_test < X:
        X_test += 1

if position == 'LU':
    while Y_test < Y:
        X_test -= 1
        while Y_test < Y:
            Y_test += 1
    X_test = X0
    while X_test > X:
        X_test -= 1

if position == 'RD':
    while Y_test > Y:
        X_test += 1
        while Y_test > Y:
            Y_test -= 1
    X_test = X0
    while X_test < X:
        X_test += 1

if position == 'LD':
    while Y_test > Y:
        X_test -= 1
        while Y_test > Y:
            Y_test -= 1
    X_test = X0
    while X_test > X:
        X_test -= 1

if position == 'R':
    while X_test < X:
        X_test += 1

if position == 'L':
    while X_test > X:
        X_test -= 1

if position == 'D':
    while Y_test > Y:
        Y_test -= 1

if position == 'U':
    while Y_test < Y:
        Y_test += 1

print("Настоящие координаты")
print(X)
print(Y)
print("Координаты при поиске:")
print(X_test)
print(Y_test)

if __name__ == '__main__':
    print('Завершение программы')
