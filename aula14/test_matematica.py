import unittest
from aula14.matematica import cauculadora


class test_cauculadora(unittest.TestCase):
    def setUp(self):
        self.c = cauculadora()
    def test_soma(self):
        self.assertEqual(self.c.soma(2,3), 5)
    def test_sub(self):
        self.assertEqual(self.c.sub(2,3), -1)
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)