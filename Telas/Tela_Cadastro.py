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
        #    Nome
        label_nome = customtkinter.CTkLabel(self, text="Nome do Produto:")
        self.nome = customtkinter.CTkEntry(self, placeholder_text="")
        label_nome.pack(pady=10)
        self.nome.pack(pady=10)

        #    CAtegorias
        label_categoria = customtkinter.CTkLabel(self, text="Categorias :")
        self.categoria = customtkinter.CTkComboBox(self, values = ["Furadeiras e Parafusadeiras",
                                                            "Chaves/Parafusadeiras de Impacto",
                                                            "Esmerilhadeiras", "serras", "Lixadeiras", "Impacto e aperto",
                                                            "Solda e corte termico", "Ar e Pressão", "Medição e Nivelamento",
                                                            "Construção Pesada", "detalhe e acabamento"])
        label_categoria.pack(pady=10)
        self.categoria.pack(pady=10)

        #    Tipos
        label_tipo = customtkinter.CTkLabel(self, text="Tipos:")
        self.tipo = customtkinter.CTkComboBox(self, values = ["Bateria", "Eletrica", "Pneumatica"])
        label_tipo.pack(pady=10)
        self.tipo.pack(pady=10)

        #    Marcas
        label_marca = customtkinter.CTkLabel(self, text="Marcas:")
        self.marca = customtkinter.CTkComboBox(self, values = ["NewBeat", "StarTool", "Bosch", "Vonder", "Tramontina"])
        label_marca.pack(pady=10)
        self.marca.pack(pady=10)

        #    Codigo
        label_codigo = customtkinter.CTkLabel(self, text="Codigo do Produto:")
        self.codigo = customtkinter.CTkEntry(self, placeholder_text="")
        label_codigo.pack(pady=10)
        self.codigo.pack(pady=10)

        #    Quantidade
        label_quantidade = customtkinter.CTkLabel(self, text="Quantidade do Produto:")
        self.quantidade = customtkinter.CTkEntry(self, placeholder_text="")
        label_quantidade.pack(pady=10)
        self.quantidade.pack(pady=10)

#    Salvar cadastro do produto
        self.botao_salvar = customtkinter.CTkButton(self, text="Salvar Produto", command=self.salvar_produto)
        self.botao_salvar.pack(pady=20)

    def salvar_produto(self):
        print(self.categoria.get())
        print(self.tipo.get())
        print(self.marca.get())
        print(self.nome.get())
        print(self.codigo.get())
        print(self.quantidade.get())

#    Adicionando ao banco de dados
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

        cursor.execute("""INSERT INTO produtos (categoria, tipo, marca, nome, codigo, quantidade)
                        VALUES (?, ?, ?, ?, ?, ?) """,
             (self.categoria.get(),
                        self.tipo.get(),
                        self.marca.get(),
                        self.nome.get(),
                        self.codigo.get(),
                        self.quantidade.get()))

        conexao.commit()
        conexao.close()
        print("Produto salvo!")




