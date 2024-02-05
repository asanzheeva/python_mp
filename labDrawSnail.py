
# HW:  Нарисовать в консоли прямоугольную улитку с параметрами: ширина, высота

s = '█'

'''
███████████████████████████████████████████
                                          █
█████████████████████████████████████████ █
█                                       █ █
█ █████████████████████████████████████ █ █
█ █                                   █ █ █
█ █ █████████████████████████████████ █ █ █
█ █ █                                 █ █ █
█ █ ███████████████████████████████████ █ █
█ █                                     █ █
█ ███████████████████████████████████████ █
█                                         █
███████████████████████████████████████████
'''

width = int(input("Width? "))
length = int(input("Length? "))

direction = input("Right or left? [r/l] ")
is_right = direction.lower() == 'r'

def reverse(str):
    return str[::-1]

frame = ''
snailBottom = ''

for i in range(int(length/2)):
    if i % 2 == 0:
        symb = s
    else:
        symb = ' '

    snailBottom = '\n' + frame + symb * (width - i*2) + reverse(frame) + snailBottom
    frame += symb

# 

frameRight = ''
frameLeft = ''
snailTop = ''
snailTopRight = ''
temp = 0

for i in range(int(length/2) + length%2):
    if i % 2 == 0:
        symb = s
    else:
        symb = ' '

    frameRight = symb + frameRight
    snailTopRight = frameLeft + symb * (width - (i+1) - temp) + frameRight
    
    if not is_right:
        snailTopRight = reverse(snailTopRight)

    snailTop += snailTopRight

    if not i == (int(length/2) + length%2 - 1):
        snailTop += '\n'

    if i > 1:
        temp +=1
        frameLeft += symb

print(snailTop, snailBottom)