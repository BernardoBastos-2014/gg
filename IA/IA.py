import random

def saudacao_GUI(nome):
    frase = ["Saudacões humano, meu nome e " + nome + ".  Como posso te auxiliar", "Ola, eu sou " + nome + " e estou aqui para ajudar!", "ola, bem vindo ao " + nome + ". como posso lhe ajudar"]
    return frase[random.randint(0,2)]
def salva_sugestao(sugestao):
    with open("BaseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")
     
def BuscaResposta_GUI(texto):
    with open("BaseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
              if jaccard(texto, viu) > 0.9:
                  proximalinha = conhecimento.readline()
                  if "Chatbot: " in proximalinha:
                      return proximalinha

            else:
               
                conhecimento.write(texto)
                return "desculpa, não sei o que falar..."
            
def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("Chatbot: ", nome)



def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len (textoBase) < 1: return 0
    else:
        palavras_em_comun = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comun += 1
        return palavras_em_comun / (len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?", "!", ",", ".", "...","Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t, "")
    frase = frase.upper()
    return frase