cont = 0
par = 0
imp = 0
pos = 0
neg = 0
while cont < 5:
    cont += 1
    num = int(input())
    if num > 0:
        pos += 1
    if num < 0:
        neg += 1
    if num % 2 == 0:
        par += 1
    if num % 2 != 0:
        imp += 1
print("%d valor(es) par(es)"%par)
print("%d valor(es) impar(es)"%imp)
print("%d valor(es) positivo(s)"%pos)
print("%d valor(es) negativo(s)"%neg)