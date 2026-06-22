
arquivo = input("qual nome exato do arquivo você quer matar?")


import os

if os.path.exists(arquivo):
    if "." in arquivo:
        os.remove(arquivo)
        print("arquivo Exterminado Dolorosamente com sucesso!!!")
    else:
        os.rmdir(arquivo)
        print("arquivo Exterminado Dolorosamente com sucesso!!!")
else:
    print("o arquivo fugiu")