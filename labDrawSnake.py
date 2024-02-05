# HW: Нарисовать в консоли прямоугольную змейку с параметрами: ширина, высота

s = '█'

width = int(input("Width? "))
length = int(input("Length? "))
direction = input("Right or left? [r/l] ")

is_right = direction.lower() == 'r'
t = 0 if is_right else 1

for i in range(length):
    if i % 2 == 0:
        print(s * width)
    elif t % 2 == 0:
        print(' ' * (width-1), s, sep='')
        t += 1
    else:
        print(s, ' ' * (width-1), sep='')
        t += 1


leftDown = '╚'
rightDown = '╝'
centerHorisontal = '═'
centerVertical = '║'
leftUp = '╔'
rightUp = '╗'

t = 0 if is_right else 1

for i in range(length):
    if i % 2 == 0:
        if t % 2 == 0:
            print(leftDown, centerHorisontal * (width-2), rightUp, sep='')
        else:
            print(leftUp, centerHorisontal * (width-2), rightDown, sep='')
    elif t % 2 == 0:
        print(' ' * (width-1), centerVertical, sep='')
        t += 1
    else:
        print(centerVertical, ' ' * (width-1), sep='')
        t += 1


whiteSmile = '☻'
blackSmile = '☺'

t = 0 if is_right else 1

counter = 0
for i in range(length):
    if i % 2 == 0:
        if width % 2 == 1 or t % 2 == 0:
            for j in range(width):
                print(whiteSmile if counter % 2 == 0 else blackSmile, end='')
                counter += 1    
        else:
            for j in range(width):
                print(blackSmile if counter % 2 == 0 else whiteSmile, end='')
                counter += 1   
    elif t % 2 == 0:
        print('\n', ' ' * (width-1), whiteSmile if counter % 2 == 0 else blackSmile, sep='')
        t += 1
        counter += 1
    else:
        print('\n', whiteSmile if counter % 2 == 0 else blackSmile, ' ' * (width-1), sep='')
        t += 1
        counter += 1