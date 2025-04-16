from operacoes import Operacoes


class Interpretar:
    def __init__(self, string):
        self.string = string
        self.op = Operacoes
        self.resultado = 0

    def interpretar(self):
        if "+" in self.string:
            return self.soma()
        elif "*" in self.string:
            return self.mult()
        elif "-" in self.string:
            pass
        elif "/" in self.string:
            pass

    def soma(self):
        self.lista_de_numeros = self.string.split("+")
        self.resultado = self.op.tranformar_em_float(
            self, self.lista_de_numeros)
        return self.op.somar_numeros(self, self.resultado)

    def mult(self):
        self.lista_de_numeros = self.string.split("*")
        self.resultado = self.op.tranformar_em_float(
            self, self.lista_de_numeros)
        return self.op.multiplicacao(self, self.resultado)
