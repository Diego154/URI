n1, n2, n3, n4 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/(1+2+3+4)
if media >= 7:
    print("Media: %.1f"%media)
    print("Aluno aprovado.")
if media >= 5 and media < 7:
    exame = float(input())
    media_exame = (media + exame)/2
    if media_exame >= 5:
        print("Media: %.1f"%media)
        print("Aluno em exame.")
        print("Nota do exame: %.1f"%exame)
        print("Aluno aprovado.")
        print("Media final: %.1f"%media_exame)
    else:
        print("Media: %.1f"%media)
        print("Aluno em exame.")
        print("Nota do exame: %.1f"%exame)
        print("Aluno reprovado.")
        print("Media final: %.1f"%media_exame)
if media < 5:
    print("Media: %.1f"%media)
    print("Aluno reprovado.")