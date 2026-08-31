import suprimentos
import os
import math
dias = 14

tripulantes = 5


agua = suprimentos.calcular_agua(5,14)

comida = suprimentos.calcular_racao(14,5)

agua_arredondada = math.ceil(agua)

print(f"o resultado de total de comida e: {comida} ")

print(f"o resultado de total de agua e: {agua} ")


if os.path.exists("lixoEspacial.txt"):
    os.remove("lixoEspacial.txt")
    print("removido")
else:
    print("não encotrado")