salario = float(input())
if salario > 0 and salario <= 400:
    porcentagem = salario * 0.15
    novo_salario = salario + porcentagem
    reajuste = novo_salario - salario
    print("Novo salario: %.2f"%novo_salario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 15 %")
if salario > 400 and salario <= 800:
    porcentagem = salario * 0.12
    novo_salario = salario + porcentagem
    reajuste = novo_salario - salario
    print("Novo salario: %.2f"%novo_salario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 12 %")
if salario > 800 and salario <= 1200:
    porcentagem = salario * 0.1
    novo_salario = salario + porcentagem
    reajuste = novo_salario - salario
    print("Novo salario: %.2f"%novo_salario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 10 %")
if salario > 1200 and salario <= 2000:
    porcentagem = salario * 0.07
    novo_salario = salario + porcentagem
    reajuste = novo_salario - salario
    print("Novo salario: %.2f"%novo_salario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 7 %")
if salario > 2000:
    porcentagem = salario * 0.04
    novo_salario = salario + porcentagem
    reajuste = novo_salario - salario
    print("Novo salario: %.2f"%novo_salario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 4 %")