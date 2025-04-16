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
        sub = 0
        for numero in lista:
            sub -= numero
        return sub

    def divisao(self, numero1, numero2):
        return numero1/numero2
