dinheiro1=0
cem=0
cinquenta=0
cinquenta1=0
vinte=0
vinte1=0 
dez=0
dez1=0
cinco=0
cinco1=0
dois=0
dois1=0
moedas=0
um=0
um1=0
cinquentac=0
vintec=0
dezc=0
cincoc=0
umc=0

dinheiro = float(input())

dinheiro1 = int(dinheiro)
dinheiro -= dinheiro1
moedas = (dinheiro *100)

cem = dinheiro1//100
cinquenta = dinheiro1 %100
cinquenta1 = cinquenta//50
vinte = cinquenta%50
vinte1 = vinte//20
dez = vinte%20
dez1 = dez//10
cinco = dez%1;
cinco1 = cinco//5
dois = cinco%5
dois1 = dois//2

um = dois%2
um1 = um//1

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%cem)
print("%d nota(s) de R$ 50.00"%cinquenta1)
print("%d nota(s) de R$ 20.00"%vinte1)
print("%d nota(s) de R$ 10.00"%dez1)
print("%d nota(s) de R$ 5.00"%cinco1)
print("%d nota(s) de R$ 2.00"%dois1)


cinquentac = moedas //50
vintec = (moedas %50)//25
dezc = (((moedas %50)%25)//10)
cincoc = ((((moedas %50)%25)%10)//5)
umc = ((((moedas %50)%25)%10)%5)//1

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%um1)
print("%d moeda(s) de R$ 0.50"%cinquentac)
print("%d moeda(s) de R$ 0.25"%vintec)
print("%d moeda(s) de R$ 0.10"%dezc)
print("%d moeda(s) de R$ 0.05"%cincoc)
print("%d moeda(s) de R$ 0.01"%umc)
