p = input().split(" ")
a, b, c = p
a = float(a)
b = float(b)
c = float(c)
if c >= b + a:
    print("NAO FORMA TRIANGULO")
if (c**2) == (b**2)+(a**2):
    print("TRIANGULO RETANGULO")
    if a==b or a==c or b==c:
        print("TRIANGULO ISOSCELES")
if (c**2) > (b**2)+(a**2):
    print("TRIANGULO OBTUSANGULO")
    if a==b or a==c or b==c:
        print("TRIANGULO ISOSCELES")
if (c**2) < (b**2)+(a**2):
    print("TRIANGULO ACUTANGULO")
    if a==b and a==c and b==c:
        print("TRIANGULO EQUILATERO")
    else:
        if a==c or b==c or a==c:
            print("TRIANGULO ISOSCELES")