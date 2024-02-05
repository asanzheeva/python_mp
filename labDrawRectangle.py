
# Rectangle with params: width, height, filled

s = '█'

width = int(input("Width?"))
height = int(input("Height?"))
filled = input("Fill with color? [y/n]")
is_filled = filled.lower() == 'y'

char_filled = s if is_filled else ' '

for i in range(height):
    if i == 0 or i == height-1:
        print(s * width)
    else:
        print(s, char_filled * (width-2), s, sep='')