import unittest
from aula14.aula14 import sob
class NomeTest(unittest.TestCase):
    def test_sobrenome(self):
        resultado = sob("jão", "madera", "sos")
        self.assertEqual(resultado, "jão madera sos")
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)