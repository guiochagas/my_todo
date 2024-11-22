import sqlite3
from time import sleep

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
        print(f'TAREFA {cont}: {dado[1]} - STATUS: {dado[2]}')
        cont += 1
    
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



# USER EXPERIENCE
while True:
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

    if user == 1:
        tarefa = str(input('NOVA TAREFA: '))
        inserir_tarefa(tarefa)

    elif user == 2:
        exibir_tarefa()

    elif user == 3:
        atualizar_tarefa()
        alterar = int(input('Selecione uma tarefa para alterar:\n'))
