class Filme: 
    def __init__(self, nomeFilme, duracFilme, anolancFilme, generoFilme):
        self.nomeFilme = nomeFilme
        self.duracFilme = duracFilme
        self.anolanFilme = anolancFilme
        self.generoFilme = generoFilme


class Serie:
    def __init__(self, nomeSerie, duracEp, anolancSerie, generoSerie, temporada):
        self.nomeSerie = nomeSerie
        self.duraEp = duracEp
        self.anolancSerie = anolancSerie
        self.generoSerie = generoSerie
        self.temporada = temporada