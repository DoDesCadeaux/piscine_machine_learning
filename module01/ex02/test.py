import unittest
from vector import Vector  # Assuming your Vector class code is in a file named vector_module.py

class TestVector(unittest.TestCase):
    def test_initialization(self):
        v1 = Vector([[1]])
        self.assertEqual(v1.value, [[1]])
        self.assertEqual(v1.shape, (1, 1))

        v2 = Vector([[1, 2, 3]])
        self.assertEqual(v2.shape, (1, 3))

        with self.assertRaises(ValueError):
            Vector([[1, 2], [3]])

    def test_addition(self):
        v1 = Vector([[1, 2, 3]])
        v2 = Vector([[4, 5, 6]])
        v3 = v1 + v2
        self.assertEqual(v3.value, [[5, 7, 9]])

        with self.assertRaises(TypeError):
            v1 + Vector([[1]])

    def test_subtraction(self):
        v1 = Vector([[10, 20, 30]])
        v2 = Vector([[1, 2, 3]])
        v3 = v1 - v2
        self.assertEqual(v3.value, [[9, 18, 27]])

    def test_multiplication(self):
        v1 = Vector([[1, 2, 3]])
        v2 = v1 * 3
        self.assertEqual(v2.value, [[3, 6, 9]])

    def test_division(self):
        v1 = Vector([[9, 18, 27]])
        v2 = v1 / 3
        self.assertEqual(v2.value, [[3.0, 6.0, 9.0]])

        with self.assertRaises(ZeroDivisionError):
            v1 / 0

    def test_transpose(self):
        v1 = Vector([[1, 2, 3]])
        v2 = v1.T()
        self.assertEqual(v2.value, [[1], [2], [3]])
        self.assertEqual(v2.shape, (3, 1))

    def test_dot_product(self):
        v1 = Vector([[1, 2, 3]])
        v2 = Vector([[4, 5, 6]])
        result = v1.dot(v2)
        self.assertEqual(result, 32)

        with self.assertRaises(TypeError):
            v1.dot(Vector([[1]]))

if __name__ == '__main__':
    unittest.main()
