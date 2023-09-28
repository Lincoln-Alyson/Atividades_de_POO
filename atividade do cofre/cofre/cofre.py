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
        if self.volume == self.volumemaximo or self.quebrou:
            return False
        if self.volume <= self.VolumeRestante and item.volume <= self.volumemaximo:
            self.volume += item.volume
            if self.itens_do_cofre:
                self.itens_do_cofre += f", {item.descricao}"
            else:
                self.itens_do_cofre += item.descricao
                self.VolumeRestante = self.volumemaximo - self.volume
                return True
        else:
            return False

    def add(self, moeda: Moeda):
        self.moeda = moeda
        if self.volume == self.volumemaximo:
            return False
        if not self.quebrou:
            if 0 < moeda.value[1] <= self.VolumeRestante:
                self.volume += moeda.value[1]
                self.soma_de_moedas += moeda.value[0]
                self.VolumeRestante = self.volumemaximo - self.volume
                return True
        else:
            return False

    def obterItens(self):
        if self.quebrou:
            if self.itens_do_cofre:
                return self.itens_do_cofre
            else:
                return 'vazio'
        else:
            return None

    def obterMoedas(self):
        if self.quebrou == True:
            return self.soma_de_moedas
        else:
            return -1


    def taInteiro(self):
        if self.quebrou == False:
            return True

    def quebrar(self):
        if not self.quebrou:
            print('Seu cofrinho está quebrado!')
            self.quebrou = True
            return True
        else:
            print('O cofrinho já está quebrado!')
            return False