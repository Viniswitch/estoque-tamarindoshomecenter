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
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

#    Buscar produtos
        cursor.execute("SELECT * FROM produtos")

#    Mostrar Produtos
        produtos = cursor.fetchall()
        for produto in produtos:
            texto = f"""ID: {produto[0]}, Categoria: {produto[1]}, Tipo: {produto[2]}, Marca: {produto[3]},Nome: {produto[4]}
                     , codigo: {produto[5]}, quantidade: {produto[6]}"""
            label_produto = customtkinter.CTkLabel(self, text=texto, font=("Arial", 18), justify="left")
            label_produto.pack(pady=10)

        conexao.close()


