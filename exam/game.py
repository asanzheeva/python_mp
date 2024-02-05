import random
que = int(input("Введите кол-во вопросов: "))
lvl = int(input("Выберите уровень сложности(1, 2 или 3):  "))

cor = 0 # кол-во правильных ответов
wr = 0 # кол-во неправильных ответов
i = 0

def func(lvl, cor, wr): 
    if (lvl == 1):
        h = random.randrange(0, 3, 1)
        m = random.randrange(0, 60, 5)
        a = h * 60 + m
        print(h, ":", m, "= ?")
        res = int(input("Ответ: "))

    elif (lvl == 2):
        h = random.randrange(0, 8, 1)
        m = random.randrange(0, 60, 5)
        a = h * 60 + m
        print(h, ":", m, "= ?")
        res = int(input("Ответ: "))   

    elif (lvl == 3):
        h = random.randrange(0, 24, 1)
        m = random.randrange(0, 60, 5)
        a = h * 60 + m
        print(h, ":", m, "= ?") 
        res = int(input("Ответ: "))

    else:
        print("Такого уровня нет")
        raise Exception("Такого уровня нет")
        
    if res == a:
        print("Правильно!")
        cor +=1
    else:
        print("Неправильно")
        wr += 1
    return i, cor, wr

while i < que: 
    i, cor, wr = func(lvl, cor, wr)   
    i+=1

print("Статистика: ", "Верно:", cor, ", Неверно:", wr)

