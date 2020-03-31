cem = 0
cinq = 0
vint = 0
dez = 0
cinc = 0
dois = 0
um = 0
N = int(input())
valor = int(N)
while N >= 100:
    N -= 100
    cem += 1
while N >= 50:
    N -= 50
    cinq += 1
while N >= 20:
    N -= 20
    vint += 1
while N >= 10:
    N -= 10
    dez += 1
while N >= 5:
    N -= 5
    cinc += 1
while N >= 2:
    N -= 2
    dois += 1
while N >= 1:
    N -= 1
    um += 1
print(valor)
print("%d nota(s) de R$ 100,00"%cem)
print("%d nota(s) de R$ 50,00"%cinq)
print("%d nota(s) de R$ 20,00"%vint)
print("%d nota(s) de R$ 10,00"%dez)
print("%d nota(s) de R$ 5,00"%cinc)
print("%d nota(s) de R$ 2,00"%dois)
print("%d nota(s) de R$ 1,00"%um)