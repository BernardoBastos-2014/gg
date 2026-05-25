a = float(input())
b=  float(input())
c=  float(input())
forma = True
if a<b:
    a, b = b, a
if a<c:
    a, c = c, a
if b<c:
    b, c = c,b

if a >= b + c:
    print("não forma triangulo seu bobalhão cabeça de feijão")
    forma = False
if forma == True:
    if a**2 == b**2 + c**2:
        print("forma triangulo retangulo")
    if a**2 > b**2 + c**2:
        print("forma triangulo obtusangulo")
    if a**2 < b**2 + c**2:
        print("forma triangulo actangulo")
    if a== b==c:
        print("forma triangulo equilatero")
    elif b== c:
        print("forma triangulo isoceles")
    elif a== b:
        print("forma triangulo isoceles")
    elif a== b:
        print("forma triangulo isoceles")

