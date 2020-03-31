n = int(input())
if n < 365:
    mes = n // 30
    dias = n - (mes * 30)
    ano = mes // 365
else:
    ano = n // 365
    mes = (n - (365 * ano)) // 30
    dias = (n - (365 * ano)) - (mes * 30)
print("%d ano(s)"%ano)
print("%d mes(es)"%mes)
print("%d dia(s)"%dias)