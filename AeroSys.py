from datetime import datetime

class Passageiro:
    def __init__(self, nome, documento, email):
        self.nome = nome
        self.documento = documento
        self.email = email

    def realizar_checkin(self):
        print(f"{self.nome} realizou o check-in.")
    
    def consultar_voo(self, voo):
        print(f"Status do voo {voo.numero}: {voo.status}.")

class Funcionario:
    def __init__(self, nome, cargo, matricula, senha):
        self.nome = nome
        self.cargo = cargo
        self.matricula = matricula
        self.senha = senha
        self.hora_saida = None
        self.hora_entrada = None

    def login(self, senha_digitada):
        if senha_digitada == self.senha:
            print(f"{self.nome} fez login com sucesso.")
            return True
        else:
            print("Senha incorreta.")
            return False

    def bater_ponto_entrada(self):
        self.hora_entrada = datetime.now()
        print(f"{self.nome} registrou entrada às {self.hora_entrada.strftime('%H:%M:%S')}.")

    def bater_ponto_saida(self):
        self.hora_saida = datetime.now()
        print(f"{self.nome} registrou saída às {self.hora_entrada.strftime('%H:%M:%S')}.")