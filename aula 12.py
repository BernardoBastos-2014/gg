# try:
#     valor = float(input("digite um numero:"))
#     nome = str(input("digite seu nome:"))
#     print(f"{nome} sacou R${valor} da sua conta bancaria.")
    
# except:
#     print("valor invalido, digite um valor valido. como numeros.")

# finally:
#     print(" finalizando processo...")

# while True:
#     try:
#         n1= int(input("digite um numero inteiro:"))
#         n2= int(input("digite um numero inteiro:"))
#         print(n1 / n2)

#     except:
#         print("divisão invalida, tu e um Beta.")
saldo = 1000
while True:
    print("caixa eletronica disque 1   ")
    print("depositar disque 2   ")
    print("saquar disque 3   ")
    print("sair disque 4   ")

    try:
        numero = int(input("coloque seu atendimento  "))
        if numero == 1:
            print(f"O saldo atual é R${saldo} e ")
            with open("recentes.txt", "r") as arquivo:
                print(arquivo.read())
        if numero == 2:
            deposito = int(input("quanto deseja depositar?"))
            if deposito >= 0: 
                saldo += deposito
                print(f"seu saldo agora e de R${saldo}")
                with open("recentes.txt", "w") as arquivo:
                    arquivo.write(f" foi adicionado {deposito} a sua conta ha um tempo.")
            else:
                print("O numero tem que ser positivo")
        if numero == 3:
            saque = int(input("quanto deseja saquar?"))
            if deposito >= 0: 
                saldo -= saque
                print(f"seu saldo agora e de R${saldo}")
                with open("recentes.txt", "w") as arquivo:
                    arquivo.write(f" foi saquado {saque} a sua conta ha um tempo.")
            else:
                print("O numero tem que ser positivo")
        if numero == 4:
                print("desligando...")
    except:
        print("erro, tente outra coisa ")
    finally:
        print("obrigado por usar o caixa.")



        sessenta e sete 67