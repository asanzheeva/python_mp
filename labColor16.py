
#HW:  Вывести в консоль все доступные цвета и фоны

# \033[_;_;_m

import random

for j in range(30, 38):
    for k in range(40, 48):
        i = random.randint(0, 6)
        print(f"\033[{i};{j};{k}m", end='')
        print(i, ";", j, ";", k, sep='', end=' ')
    print("\033[0m")