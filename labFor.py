
for i in range(5):
    print(i)

for i in [0, 1, 2]:
    print(i)

for i in range(19, 16, -1):
    print(i)

print("--------------")

for i in range(10):
    if i == 2:
        continue
    elif i == 5:
        break
    else:
        print(i)

print("*", end="")
for c in "Welcome back":
    print(c, end="*")

print("\n")
print(*"Hello", sep="-")

i = 0
while i < 3:
    print(i)
    i += 1