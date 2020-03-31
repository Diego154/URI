n1, n2 = input().split(" ")
inicio = int(n1)
fim = int(n2)
if inicio > fim:
    soma = (24-inicio)+fim
    print("O JOGO DUROU %d HORA(S)"%soma)
elif inicio < fim:
    soma = fim - inicio
    print("O JOGO DUROU %d HORA(S)"%soma)
else:
    print("O JOGO DUROU 24 HORA(S)")