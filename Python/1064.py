cont = 0
valor = 0
val = 0
while cont < 6:
    cont += 1
    num = float(input())
    if num > 0:
        val += num
        valor += 1
media = val/valor
print("%d valores positivos"%valor)
print("%.1f"%media)