from datetime import datetime


class pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return
        
        if self.falando:
            print(f"{self.nome} está falando, não pode comer.")
        
        self.comendo = True
        print(f"{self.nome} está comendo {alimento}.")
    
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        
        self.comendo = False
        print(f"{self.nome} parou de comer.")
        
    def falar(self, assunto):
        if self.falando:
            print(f"{self.nome} já está falando.")
            return
        
        if self.comendo:
            print(f"{self.nome} está comendo, nao pode falar.")
            return     
           
        self.falando = True
        print(f"{self.nome} está falando sobre {assunto}.")
        
    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando")
            return
        
        self.falando = False
        print(f"{self.nome} parou de falar.")
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
    def ano_nascimento(self):
        print(f"{self.nome} nasceu em {self.get_ano_nascimento()}")
        
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)