import customtkinter
import sqlite3
from tkinter import messagebox

class TelaCadastro(customtkinter.CTkFrame):
    def __init__(self, master, voltar_inicio):
        super().__init__(master)
        frame_formulario = customtkinter.CTkFrame(self, corner_radius=15)
        frame_formulario.pack(expand=True, padx=40, pady=40)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


#    Titulo
        titulo = customtkinter.CTkLabel(frame_formulario, text="Cadastro de Produtos", font=("Arial", 30))
        titulo.grid(row=0, column=0, columnspan=2, pady=(10, 25))

#    Botão para Sair
        botao_voltar = customtkinter.CTkButton(frame_formulario, text="Voltar", command=voltar_inicio)
        botao_voltar.grid(row=1, column=0, columnspan=2, pady=(8, 8))

#    Campos de cadastro

    #    Nome
        label_nome = customtkinter.CTkLabel(frame_formulario, text="Nome do Produto: ", width=220, anchor="w")
        self.nome = customtkinter.CTkEntry(frame_formulario, placeholder_text="")
        label_nome.grid(row=2, column=0, columnspan=1, pady=(8, 8), sticky="e")
        self.nome.grid(row=2, column=1,columnspan=1, pady=(8, 8), sticky="e")

        #    CAtegorias
        label_categoria = customtkinter.CTkLabel(frame_formulario, text="Categorias :", width=220, anchor="w")
        self.categoria = customtkinter.CTkComboBox(frame_formulario, values = ["Furadeiras e Parafusadeiras",
                                                            "Chaves/Parafusadeiras de Impacto",
                                                            "Esmerilhadeiras", "serras", "Lixadeiras", "Impacto e aperto",
                                                            "Solda e corte termico", "Ar e Pressão", "Medição e Nivelamento",
                                                            "Construção Pesada", "detalhe e acabamento"])
        label_categoria.grid(row=3, column=0, columnspan=1, pady=(8, 8), sticky="e")
        self.categoria.grid(row=3, column=1, columnspan=1, pady=(8, 8), sticky="w")

    #    Tipos
        label_tipo = customtkinter.CTkLabel(frame_formulario, text="Tipos: ", width=220, anchor="w")
        self.tipo = customtkinter.CTkComboBox(frame_formulario, values = ["Bateria", "Eletrica", "Pneumatica"])
        label_tipo.grid(row=4, column=0, columnspan=1, pady=(8, 8), sticky="e")
        self.tipo.grid(row=4, column=1, columnspan=1, pady=(8, 8), sticky="w")

    #    Marcas
        label_marca = customtkinter.CTkLabel(frame_formulario, text="Marcas: ", width=220, anchor="w")
        self.marca = customtkinter.CTkComboBox(frame_formulario, values = ["NewBeat", "StarTool", "Bosch", "Vonder",
                                                                           "Tramontina"])
        label_marca.grid(row=5, column=0, columnspan=1, pady=(8, 8), sticky="e")
        self.marca.grid(row=5, column=1, columnspan=1, pady=(8, 8), sticky="w")

    #    Codigo
        label_codigo = customtkinter.CTkLabel(frame_formulario, text="Codigo do Produto: ", width=220, anchor="w")
        self.codigo = customtkinter.CTkEntry(frame_formulario, placeholder_text="")
        label_codigo.grid(row=6, column=0, columnspan=1, pady=(8, 8), sticky="e")
        self.codigo.grid(row=6, column=1, columnspan=1, pady=(8, 8), sticky="w")

    #    Quantidade
        label_quantidade = customtkinter.CTkLabel(frame_formulario, text="Quantidade do Produto: ", width=220, anchor="w")
        self.quantidade = customtkinter.CTkEntry(frame_formulario, placeholder_text="")
        label_quantidade.grid(row=7, column=0, columnspan=1, pady=(8, 8), sticky="e")
        self.quantidade.grid(row=7, column=1, columnspan=1, pady=(8, 8), sticky="w")

#    Salvar cadastro do produto
        self.botao_salvar = customtkinter.CTkButton(frame_formulario, text="Salvar Produto", command=self.salvar_produto)
        self.botao_salvar.grid(row=8, column=0, columnspan=2, pady=(25, 10))

    def salvar_produto(self):

    #    Pegando os dados
        categoria = self.categoria.get()
        tipo = self.tipo.get()
        marca = self.marca.get()
        nome = self.nome.get()
        codigo = self.codigo.get()
        quantidade = self.quantidade.get()

    #    Verificação dos dados
        if categoria == "" or tipo == "" or marca == "" or nome == "" or codigo == "" or quantidade == "":
            messagebox.showerror("Erro","Preencha todos os campos!")
            return

    #    Conectando ao banco de dados
        conexao = sqlite3.connect("Banco_De_Dados/estoque.db")
        cursor = conexao.cursor()

    #    Verificando se o "produto" já existe no banco de dados
        cursor.execute("SELECT quantidade FROM produtos WHERE codigo = ?",(codigo,))
        produto_existente = cursor.fetchone()

    #    Caso já exista no banco de dados, atualiza a quantidade do "produto"
        if produto_existente:
            quantidade_atual = int(produto_existente[0])
            nova_quantidade = quantidade_atual + int(quantidade)
            cursor.execute("UPDATE produtos SET quantidade = ? WHERE codigo = ?",(nova_quantidade, codigo))
            messagebox.showinfo(title = "Atualizado", message = "Quantidade atualizada!")

    #    Caso não exista no banco de dados, adiciona
        else:
            cursor.execute("""INSERT INTO produtos(categoria, tipo, marca, nome, codigo, quantidade)
                              VALUES (?, ?, ?, ?, ?, ?)""",(categoria,tipo,marca,nome,codigo,quantidade))
            messagebox.showinfo(title="Sucesso", message="Produto salvo com sucesso!")
        conexao.commit()
        conexao.close()

    #    Limpar campos
        self.nome.delete(0, "end")
        self.codigo.delete(0, "end")
        self.quantidade.delete(0, "end")
        self.categoria.set("")
        self.tipo.set("")
        self.marca.set("")
