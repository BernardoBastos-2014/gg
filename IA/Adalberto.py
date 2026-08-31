import IA as pc
from tkinter import *


main_window = Tk()
main_window.title("Adalberto")
main_window.geometry("800x500")

frame = Frame(main_window)
frame.grid()


l_indentif = Label(frame, text = "insira uma mensagem aqui:")
l_indentif.grid(row=0, column=0)


e_mensagem =  Entry(frame)
e_mensagem.grid(row=0, column=1)


frame2 = Frame(main_window)
frame2.grid(row=1, column=0)

v = StringVar()
Label(frame2, textvariable=v, justify=LEFT).grid()

nome_maquina = "adalberto"

v.set("qual seu nome?")


entrada_sugestao = False
entrada_nome_do_usuario = True
nome_usuario = ""
historico_conversa = ""




def roda_IA():
    global entrada_sugestao
    global entrada_nome_do_usuario
    global historico_conversa
    global nome_usuario

    if entrada_nome_do_usuario:
        nome_usuario = e_mensagem.get()
        saudacao = pc.saudacao_GUI(nome_maquina)
        historico_conversa = nome_maquina + ": " + saudacao + "\n"
        v.set(historico_conversa)
        entrada_nome_do_usuario = False
        e_mensagem.delete(0, END)
    else:
        texto = e_mensagem.get()
        historico_conversa += "\n" + nome_usuario + ": " + texto
        v.set(historico_conversa)
        e_mensagem.delete(0, END)

        if entrada_sugestao:
            pc.salva_sugestao(texto)
            entrada_sugestao = False
            historico_conversa += "\nAgora aprendi!!!Vamos continuar a conversa..."
            v.set(historico_conversa)
        else:
            resposta = pc.BuscaResposta_GUI("Cliente: " + texto + "\n")
            if resposta == "Me desculpe, não sei o que falar":
                historico_conversa += "Me desculpe, não sei o que falar.O que você esperava?\n"
                v.set(historico_conversa)
                entrada_sugestao = True

            else:
                historico_conversa += "\n" + pc.exibeResposta_GUI(texto, resposta, nome_maquina)
                v.set(historico_conversa)




Button(frame, text="enter", command= roda_IA).grid(row=0, column=2)


main_window.mainloop()