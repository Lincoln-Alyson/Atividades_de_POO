from item import Item
from moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volume = 0
        self.volumemaximo = volumeMaximo
        self.VolumeRestante = self.volumemaximo - self.volume
        self.itens_do_cofre = ''
        self.soma_de_moedas = 0
        self.quebrou = False

    def getVolume(self):
        return self.volume

    def getVolumeMaximo(self):
        return self.volumemaximo

    def getVolumeRestante(self):
        return self.VolumeRestante

    def add(self, item: Item):
        return False

    def add(self, moeda: Moeda):
        return False

    def obterItens(self):
        return "vazio"

    def obterMoedas(self):
        return -1

    def taInteiro(self):
        return False

    def quebrar(self):
        return False