class Programa():

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._likes = 0
        self.ano = ano

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

starWars = Filme('star wars: o despertar da força', 2015, "2h 16m")

starWars.dar_like()
starWars.dar_like()

print(f'Nome: {starWars.nome} - Ano: {starWars.ano} - duracao: {starWars.duracao} - likes: {starWars.likes}')

atlanta = Serie('Atlanta', 2018, 2)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - likes: {atlanta.likes}')