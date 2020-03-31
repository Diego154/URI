p = input().split(" ")
a, b, c = p
a = int(a)
b = int(b)
c = int(c)
if a > b and b > c:
    print(c)
    print(b)
    print(a)
if a > c and b < c:
    print(b)
    print(c)
    print(a)
if b > a and a > c:
    print(c)
    print(a)
    print(b)
if b > c and c > a:
    print(a)
    print(c)
    print(b)
if c > a and a > b:
    print(b)
    print(a)
    print(c)
if c > b and b > a:
    print(a)
    print(b)
    print(c)
print("")
print(a)
print(b)
print(c)
