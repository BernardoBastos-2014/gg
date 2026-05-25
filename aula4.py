def dia():
    mes = ["January", "February", "March ", "April", "May","June ", "July", "August", "September", "October ", "November ", "December"]
    number = int(input("put your number here: "))
    if number == 1:
        print(mes[0])
    elif number == 2:
        print(mes[1])
    elif number == 3:
        print(mes[2])
    elif number == 4:
        print(mes[3])
    elif number == 5:
        print(mes[4])
    elif number == 6:
        print(mes[5])
    elif number == 7:
        print(mes[6])
    elif number == 8:
        print(mes[7])
    elif number == 9:
        print(mes[8])
    elif number == 10:
        print(mes[9])
    elif number == 11:
        print(mes[10])
    elif number == 12:
        print(mes[11])
    elif number == 0:
        print("erro:não ha mes 0")
    elif number > 12:
        print("erro:não ha mes maior que 12")
    else:
        print("isso não existe")
dia()