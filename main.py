import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Madalena8670',
    database='bdyoutube',
)
cursor = conexao.cursor()

# crud
nome_produto= "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto= "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #edita obanco de dados


cursor.close()
conexao.close()

# READ
#comando = f'SELECT * FROM vendas;'
#cursor.execute(comando)
#resultado = cursor.fetchall() # ler banco de dados
#print(resultado)

# UPDATE
"""nome_produto= "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto= "{nome_produto}"' #atualizar tabela vendas alterando o valor
cursor.execute(comando)
conexao.commit() #edita obanco de dados

"""

#DELETE
nome_produto= "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto= "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #edita obanco de dados
