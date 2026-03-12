import unittest
from calculadora import calculadora


class TestCalculadora(unittest.TestCase):

# Essa def existe para ativar a calculadora
    def setUp(self):
        self.calculadora = calculadora()

# Teste básico de soma     
    def testSoma(self):
        # CENÁRIO
        a = 2
        b = 3


        # EXECUÇÃO
        resultado = self.calculadora.soma(a, b)


        # VERIFICAÇÃO
        self.assertEqual(resultado, 5)

# Teste de soma de um número positivo + negativo
    def testSomaNegativo(self):
        # CENÁRIO
        a = -2
        b = 3


        # EXECUÇÃO
        resultado = self.calculadora.soma(a, b)


        # VERIFICAÇÃO
        self.assertEqual(resultado, 1)

# Teste básico de subtração
    def testSubtracaoSimples(self):
        # CENÁRIO
        a = 5
        b = 2


        # EXECUÇÃO
        resultado = self.calculadora.subtracao(a, b)


        # VERIFICAÇÃO
        self.assertEqual(resultado, 3)

# Teste básico de multiplicação
    def testMultiplicacaoSimples(self):
        # CENÁRIO
        a = 4
        b = 3


        # EXECUÇÃO
        resultado = self.calculadora.multiplicacao(a, b)


        # VERIFICAÇÃO
        self.assertEqual(resultado, 12)

# Teste básico de divisão
    def testDivisaoSimples(self):
        # CENÁRIO
        a = 10
        b = 2


        # EXECUÇÃO
        resultado = self.calculadora.divisao(a, b)


        # VERIFICAÇÃO
        self.assertEqual(resultado, 5)

# Teste para divisão por 0 (dá erro)
    def testDivisaoPorZero(self):
        # CENÁRIO
        a = 10
        b = 0


        # EXECUÇÃO
        resultado = self.calculadora.divisao(a, b)


        # VERIFICAÇÃO
        self.assertEqual(resultado, "Erro: Divisão por zero")




if __name__ == "__main__":
    unittest.main()
