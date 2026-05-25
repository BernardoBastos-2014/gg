
with open("frutas.txt", "r") as arquivo:
    print("frutas atuais: " + arquivo.read())
fruta = input("digite um nome: ")
with open("frutas.txt", "a") as arquivo:
    arquivo.write(fruta +"\n")
print   ("fruta adicionada com sucesso")
with open("frutas.txt", "r") as arquivo:   
    linhas= arquivo.readlines()
    print("quantidade de linhas:", len(linhas))
with open("frutas.txt", "r") as arquivo:
    print("frutas atuais: " + arquivo.read())


    
