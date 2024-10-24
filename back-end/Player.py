class Player:
    def __init__(self):
        self.nome = ""
        self.email = ""
        self.telefone = ""

    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getTelefone(self):
        return self.telefone

    def setNome(self, nome):
        self.nome = nome

    def setEmail(self, email):
        self.email = email

    def setTelefone(self, telefone):
        self.telefone = telefone


