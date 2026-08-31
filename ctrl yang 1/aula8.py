def soma(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b 
    elif op == "-":
        return a - b   
    elif op == "*":
        return a * b   
    elif op == "/":
        return a / b   
    else :
        return("não e possivel fazer isso :(")
letraA=input("qual o primeiro numero? ")
letraB=input("qual o segundo numero? ")
def bigest(a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
bigest(letraA, letraB)