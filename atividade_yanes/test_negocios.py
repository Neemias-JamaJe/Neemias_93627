import unittest
from loja import Loja
from escola import Escola

class TestDesafios(unittest.TestCase):

    def setUp(self):
        self.loja = Loja()
        self.escola = Escola()

    # --- TESTES DE DESCONTO ---
    def test_calculo_desconto_10(self):
        # CENÁRIO: R$ 100,00
        valor = 100.0
        # EXECUÇÃO
        resultado = self.loja.calcular_desconto(valor, tipo_cliente="comum")
        # VERIFICAÇÃO: 100 - 10% = 90
        self.assertEqual(resultado, 90.0)

    def test_calculo_desconto_vip(self):
        # CENÁRIO: R$ 100,00 e Cliente VIP (30% de desconto, por exemplo)
        valor = 100.0
        # EXECUÇÃO
        resultado = self.loja.calcular_desconto(valor, tipo_cliente="VIP")
        # VERIFICAÇÃO: 100 - 30% = 70
        self.assertEqual(resultado, 70.0)

    # --- TESTES ACADÊMICOS ---
    def test_media_notas(self):
        # CENÁRIO
        notas = [8.0, 7.0, 9.0]
        # EXECUÇÃO: (8+7+9) / 3 = 8.0
        resultado = self.escola.calcular_media(notas)
        # VERIFICAÇÃO
        self.assertEqual(resultado, 8.0)

    def test_aluno_aprovado(self):
        # CENÁRIO: Média 7.0 (exatamente no limite)
        notas = [7.0, 7.0]
        # EXECUÇÃO
        status = self.escola.verificar_status(notas)
        # VERIFICAÇÃO
        self.assertEqual(status, "Aprovado")

    def test_aluno_reprovado(self):
        # CENÁRIO: Média abaixo de 7.0
        notas = [6.0, 5.0]
        # EXECUÇÃO
        status = self.escola.verificar_status(notas)
        # VERIFICAÇÃO
        self.assertEqual(status, "Reprovado")

if __name__ == "__main__":
    unittest.main()