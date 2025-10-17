from typing import Any, List, Optional, Tuple
# Importamos apenas a função de conexão, sem saber como ela funciona internamente
from db_connector import get_connection 


# Definimos o formato de dados esperado para leitura.

AlunoData = Tuple[int, str, int, float] 
TABLE_NAME = 'alunos'

class AlunoRepository:
    """
    Encapsula as operações de CRUD (Create, Read, Update, Delete) diretamente sobre
    a tabela 'alunos'. Esta classe NÃO deve conter (validações).
    """
    def __init__(self):

        pass 

    def create_table(self):
        """Cria a tabela de alunos se ela não existir."""
        # O 'with' garante que a conexão será fechada após a operação.
        with get_connection() as con: 
            con.execute(
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, serie INTEGER, nota REAL)')
            con.commit() # É crucial commitar DDL (Data Definition Language)

    def insert_aluno(self, nome: str, serie: int, nota: float) -> int:
        """Insere um novo aluno e retorna o ID gerado."""
        query = f'INSERT INTO {TABLE_NAME} (nome, serie, nota) VALUES (?, ?, ?)'
        with get_connection() as con:
            con.execute(query, (nome, serie, nota))
            con.commit() 
            # Retorna o ID para o Service poder usar em confirmações ou testes.
            return con.execute("SELECT last_insert_rowid()").fetchone()[0]

    def select_one(self, aluno_id: int) -> Optional[AlunoData]:
        """Busca um aluno pelo ID."""
        query = f'SELECT * FROM {TABLE_NAME} WHERE id = ?'
        with get_connection() as con:
            cur = con.execute(query, (aluno_id,))
            return cur.fetchone()

    def delete_aluno(self, aluno_id: int) -> None:
        """Remove um aluno pelo ID."""
        query = f'DELETE FROM {TABLE_NAME} WHERE id = ?'
        with get_connection() as con:
            con.execute(query, (aluno_id,))
            con.commit() # DML (Data Manipulation Language)

    def update_aluno_nota(self, aluno_id: int, nova_nota: float) -> None:
        """Atualiza a nota de um aluno específico."""
        query = f'UPDATE {TABLE_NAME} SET nota = ? WHERE id = ?'
        with get_connection() as con:
            con.execute(query, (nova_nota, aluno_id))
            con.commit()


    def select_all(self) -> List[AlunoData]:
        """Retorna todos os registros de alunos."""
        query = f'SELECT * FROM {TABLE_NAME}'
        with get_connection() as con:
            cur = con.execute(query)
            return cur.fetchall()