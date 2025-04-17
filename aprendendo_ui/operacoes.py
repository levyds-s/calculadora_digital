import math


class Operacoes:
    def __init__(self):
        pass

    def tranformar_em_float(self, lista):
        return [float(i) for i in lista]

    def somar_numeros(self, lista):
        return sum(lista)

    def multiplicacao(self, lista):
        return math.prod(lista)

    def subtracao(self, lista):
        sub = lista[0]
        for i in range(1, len(lista)):
            sub -= lista[i]
        return sub

    def divisao(self, lista):
        div = lista[0]
        for i in range(1, len(lista)):
            div /= lista[i]
        return div
