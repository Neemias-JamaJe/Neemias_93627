class Loja:
    def calcular_desconto(self, valor, tipo_cliente):
        if tipo_cliente == "VIP":
            return valor * 0.70  # 30% de desconto
        return valor * 0.90      # 10% de desconto (comum)