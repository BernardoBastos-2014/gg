def cadastro():
    nome = input("coloque seu primeiro nome ")
    altura= float(input("coloque sua altura"))
    idade_minima = 12
    idade =  int(input("coloque a sua idade "))
    if idade >= idade_minima and altura >= 1.40:
        print("cadastro realizado!")
        print(nome,idade)
        print(nome+" e maior de idade e altura o suficiente, esta autorizado a ir no brinquedo")
    elif idade < idade_minima and idade > 0 and altura >= 1.40:
        print("cadastro realizado!")
        print(nome,idade)
        print(nome+" e menor de idade e não pode ir no brinquedo ")
    elif idade >= idade_minima and idade > 0 and altura < 1.40:
        print("cadastro realizado!")
        print(nome,idade)
        print(nome+" e muito pequeno e não pode ir no brinquedo ")
    elif idade < idade_minima and idade > 0 and altura < 1.40:
        print("cadastro realizado!")
        print(nome,idade)
        print(nome+" e muito pequeno e muito novo, não pode ir no brinquedo ")
    else:
        print("você e burro? isso não existe  >:(")
cadastro()