import unittest
from factorial import factorial_iterativo, factorial_recursivo

class TestFactorial(unittest.TestCase):
    def test_factorial_iterativo(self):
        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(1), 1)

    def test_factorial_recursivo(self):
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(1), 1)

    def test_casos_especiales(self):
        with self.assertRaises(ValueError):
            factorial_iterativo(-1)
        with self.assertRaises(ValueError):
            factorial_recursivo(-1)

if __name__ == "__main__":
    unittest.main()
