import itertools as it
list_1 = []
list_2 = []
def count(n):
    for i in it.count(n, 1):
        if i > n + 10:
            break
        else:
            list_1.append(i)
    return list_1
def cycle(n):
    count = 0
    for item in it.cycle(n):
        if count >= 10:
            break
        list_2.append(item)
        count += 1
    return list_2
number = int(input("Введите число: "))
symbol = input("Введите символ: ")
print(count(number))
print(cycle(symbol))
