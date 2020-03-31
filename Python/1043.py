p = input().split(" ")
a, b, c = p
a = float(a)
b = float(b)
c = float(c)
if b-c<a<b+c and a-c<b<a+c and a-b<c<a+b:
    p = a+b+c
    print("Perimetro = %.1f"%p)
else:
    area = ((a+b)*c)/2
    print("Area = %.1f"%area)