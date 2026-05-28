import customtkinter
import sqlite3

class TelaEstoque(customtkinter.CTkFrame):
    def __init__(self, master, voltar_inicio):
        super().__init__(master)
        titulo = customtkinter.CTkLabel(self, text="Estoque dos Produtos", font=("Arial", 30))
        titulo.pack(pady=20)

#    Botão para voltar para a tela inicial
        botao_voltar = customtkinter.CTkButton(self, text="Voltar", command=voltar_inicio)
        botao_voltar.pack(pady=20)

#    Banco de dados
        conexao = sqlite3.connect("Banco_De_Dados/estoque.db")
        cursor = conexao.cursor()

#    Buscar produtos
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

#    Scrollable Frame
        scroll = customtkinter.CTkScrollableFrame(self)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

#    Criando os Cards
        for produto in produtos:
            frame_produto = customtkinter.CTkFrame(scroll)
            frame_produto.pack(fill="x", padx=10, pady=10)

            nome = customtkinter.CTkLabel(frame_produto,text=f"Nome: {produto[4]}")
            nome.pack(anchor="w", padx=10, pady=2)

            categoria = customtkinter.CTkLabel(frame_produto,text=f"Categoria: {produto[1]}")
            categoria.pack(anchor="w", padx=10, pady=2)

            quantidade = customtkinter.CTkLabel(frame_produto,text=f"Quantidade: {produto[6]}")
            quantidade.pack(anchor="w", padx=10, pady=2)



        conexao.close()


