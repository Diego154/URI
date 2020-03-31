nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())
porcentagem = total_vendas * (15/100)
salario = salario_fixo + porcentagem
print("TOTAL = R$ %.2f"%salario)