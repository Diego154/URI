N = int(input())
if N <= 3600:
    minutos = N // 60
    segundos = N - (minutos * 60)
    horas = minutos // 60
else:
    horas = N // 3600
    minutos = (N - (horas * 3600)) // 60
    segundos= (N - (horas * 3600)) - (minutos * 60)
print("%d:%d:%d"%(horas,minutos,segundos))