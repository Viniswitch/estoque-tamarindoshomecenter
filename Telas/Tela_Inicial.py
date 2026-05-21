import customtkinter


class TelaInicial(customtkinter.CTkFrame):
    def __init__(self, master, abrir_cadastro, abrir_estoque):
        super().__init__(master)
        titulo = customtkinter.CTkLabel(self, text="Tela Inicial", font=("Arial", 30))
        titulo.pack(pady=20)

        botao_cadastrar = customtkinter.CTkButton(self, text="Cadastrar Produto", command=abrir_cadastro)
        botao_cadastrar.pack(pady=20)

        botao_estoque = customtkinter.CTkButton(self, text="Estoque de Produtos", command=abrir_estoque)
        botao_estoque.pack(pady=20)
