
class Alunos:
    
    def __init__(self, nome, nota1, nota2, faltas):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.faltas = faltas
    

    def infor(self): 
        print(self.nome)
        print(self.nota1 )
        print(self.nota2)
        print(self.faltas)
        
    
       
    def media(self):
        return (self.nota1 + self.nota2 / 2)
    def situação(self):
        media = self.media()
        if media <6 and media>=0:
            print("aluno reprovado, sera exterminado dentro de 24H.")
        elif media>6 and media < 10:
            print("aluno aprovado.")
        else:
            
    def faltas(self):
        if self.faltas>=5:
            print("aluno reprovado por faltas, sera exterminado dentro de 24H.")
        



joão=Alunos("João", 10, 2,2)
lara=Alunos("lara", "10", "10","7")
carlos=Alunos("carlos", "6", "8","4")
joão.media()
joão.situação()
