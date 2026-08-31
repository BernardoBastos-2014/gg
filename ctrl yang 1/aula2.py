nome =input("digite nome do aluno(a): ")
nota = float(input("digite a nota do aluno: "))
if nota < 0 or nota > 10:
    print("nota invalida")
elif nota < 5:
    print(nome + " esta reprovado na materia")
elif nota >= 5 and nota < 6.9:
    print(nome + " esta de recuperação na materia")
elif nota >= 7:
    print(nome + " esta aprovado na materia")


