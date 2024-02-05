
# HW:  Вывести в консоль все доступные цвета и фоны

import random

for j in range(0, 256, 16):
    for k in range(0, 16):
        print(f"\033[38;5;{j+k}m", end='')
        print(f"\033[48;5;{abs(256-(j+7+k))}m", end='')
        print(f" %3d" % (j+k), end=' ')
    print("\033[0m")