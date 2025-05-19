import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Calculadora Master")
        self.root.configure(background="gray8")
        self.botoes = []
        self.linhas = []
        self.entradas = []
        self.criar_entradas()
        self.criar_linhas()
        self.linhas_de_numeros = self.linhas[1:]
        self.linhas_de_numeros.reverse()
        self.criar_botoes()

    def criar_linhas(self):
        for i in range(5):
            linha = tk.Frame(self.root)
            linha.pack(fill="both", expand=True)
            self.linhas.append(linha)

    def criar_entradas(self):
        for i in range(2):
            entrada = tk.Entry(self.root)
            entrada.pack(fill="both", expand=True)
            self.entradas.append(entrada)

    def criar_botoes(self):
        operadores = ["AC", "X", "%", "÷"]
        for i in operadores:
            button = tk.Button(self.linhas[0], text=i)
            button.pack(side=tk.LEFT, fill="both", expand=True)
            self.botoes.append(button)

        for i in range(10):
            button = tk.Button(self.linhas_de_numeros[(i//3)], text=i)
            button.pack(side=tk.LEFT, fill="both", expand=True)
            self.botoes.append(button)

        sinais = ["x", "-", "+", "="]
        for i in range(1, 5):
            button = tk.Button(self.linhas[i], text=sinais[i-1])
            button.pack(side=tk.LEFT, fill="both", expand=True)
            self.botoes.append(button)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
