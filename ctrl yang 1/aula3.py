convidados = ["ana", "bruno", "carlos", "daniel",  "eduarda"]
convidados[2] = "fernanda"
convidados.append("gabriel")
convidados.insert(1,"helena")
removido=convidados.pop()
def festa():
    nome = input("digite um nome: ")
    if nome in convidados:
        print(nome + " esta confirmado na festa")
    else:
        print(nome + " não esta confirmado na festa")
    if len(convidados) > 5:
        print("a festa tera muitos convidados")
    else:
        print("a festa sera mais reservada")
    convidados.sort
    print(len(convidados))
    print(removido)
    print(convidados)
    #primeira posição da variavel e 0 e -1 e o ultimo, 
    # para trocar convidado digite:nome da variavel[numero do convidado] = nome novo/
    # para adicionar algo novo a lista digite: o nome da lista.apend("nome novo")
    #para adicionar algo na lista em um lugar expecifico utilize:o nome da lista.insert(o numero da pessoa, "o nome novo")
    #para remover algo na lista em um lugar expecifico utilize:del o nome da lista(o numero da pessoa)
    #pop = primeiro a sair, ultimo a entrar retira o ultimo item da lista
    #.remove = remover o nome das pessoas dentro da lista ou a lista em si
    #sort deixa listas com palavras em ordem alfabetica e listas com numeros em ordem decrecente
    #len mostra o tamanho da sua lista em numeros
    #set inicia vazio( lista = set()) e so aceita numeros ou outros diferentes
    #.upper e usado para deixar tudo em MAIUSCULA

    # timesxjogadores = [["amongus", "fenix", "BBC"],["jonas", "mauricio", "bernardo"]]
    # print(timesxjogadores[1][2])
    # matriz = [
    # [1,2,3,4],
    # [5,6,7, 8],
    # [9,10,11, 12]
    # ]
    # pares = 0
    # if matriz[0][0] % 2 == 0:
    #     pares += 1
    # if matriz[0][1] % 2 == 0:
    #     pares += 1
    # if matriz[0][2] % 2 == 0:
    #     pares += 1
    # if matriz[0][3] % 2 == 0:
    #     pares += 1
    # if matriz[1][0] % 2 == 0:
    #     pares += 1
    # if matriz[1][1] % 2 == 0:
    #     pares += 1
    # if matriz[1][2] % 2 == 0:
    #     pares += 1
    # if matriz[1][3] % 2 == 0:
    #     pares += 1
    # if matriz[2][0] % 2 == 0:
    #     pares += 1
    # if matriz[2][1] % 2 == 0:
    #     pares += 1
    # if matriz[2][2] % 2 == 0:
    #     pares += 1
    # if matriz[2][3] % 2 == 0:
    #     pares += 1


    # print(matriz[0])
    # print(matriz[1])
    # print(matriz[2])
    # print(pares)