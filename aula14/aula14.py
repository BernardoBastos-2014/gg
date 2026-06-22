#print("local de criação de nome:")
#nome = input("qual nome gostaria de aplicar? ")
#sobrenome = input("qual sobrenome gostaria de aplicar primeiro? ")
#sobrenome2 = input("qual sobrenome gostaria de aplicar agora? ")
#x =len(sobrenome)
#y =len(sobrenome2)
#if x > y: 
#    print("Então o nome do seu filho sera " + nome + " " + sobrenome + " " +  sobrenome2)
#else:
#     print("Então o nome do seu filho sera " + nome + " " + sobrenome2 + " " + sobrenome )


def sob(nome,sobrenome1,sobrenome22):
    if (len(sobrenome22)) > (len(sobrenome1)):
        return nome + " " + sobrenome22 + " " + sobrenome1
    else:
        return nome + " " + sobrenome1 + " " + sobrenome22

print(sob("jão","madera", "sos"))


