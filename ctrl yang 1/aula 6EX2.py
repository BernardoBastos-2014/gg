saldo = 0
idade_minima = 17
cadastro = False
print ("cadastro obrigatorio!!!")
while True:
    print("caixa eletronica disque 1   ")
    print("depositar disque 2   ")
    print("saquar disque 3   ")
    print("sair disque 4   ")
    print("logar disque 5   ")
    
    numero = int(input("coloque seu atendimento  "))

    if cadastro == True:
        if numero ==  1:
                print(nome, "seu saldo atual e " , saldo)
        elif numero == 2:
            depositar = float(input("quanto deseja depoitar?  "))
            if depositar > 0:
                print("dinheiro depositado!!!")
                saldo += depositar
                print(nome, "seu saldo atual e " , saldo)
            else:
                print("ERRO....isso e imposivel")

        if numero == 3:
            saquar = float(input("quanto deseja saquar?  "))

            if saquar < 0 or saquar > saldo:
                print("ERRO....isso e imposivel")

            else:
                saldo -= saquar
                print(nome,"seu saldo atual e " , saldo)
        if numero == 4:
            break

        else:
            if numero == 5:
                if idade > idade_minima:
                    nome = input("coloque seu primeiro nome ")
                    altura= int(input("coloque seu numero de telefone "))
                    idade =  int(input("coloque a sua idade "))
                    idade_minima = 17
                    print("parabens!!! agora voce esta logado no banco bernardo.")
                    cadastro = True
                else:
                    print("você e muito novo para esse aplicativo. BLOQUEANDO")
                    break