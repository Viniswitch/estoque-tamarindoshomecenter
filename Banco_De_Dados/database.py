import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, tipo TEXT,
                                                       marca TEXT, nome TEXT, codigo TEXT, quantidade TEXT)""")

conexao.commit()
conexao.close()
