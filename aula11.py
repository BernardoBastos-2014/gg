# class Cachorro:
#     def __init__(self,nome,idade,raca):
#         self.nome = nome
#         self.__idade = idade
#         self.raca = raca

#     def latir(self):
#         print(f"{self.nome} esta latindo")

#     def idade(self):
#         print(f"{self.nome} esta com {self.__idade} anos de idade")

#     def get_idade(self):
#         return self.__idade
    
#     def set_idade(self, nova_idade):
#        if nova_idade > 0:
#         self.__idade = nova_idade
#        else:
#           print("idade invalida")
    
# cleitinho = Cachorro("cleitinho", 5, "Dachshund" )
# cleitinho.idade()
# print(cleitinho.get_idade())
# cleitinho.set_idade(-1)
# print(cleitinho.get_idade())




# class Animal:
#     def __init__ (self, nome, idade):
#       self.nome = nome
#       self.idade = idade
#     def comer(self):
#         print(f"{self.nome} esta comendo")
#     def respirar(self):
#         print(f"{self.nome} esta respirando")
# class Cachorro(Animal):
#    def latir(self):
#         print(f"{self.nome} esta latindo")
# class cobra(Animal):
#     def abrir_o_tinder(self):
#         print(f"{self.nome} esta abrindo o tinder para te trair")
#     def rastejar(self):
#         print(f"{self.nome} esta rastejando")
# ana_julha = cobra("ana julha", 11)
# vinho = Cachorro("vinho", 4)

# ana_julha.abrir_o_tinder()
# ana_julha.rastejar()
# ana_julha.comer
# ana_julha.respirar


# vinho.comer
# vinho.respirar
# vinho.latir

class nivel_estelar:
    def __init__ (self, nome, arma, anime, poder, poder_arma, aura):
       self.nome = nome
       self.arma = arma
       self.anime = anime
       self.poder = poder
       self.poder_arma = poder_arma
       self.__aura = aura
    def get_aura(self):
         return self.__aura
    
    def set_aura(self, quanta_aura):
        if quanta_aura < 0:
         self.__aura = quanta_aura
         print(f"{self.nome} tem aura")
        else:
           print("personagen e betinha")
   

   
    def nivel_estelar(self):
        if self.poder > 6:
            print(f"{self.nome} tem poder nivel estelar")
        else:
           print(f"{self.nome} não tem nivel de poder estelar")
           
class personagen(nivel_estelar):
    def equipamento(self):
        if self.arma == True:
            print(f"{self.nome} tem equipamento")
        elif self.poder_arma > 4:
            print(f"{self.nome} tem equipamento forte") 
        else:
           print(f"{self.nome} não tem equipamento")
    
gojo = personagen("gojo", False, "jujutso kisen", 4, 0, 100000)
gojo.equipamento()
gojo.nivel_estelar()
print(gojo.get_aura())
gojo.set_aura(0)
print(gojo.get_aura())
