class Carro:

    def __init__(self):
        self.quilometragem = 0
        self.combustivel = 0
        self.passageiros = 0



    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.combustivel

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            self.passageiros += 1
            return True
        else:
            return False

    def desembarcar(self):
        if 2 >= self.passageiros > 0:
            self.passageiros -= 1
            return True
        else:
            return False


    def dirigir(self, distancia):
        if self.passageiros != 0 and 100 > distancia > 0:
            if distancia <= self.combustivel:
                self.combustivel -= distancia
                self.quilometragem += distancia
                return True
        if distancia > 100:
            diferenca = distancia - 100
            self.combustivel = 0
            self.quilometragem += distancia - diferenca
            return False
        else:
            return False

    def abastecer(self, quantidade):
        if 0 < quantidade <= 100:
            self.combustivel += quantidade
        if quantidade > 100:
            self.combustivel = 100
            return True
        else:
            return False

