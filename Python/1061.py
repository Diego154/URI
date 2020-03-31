dia_inicio = int(input("Dia "))
hr_inicio, min_inicio, seg_inicio = input().split(" : ")
hr_inicio = int(hr_inicio)
min_inicio = int(min_inicio)
seg_inicio = int(seg_inicio)

dia_fim = int(input("Dia "))
hr_fim, min_fim, seg_fim = input().split(" : ")
hr_fim = int(hr_fim)
min_fim = int(min_fim)
seg_fim = int(seg_fim)

if hr_inicio > hr_fim:
    soma = (24-hr_inicio)+hr_fim