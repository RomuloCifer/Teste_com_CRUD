# aluno_repository.py

from typing import Any, List, Optional, Tuple
from pathlib import Path
from db_connector import get_connection, DEFAULT_DB_FILE, Connection

# Tipo que representa os dados do aluno: (id, nome, serie, nota)
AlunoData = Tuple[int, str, int, float] 
TABLE_NAME = 'alunos'

class AlunoRepository:
    """
    Essa classe só cuida de conversar com o banco de dados.
    É tipo o tradutor entre nosso código Python e o SQLite.
    """
    def __init__(self, db_file: str | Path = DEFAULT_DB_FILE):
        # Guarda qual arquivo de banco vamos usar (ou ':memory:' pra testes)
        self._db_file = db_file 

    def _get_connection(self) -> Connection:
        """Pega uma conexão pro banco que configuramos."""
        return get_connection(self._db_file)

    def create_table(self):
        """Cria a tabela dos alunos se ainda não existir."""
        with self._get_connection() as con: 
            con.execute(
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, serie INTEGER, nota REAL)')
            con.commit() 

    def insert_aluno(self, nome: str, serie: int, nota: float) -> int:
        """Adiciona um aluno novo no banco e devolve o ID que foi criado."""
        query = f'INSERT INTO {TABLE_NAME} (nome, serie, nota) VALUES (?, ?, ?)'
        with self._get_connection() as con:
            con.execute(query, (nome, serie, nota))
            con.commit() 
            # Pega o ID que o banco acabou de gerar
            return con.execute("SELECT last_insert_rowid()").fetchone()[0]

    def select_one(self, aluno_id: int) -> Optional[AlunoData]:
        """Procura um aluno específico pelo ID."""
        query = f'SELECT * FROM {TABLE_NAME} WHERE id = ?'
        with self._get_connection() as con:
            cur = con.execute(query, (aluno_id,))
            return cur.fetchone()

    def select_all(self) -> List[AlunoData]:
        """Pega todos os alunos que estão no banco."""
        query = f'SELECT * FROM {TABLE_NAME}'
        with self._get_connection() as con:
            cur = con.execute(query)
            return cur.fetchall()

    def delete_aluno(self, aluno_id: int) -> None:
        """Apaga um aluno do banco."""
        query = f'DELETE FROM {TABLE_NAME} WHERE id = ?'
        with self._get_connection() as con:
            con.execute(query, (aluno_id,))
            con.commit() 

    def update_aluno_nota(self, aluno_id: int, nova_nota: float) -> None:
        """Muda só a nota de um aluno."""
        query = f'UPDATE {TABLE_NAME} SET nota = ? WHERE id = ?'
        with self._get_connection() as con:
            con.execute(query, (nova_nota, aluno_id))
            con.commit()