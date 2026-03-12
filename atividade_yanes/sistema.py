import re

class Autenticacao:
    def __init__(self):
        self.usuario_valido = "admin"
        self.senha_valida = "123"

    def login(self, usuario, senha):
        # Ajustado para bater exatamente com seus Assertions
        if not usuario:
            return "Erro, Usuário Vazio!"
        if not senha:
            return "Erro, Senha Vazia!"
        
        if usuario == self.usuario_valido and senha == self.senha_valida:
            return True
        return False

    def cadastrar_email(self, email):
        # Ajustado para usar a vírgula conforme seu erro no terminal
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(padrao, email):
            return True
        return "Erro, Email inválido"