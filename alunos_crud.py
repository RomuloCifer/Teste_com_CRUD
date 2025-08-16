from pathlib import Path
import sqlite3
from typing import Any, List, Optional

ROOT_DIR = Path(__file__).parent
DB_NAME = 'my_db.sqlite3'
TABLE_NAME = 'alunos'
DB_FILE = ROOT_DIR / DB_NAME

# USAR ESTA VARIAVEL PARA CONDIÇÃO DAS FUNÇÕES
CONDITION = 'id = ?'

def get_connection():
    return sqlite3.connect(DB_FILE)


def create_table():
    with get_connection() as con:
        con.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, serie INTEGER, nota REAL)')


def insert_aluno(nome: str, serie: int, nota: float) -> str:
    with get_connection() as con:
        con.execute(
            f'INSERT INTO {TABLE_NAME} (nome, serie, nota) VALUES (?, ?, ?)',
            (nome, serie, nota)
        )
    return f'Adicionado aluno {nome} com sucesso!'


def insert_alunos(alunos: List[dict | tuple]) -> None:
    with get_connection() as con:
        con.executemany(
            f'INSERT INTO {TABLE_NAME} (nome, serie, nota) VALUES (?, ?, ?)', alunos
        )


def delete_aluno(condicao: str, parametro: tuple) -> None:
    with get_connection() as con:
        con.execute(f'DELETE FROM {TABLE_NAME} WHERE {condicao}', parametro)


def select_all() -> List[Any]:
    with get_connection() as con:
        cur = con.execute(f'SELECT * FROM {TABLE_NAME}')
        return cur.fetchall()


def select_one(condicao: str, parametros: tuple) -> Optional[Any]:
    with get_connection() as con:
        cur = con.execute(f'SELECT * FROM {TABLE_NAME} WHERE {condicao}', parametros)
        return cur.fetchone()


def update_aluno(coluna: str, novo_valor: Any, condicao: str, parametros: tuple = ()) -> None:
    with get_connection() as con:
        con.execute(f'UPDATE {TABLE_NAME} SET {coluna} = ? WHERE {condicao}', (novo_valor, *parametros))


# Testando o código
# Cria e insere alguns dados na tabela
if __name__ == '__main__':
    create_table()
    insert_aluno('Jorgin do pneu', 5, 8.9)
    insert_alunos([
        ('Maria da silvan', 6, 7.5),
        ('Joao da silva Sauro', 9, 9.0),
        ('Marcos pereira jubiscleiton', 9, 4.5),
    ])

    # deleta aluno com o id 2
    delete_aluno(CONDITION, (2,))

    # atualiza a nota do aluno com o id 1
    update_aluno('nota', 10.0, CONDITION, (1,))

    # seleciona todos os alunos
    select_all()

    # seleciona o aluno com o id 1
    aluno = select_one(CONDITION, (1,))

    # imprime os dados do aluno
    print(aluno)

    # seleciona um aluno aleatório
    aluno_aleatorio = select_one(CONDITION, (4,))

    # imprime os dados do aluno aleatório
    print(aluno_aleatorio)