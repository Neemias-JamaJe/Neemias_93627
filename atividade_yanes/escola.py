class Escola:
    def calcular_media(self, notas):
        if not notas:
            return 0
        return sum(notas) / len(notas)

    def verificar_status(self, notas):
        media = self.calcular_media(notas)
        if media >= 7.0:
            return "Aprovado"
        return "Reprovado"