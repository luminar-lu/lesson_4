def fact(n):
    for i in range (1, n+1, 1):
        yield i
n = int(input("Введите число :"))

answ = 1
for i in fact(n):
    answ= answ * i
print(answ)