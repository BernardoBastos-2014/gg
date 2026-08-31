def banco():
    codigo = int(input("put your food number here: "))
    quantia = int(input("how many itens you will whant: "))
    valor = 0
    if codigo == 1:
        valor = quantia * 4.00
        print(valor)

    elif codigo == 2:
        valor = quantia  * 4.50
        print(valor)
    elif codigo == 3:
        valor = quantia  * 5.00 
        print(valor)
    elif codigo == 4:
        valor = quantia  * 2.00 
        print(valor)
    elif codigo == 5:
        valor = quantia  * 1.50 
        print(valor)
    else :
        print("there anen't this in menu today")   
banco()