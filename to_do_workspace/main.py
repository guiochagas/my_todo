import sqlite3
from time import sleep

# CONEXÃO GLOBAL COM O BANCO DE DADOS 
conexao = sqlite3.connect('to-do-database.db')
c = conexao.cursor()

# RENUMERAR IDS DO BANCO DE DADOS
def renumerar_ids():
    c.execute("SELECT id FROM tasks ORDER BY id")
    ids = c.fetchall()

    for i, (id,) in enumerate(ids, start=1):
        c.execute("UPDATE tasks SET id = ? WHERE id = ?", (i, id))
    
    conexao.commit()

# CRIAR TABELA
def criar_tabela():
    conexao = sqlite3.connect('to-do-database.db')
    c = conexao.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks
            (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarefa text NOT NULL,
            status INTEGER

            )""")
    conexao.commit()
    conexao.close()


# INSERIR NOVA TAREFA
def inserir_tarefa(tarefa):
    conexao = sqlite3.connect('to-do-database.db')
    c = conexao.cursor()
    c.execute(f"INSERT INTO tasks (tarefa, status) VALUES ('{tarefa}', 0)")
    conexao.commit()
    conexao.close()

    print('Adicionando tarefa...')
    sleep(1)
    print('Tarefa adicionada!')
    sleep(1)
    print()


# EXIBIR TAREFAS
def exibir_tarefa():

    conexao = sqlite3.connect('to-do-database.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM tasks")
    conexao.commit()

    dados = c.fetchall()
    cont = 1

    for dado in dados:
        print(f'TAREFA {cont}: {dado[1]}')
        cont += 1
    
    sleep(1)
    print()

    conexao.close()


#ATUALIZAR TAREFA
def atualizar_tarefa():
    exibir_tarefa()

    conexao = sqlite3.connect('to-do-database.db')
    c = conexao.cursor()
    c.execute("UPDATE tasks SET tarefa = {tarefa_alterada} WHERE id = {id_selecionado}")
    conexao.commit()
    conexao.close()


def excluir_tarefa(tarefa_excluida):
    c.execute("DELETE FROM tasks WHERE id = ?", (tarefa_excluida,))

    print('Excluindo tarefa...')
    sleep(1)
    print('Tarefa excluida com sucesso!')
    sleep(1)

    conexao.commit()


# USER EXPERIENCE
while True:
    renumerar_ids()
    
    print()
    print(f"""{'== COMANDOS ==':^22}
[1] - INSERIR TAREFA
[2] - EXIBIR TAREFAS
[3] - ATUALIZAR TAREFA
[4] - DELETAR TAREFA
[5] - SAIR
{'='*23}""")
    
    

    user = int(input('Selecione uma opção:\n'))
    print()

    # INSERIR
    if user == 1:
        tarefa = str(input('NOVA TAREFA: '))
        inserir_tarefa(tarefa)

    # EXIBIR
    elif user == 2:
        exibir_tarefa()

    # ATUALIZAR
    elif user == 3:
        atualizar_tarefa()
        alterar = int(input('Selecione uma tarefa para alterar:\n'))

    # DELETAR
    elif user == 4:
        exibir_tarefa()
        user_delete = int(input('Selecione uma tarefa para excluir: '))
        excluir_tarefa(user_delete)

    # ENCERRAR PROGRAMA
    elif user == 5:
        print('ENCERRANDO...')
        sleep(1)
        print('Até a próxima')
        sleep(1)
        break
