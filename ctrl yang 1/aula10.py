class casa:
    cidade="BH"
    def __init__(self, rua, bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep

    def endereçoCompleto(self):
        print(casa.cidade)
        print(self.rua)
        print(self.bairro )
        print(self.cep)

CtrlPlay=casa("rua A", "santo augustinho", "12345=678")
casasamuel=casa("rua B", "santo pedro", "87654=321")
CtrlPlay.endereçoCompleto()
casasamuel.endereçoCompleto()