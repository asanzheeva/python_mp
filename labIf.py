# if
# if-else
# if-elif-elif-else

x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print(1)
else:
    if x < 0 and y > 0:
        print(2)
    else:
        if x < 0 and y < 0:
            print(3)
        else:
            print("else")

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print("else")

# тернальный условный оператор 

z = 1
print("yes" if z == 1 else "no")