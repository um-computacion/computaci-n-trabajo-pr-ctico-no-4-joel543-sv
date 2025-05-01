import unittest
from fibonacci import fibonacci_iterativo, fibonacci_recursivo

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_iterativo(self):
        self.assertEqual(fibonacci_iterativo(0), 0)
        self.assertEqual(fibonacci_iterativo(1), 1)
        self.assertEqual(fibonacci_iterativo(10), 55)

    def test_fibonacci_recursivo(self):
        self.assertEqual(fibonacci_recursivo(0), 0)
        self.assertEqual(fibonacci_recursivo(1), 1)
        self.assertEqual(fibonacci_recursivo(10), 55)

    def test_casos_especiales(self):
        with self.assertRaises(ValueError):
            fibonacci_iterativo(-5)
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-5)

if __name__ == "__main__":
    unittest.main()
