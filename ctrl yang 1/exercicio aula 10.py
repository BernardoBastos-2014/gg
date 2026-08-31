
class livro:
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.emprestado = False
    

    def infor(self): 
        print(self.titulo)
        print(self.autor )
        print(self.paginas)
        print(self.emprestado)
        
        
       
    def emprestado(self):
        if self.emprestado == False:
            self.emprestado = True
            print("livro emprestado")
        else:
            self.emprestado = False
            print("livro ja emprestado")
    def devolver(self):
        if self.emprestado == False:
           self.devolver = True
           print("livro não emprestado")
        else:
            print("livro devolvido")
            self.devolver = False
        
    

pequeno_princepe=livro("O Pequeno Princepe", "Roberto Carlos", "201")
roberto_carlos_a_hstoria=livro("roberto_carlos_a_hstoria", "Pequeno Princepe", "102",)
pequeno_princepe.infor()
pequeno_princepe.emprestado()
#pequeno_princepe.devolver()

