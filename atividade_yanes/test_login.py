import unittest 

from sistema import Autenticacao

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.auth = Autenticacao()

# OS PRIMEIROS 4 TESTES SÃO DE LOGIN, OS PRÓXIMOS 2 PARA CADASTRO

# Teste para login válido
    def test_login_valido(self):
        #CENÁRIO
        usuario = "admin"
        senha = "123"

        #EXECUÇÃO
        resultado = self.auth.login(usuario, senha)

        #VERIFICAÇÃO
        self.assertTrue(resultado)

# Teste para login inválido

    def test_login_invalido(self):
        #CENÁRIO
        usuario = "admin"
        senha = "errada"

        #EXECUÇÃO
        resultado = self.auth.login(usuario, senha)

        #VERIFICAÇÃO
        self.assertFalse(resultado)


# Teste para usuário vazio no login

    def test_usuario_vazio(self):
        #CENÁRIO
        usuario = ""
        senha = "123"

        #EXECUÇÃO
        resultado = self.auth.login(usuario, senha)

        #VERIFICAÇÃO
        self.assertEqual(resultado, "Erro, Usuário Vazio!")

# Teste para senha vazia no login

    def test_senha_vazia(self):
        #CENÁRIO
        usuario = "admin"
        senha = ""

        #EXECUÇÃO
        resultado = self.auth.login(usuario, senha)

        #VERIFICAÇÃO
        self.assertEqual(resultado, "Erro, Senha Vazia!")

# TESTES DE CADASTRO (PRÓXIMOS 2)

# Teste cadastro válido

    def test_cadastro_email_valido(self):
        #CENÁRIO
        email = "teste@exemplo.com"

        #EXECUÇÃO
        resultado = self.auth.cadastrar_email(email)

        #VERIFICAÇÃO
        self.assertTrue(resultado)

# Teste para cadastro email inválido
   
    def test_cadastro_email_invalido(self):
                #CENÁRIO
        email = "email_sem_arroba.com"

        #EXECUÇÃO
        resultado = self.auth.cadastrar_email(email)

        #VERIFICAÇÃO
        self.assertEqual(resultado, "Erro, Email inválido")