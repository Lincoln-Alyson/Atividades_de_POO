class Carro:

    def __init__(self):
        self.quilometragem = 0
        self.combustivel = 0
        self.passageiros = 0
        self.limite_passageiros = 2
        self.limite_combustivel = 100

    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.combustivel

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < self.limite_passageiros:
            self.passageiros += 1
            return True
        else:
            return False

    def desembarcar(self):
        if self.passageiros > 0:
            self.passageiros -= 1
            return True
        else:
            return False


    def dirigir(self, distancia):
        if self.passageiros > 0 and self.combustivel > 0:
            if self.combustivel >= distancia:
                self.quilometragem += distancia
                self.combustivel -= distancia
                return f'Percorridos {distancia} km.'
            else:
                distancia_possivel = self.combustivel
                self.quilometragem += distancia_possivel
                self.combustivel -= distancia_possivel
                return f'Percorridos {distancia_possivel} km. Combustível insuficiente para a viagem completa.'
        else:
            return False

    def abastecer(self, quantidade):
        if quantidade > 0 and self.combustivel + quantidade <= self.limite_combustivel:
            self.combustivel += quantidade
            return True
        elif quantidade + self.combustivel > self.limite_combustivel:
            return False

