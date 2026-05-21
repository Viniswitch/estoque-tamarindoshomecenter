import customtkinter

class TelaEstoque(customtkinter.CTkFrame):
    def __init__(self, master, voltar_inicio):
        super().__init__(master)
        titulo = customtkinter.CTkLabel(self, text="Estoque dos Produtos", font=("Arial", 30))
        titulo.pack(pady=20)

        botao_voltar = customtkinter.CTkButton(self, text="Voltar", command=voltar_inicio)
        botao_voltar.pack(pady=20)


