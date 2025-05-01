import unittest
from flatten import aplanar

class TestAplanar(unittest.TestCase):
    def test_lista_simple(self):
        self.assertEqual(aplanar([1, 2, 3]), [1, 2, 3])

    def test_lista_anidada(self):
        self.assertEqual(aplanar([1, [2, 3], [4, [5]]]), [1, 2, 3, 4, 5])

    def test_elementos_no_listas(self):
        self.assertEqual(aplanar(42), [42])  # Elemento único no lista
        self.assertEqual(aplanar("texto"), ["texto"])  # Cadena como elemento

    def test_lista_vacia(self):
        self.assertEqual(aplanar([]), [])
        self.assertEqual(aplanar([[], [[], []]]), [])

    def test_tipo_datos_mixtos(self):
        self.assertEqual(aplanar([1, "a", [True, [None]]]), [1, "a", True, None])

if __name__ == "__main__":
    unittest.main()
