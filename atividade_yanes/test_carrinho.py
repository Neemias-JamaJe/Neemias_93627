import unittest
from sistema_carrinho import CarrinhoDeCompras

class TestCarrinho(unittest.TestCase):

    def setUp(self):
        self.carrinho = CarrinhoDeCompras()

    def test_adicionar_item(self):
        # CENÁRIO
        item = "Teclado"
        preco = 150.0
        
        # EXECUÇÃO
        self.carrinho.adicionar_item(item, preco)
        
        # VERIFICAÇÃO (Verificamos se o item está na lista de itens)
        self.assertIn(item, self.carrinho.listar_itens())

    def test_remover_item(self):
        # CENÁRIO
        self.carrinho.adicionar_item("Mouse", 50.0)
        
        # EXECUÇÃO
        self.carrinho.remover_item("Mouse")
        
        # VERIFICAÇÃO
        self.assertNotIn("Mouse", self.carrinho.listar_itens())

    def test_calcular_total(self):
        # CENÁRIO
        self.carrinho.adicionar_item("Monitor", 800.0)
        self.carrinho.adicionar_item("Cabo HDMI", 50.0)
        
        # EXECUÇÃO
        total = self.carrinho.calcular_total()
        
        # VERIFICAÇÃO
        self.assertEqual(total, 850.0)

if __name__ == "__main__":
    unittest.main()