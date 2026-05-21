import customtkinter
import Banco_De_Dados.database
from Telas.Tela_Inicial import TelaInicial
from Telas.Tela_Cadastro import TelaCadastro
from Telas.Tela_Estoque import TelaEstoque

app = customtkinter.CTk()
app.geometry("1200x700")
app.title("Sistema de Estoque")


def abrir_cadastro():
    tela_inicial.pack_forget()
    tela_cadastro.pack(fill="both", expand=True)

def abrir_estoque():
    tela_inicial.pack_forget()
    tela_estoque.pack(fill="both", expand=True)


def voltar_inicio():
    tela_cadastro.pack_forget()
    tela_estoque.pack_forget()
    tela_inicial.pack(fill="both", expand=True)


tela_inicial = TelaInicial(app, abrir_cadastro, abrir_estoque)
tela_cadastro = TelaCadastro(app, voltar_inicio)
tela_estoque = TelaEstoque(app, voltar_inicio)
tela_inicial.pack(fill="both", expand=True)



app.mainloop()


