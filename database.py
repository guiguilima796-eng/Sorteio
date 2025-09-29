import psycopg2

parametros ={
    "host":"localhost",
    "dbname":"Sorteio",
    "user":"postgres",
    "password": "1234"
}

CriaTabelasNome = """
    create table if not exists nomes(
        id serial primary key,
        nome varchar(40) not null
    );
"""

def conecta_db():
    conexao = None

    try:
        conexao = psycopg2.connect(**parametros)
        print("Banco de Dados Conectado Com Sucesso!")
    except Exception as error:
        print("[ERRO] Banco de Dados não Conectado!",error)
    return conexao


def cria_tabel(conexao):
    try:
        with conexao.cursor() as cursor:
            cursor.execute(CriaTabelasNome)
            conexao.commit()
            print("Tabela Criada Com Sucesso!")
    except Exception as error:
        print("Erro ao Criar as Tabelas no DB",error)

def lista_Nomes(conexao):
    try:
        with conexao.cursor() as cursor:
            cursor.execute("Select *from nomes order by id;")
            return cursor.fetchall()
    except Exception as error:
        print("Erro ao Consultar os Nomes no DB",error)

def Inseri_Nomes(conexao,nome):
    try:
        contador = 0
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO nomes (nome) (%s) VALUES(nome,)")
            print("Nome cadastrado com sucesso!")
            conexao.commit()
            contador.cursor.rowcount()
            return contador
            return cursor.fetchall()
    except Exception as error:
        print("Erro ao Inserir os Nomes no DB",error)
        return contador
    
def remove_Nomes(conexao):
    try:
        contador = 0
        with conexao.cursor() as cursor:
            cursor.execute("delete from nomes")
            print("Nome cadastrado com sucesso!")
            conexao.commit()
            contador.cursor.rowcount()
            return contador
            return cursor.fetchall()
    except Exception as error:
        print("Erro ao Remover os Nomes no DB",error)
        return contador

def remove_nome(conexao,nome):
    try:
        print(conexao)
        with conexao.cursor() as cursor:
            cursor.execute("DELETE from nomes where lower(nome) = %s;", (str.lower(nome)),)
            conexao.commit()
            print("Nome Deletado com sucesso!")
    except Exception as error:
        print("Erro ao Remover o Nome no DB",error)

    
if __name__ == '__main__':
    conexao = conecta_db()
    if conexao:
        cria_tabel(conexao)
        conexao.close()  # importante fechar a conexão!