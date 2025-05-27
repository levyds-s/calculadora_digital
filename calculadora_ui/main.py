import tkinter as tk
import math


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Calculadora Master")
        self.root.configure(background="gray1")
        self.botoes = []
        self.linhas = []
        self.entradas = []
        self.criar_entradas()
        self.criar_linhas()
        self.linhas_de_numeros = self.linhas[1:]
        self.linhas_de_numeros.reverse()
        self.criar_botoes()
        self.calculo = []

    def criar_linhas(self):
        for i in range(5):
            linha = tk.Frame(self.root)
            linha.pack(fill="both", expand=True)
            self.linhas.append(linha)

    def criar_entradas(self):
        self.valores_digitados = ""
        self.entrada = tk.Label(
            self.root, text=self.valores_digitados, foreground="snow", background="gray1")
        self.entrada.pack(fill="both", expand=True)
        # self.entradas.append(entrada)

    def criar_botoes(self):
        operadores = ["AC", "X", "%", "÷"]
        for i in operadores:
            button = tk.Button(
                self.linhas[0], text=i, background="gray1", foreground="snow", command=self.gerar_evento(i))
            button.pack(side=tk.LEFT, fill="both", expand=True)
            self.botoes.append(button)

        for i in range(10):
            button = tk.Button(
                self.linhas_de_numeros[(math.ceil(i/3))], text=i, background="gray1", foreground="snow", command=self.gerar_evento_para_numero(i))
            button.pack(side=tk.LEFT, fill="both", expand=True)
            self.botoes.append(button)

        sinais = ["x", "-", "+", "="]
        for i in range(4):
            button = tk.Button(
                self.linhas[i+1], text=sinais[i], background="gray1", foreground="snow", command=self.gerar_evento_para_sinal(sinais[i]))
            button.pack(side=tk.LEFT, fill="both", expand=True)
            self.botoes.append(button)

    def gerar_evento_para_numero(self, id):
        def atualizar_label():
            self.valores_digitados += str(id)
            self.entrada.config(text=self.valores_digitados)
            print(self.valores_digitados)
        return atualizar_label

    def gerar_evento(self, id):
        def funcao():
            if id == "AC":
                self.valores_digitados = ""
            elif id == "X":
                self.valores_digitados = self.valores_digitados[:-1]
            self.entrada.config(text=self.valores_digitados)
        return funcao

    def gerar_evento_para_sinal(self, id):
        def sinal():
            self.calculo.append(int(self.valores_digitados))
            self.calculo.append(id)
            print(self.calculo)
        return sinal


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
