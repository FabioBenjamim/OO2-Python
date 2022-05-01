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

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def __str__(self):
       return f'Nome: {self.nome} - Ano: {self.ano} - likes: {self .likes}'

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - duracao: {self.duracao} - likes: {self .likes}'

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - likes: {self.likes}'

class PlayList():

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

starWars = Filme('star wars: o despertar da força', 2015, "2h 16m")
atlanta = Serie('Atlanta', 2018, 2)
batman = Filme('Batman', 2022, "2h 56m")
demolidor = Serie('Demolidor', 2016, 2)

demolidor.dar_like()
batman.dar_like()
batman.dar_like()
starWars.dar_like()
starWars.dar_like()
starWars.dar_like()

filmes_series = [starWars, atlanta, demolidor, batman]

playlist_fim_de_semana = PlayList('fim de semana', filmes_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho: {len(playlist_fim_de_semana)}')