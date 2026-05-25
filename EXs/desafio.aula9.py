
tarefas = input("digite uma tarefa: ")
with open("tarefas.txt", "a") as arquivo:
    arquivo.write(tarefas)
horario = input("digite o horario da tarefa: " + "\n")
with open("tarefas.txt", "a") as arquivo:
    arquivo.write("[" + horario + "]" + "\n")
print   ("tarefa adicionada com sucesso")
with open("tarefas.txt", "r") as arquivo:
    print("tarefas pendentes atuais: " + arquivo.read())



