class Interpretar:
    def __init__(self, lista):
        self.lista_nova = []
        for string in lista:
            if (int(string) >= 0):
                self.lista_nova.append(int(string))
