import customtkinter
import sqlite3

class TelaCadastro(customtkinter.CTkFrame):
    def __init__(self, master, voltar_inicio):
        super().__init__(master)
        titulo = customtkinter.CTkLabel(self, text="Cadastro de Produtos", font=("Arial", 30))
        titulo.pack(pady=20)

#    Botão para Sair
        botao_voltar = customtkinter.CTkButton(self, text="Voltar", command=voltar_inicio)
        botao_voltar.pack(pady=20)

#    Campos de cadastro
        self.nome = customtkinter.CTkEntry(self, placeholder_text="Nome")
        self.nome.pack(pady=10)

        self.categoria = customtkinter.CTkComboBox(self, values = ["Furadeiras e Parafusadeiras",
                                                            "Chaves/Parafusadeiras de Impacto",
                                                            "Esmerilhadeiras", "serras", "Lixadeiras", "Impacto e aperto",
                                                            "Solda e corte termico", "Ar e Pressão", "Medição e Nivelamento",
                                                            "Construção Pesada", "detalhe e acabamento"])
        self.categoria.pack(pady=10)

        self.tipo = customtkinter.CTkComboBox(self, values = ["Bateria", "Eletrica", "Pneumatica"])
        self.tipo.pack(pady=10)

        self.marca = customtkinter.CTkComboBox(self, values = ["NewBeat", "StarTool", "Bosch", "Vonder", "Tramontina"])
        self.marca.pack(pady=10)

        self.codigo = customtkinter.CTkEntry(self, placeholder_text="Codigo do Produto")
        self.codigo.pack(pady=10)

#    Salvar cadastro do produto
        self.botao_salvar = customtkinter.CTkButton(self, text="Salvar Produto", command=self.salvar_produto)
        self.botao_salvar.pack(pady=20)

    def salvar_produto(self):
        print(self.categoria.get())
        print(self.tipo.get())
        print(self.marca.get())
        print(self.nome.get())
        print(self.codigo.get())

#    Adicionando ao banco de dados
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

        cursor.execute("""INSERT INTO produtos (categoria, tipo, marca, nome, codigo) VALUES (?, ?, ?, ?, ?) """,
             (self.categoria.get(),
                        self.tipo.get(),
                        self.marca.get(),
                        self.nome.get(),
                        self.codigo.get()))

        conexao.commit()
        conexao.close()
        print("Produto salvo!")




