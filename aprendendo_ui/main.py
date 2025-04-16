import tkinter as tk
from interpretar import Interpretar


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste")

        self.entry1 = tk.Entry(root, textvariable="separe por espaco")
        self.entry1.pack(padx=10, pady=5)

        self.sum_button = tk.Button(
            root, text="=", command=self.obter_valor)
        self.sum_button.pack(padx=10, pady=5)

        self.entry2 = tk.Entry(root)
        self.entry2.pack(padx=10, pady=5)

    def obter_valor(self):
        texto = self.entry1.get()
        print(type(texto))
        inter = Interpretar(texto)
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, inter.interpretar())


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
