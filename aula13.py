alcool=0
gasolina=0
disel=0

while True:
    print("escolha uma opção:")
    print("1) Alcool")
    print("2)Gasolina")
    print("3)Disel")
    print("4)Sair")
    numero = int(input("coloque seu atendimento:"))


    if numero == 1:
        alcool += 1
    if numero == 2:
        gasolina += 1
    if numero == 3:

        disel += 1
    if numero == 4:
        print("obrigado por abastecer ;)")
        print(gasolina)
        print(disel)
        print(alcool)
        break
