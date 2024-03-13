import unittest

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return round(a / b, 2)

def media(lista):
    return sum(lista) / len(lista)

def maior_valor(lista):
    return max(lista)

def menor_valor(lista):
    return min(lista)

def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

class TestFuncoes(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(-1, -1), 0)
        self.assertEqual(subtracao(10, 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 3), 6)
        self.assertEqual(multiplicacao(-2, 3), -6)
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_divisao(self):
        self.assertEqual(divisao(5, 2), 2.5)
        self.assertEqual(divisao(10, 3), 3.33)

    def test_media(self):
        self.assertEqual(media([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(media([0, 0, 0]), 0.0)

    def test_maior_valor(self):
        self.assertEqual(maior_valor([1, 2, 3]), 3)
        self.assertEqual(maior_valor([-1, -2, -3]), -1)

    def test_menor_valor(self):
        self.assertEqual(menor_valor([1, 2, 3]), 1)
        self.assertEqual(menor_valor([-1, -2, -3]), -3)

    def test_numero_primo(self):
        self.assertTrue(numero_primo(2))
        self.assertTrue(numero_primo(3))
        self.assertFalse(numero_primo(4))
        self.assertTrue(numero_primo(5))
        self.assertFalse(numero_primo(6))

if __name__ == '__main__':
    unittest.main()
