import unittest
from Practica31 import Equacio

class TestEq(unittest.TestCase):
    def test_eq(self):
        #Test 1 - Numeros Positius
        self.assertEqual(Equacio("20x + 30 = 70").calcula(),2.0)
        #Test 2 - Numeros Negatius
        self.assertEqual(Equacio("200x - 50 = -78").calcula(),-0.14)
        #Test 3 - Numeros Positius i Negatius
        self.assertEqual(Equacio("5x + 8 = -6").calcula(),-2.8)
        #Test 4 - Valor 0
        self.assertEqual(Equacio("4x - 28 = 0").calcula(),7.0)
        #Test 5 - Lletra en comptes de numero
        self.assertEqual(Equacio("4x - 28 = d").calcula(),7.0)
        #Test 6 - Operador no valid
        self.assertEqual(Equacio("4x * 28 = 0").calcula(),7.0)

if __name__ == "__main__":
    unittest.main();
