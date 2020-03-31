cod, quant = input().split(" ")
cod = int(cod)
quant = int(quant)
if cod == 1:
    valor = quant * 4.00
    print("Total: R$ %.2f"%valor)
if cod == 2:
    valor = quant * 4.50
    print("Total: R$ %.2f"%valor)
if cod == 3:
    valor = quant * 5.00
    print("Total: R$ %.2f"%valor)
if cod == 4:
    valor = quant * 2.00
    print("Total: R$ %.2f"%valor)
if cod == 5:
    valor = quant * 1.50
    print("Total: R$ %.2f"%valor)
