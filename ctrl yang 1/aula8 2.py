
def caucular(notas):
    return sum(notas) / len(notas)
numero = ("aluno numero ")
def aluno_media(media):
    if media < 0 or media > 10:
        print("nota invalida")
    elif media < 5:
        print(" esta reprovado na materia")
    elif media >= 5 and media < 6.9:
        print( " esta de recuperação na materia")
    elif media >= 7:
        print(" esta aprovado na materia")
def boltim(nome, notas):
    media = caucular(notas)
    situação = aluno_media(media)

    print(f"aluno: {nome}")
    print(f"media: {media}")
    print(f"situação: {situação}")
boltim("joão",  [10,9,2])
