class prova():
    def __init__ (self):
        self.questoess = []
        self.respostas = []



    def questoes(self, questao, resposta):
        if questao != "":
            self.questoess.append(questao)
        if resposta != "":
            self.respostas.append(resposta)

import unittest


class provatest(unittest.TestCase):
    def test_questoes(self):
        questao = "quanto e 2+2?"
        p = prova()
        p.questoes(questao, "")
        self.assertIn("quanto e 2 + 2", p.questoess)

    def test_respostas(self):
        resposta = "4"
        p = prova()
        p.respostas,("",resposta)
        self.assertIn("4", p.respostas)




if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)