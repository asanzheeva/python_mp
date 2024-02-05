
# Line with width parametr 

char = '*' #draw element

print("Line length")
w = int(input())

# 1
print(char * w)

# 2
for i in range(w):
    print(char, end='')

for i in range(w):
    if i % 7 == 0:
        print('+', end='')
    else:
        print(char, end='')