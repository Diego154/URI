cont = 0
par = 0
while cont < 5:
    cont += 1
    num = int(input())
    if num % 2 == 0:
        par += 1
print("%d valores pares"%par)