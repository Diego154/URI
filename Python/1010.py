cod_peca1, num_peca1, valor_peca1 = input().split(" ")
cod_peca2, num_peca2, valor_peca2 = input().split(" ")
cod_peca1 = int(cod_peca1)
num_peca1 = int(num_peca1)
valor_peca1 = float(valor_peca1)
cod_peca2 = int(cod_peca2)
num_peca2 = int(num_peca2)
valor_peca2 = float(valor_peca2) 
soma1 = num_peca1 * valor_peca1
soma2 = num_peca2 * valor_peca2
soma = soma1 + soma2
print("VALOR A PAGAR: R$ %.2f"%soma)