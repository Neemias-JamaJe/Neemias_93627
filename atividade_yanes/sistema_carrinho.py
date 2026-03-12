class CarrinhoDeCompras:
    def __init__(self):
        # Inicializa o estado do carrinho
        self.itens = []
        self.precos = []

    def adicionar_item(self, nome_item, preco):
        self.itens.append(nome_item)
        self.precos.append(preco)

    def remover_item(self, nome_item):
        if nome_item in self.itens:
            # Descobre o índice do item para remover o preço correspondente também
            indice = self.itens.index(nome_item)
            self.itens.pop(indice)
            self.precos.pop(indice)

    def listar_itens(self):
        return self.itens

    def calcular_total(self):
        # Soma todos os valores da lista de preços
        return sum(self.precos)