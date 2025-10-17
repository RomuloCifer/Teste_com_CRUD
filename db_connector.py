# db_connector.py

from pathlib import Path
import sqlite3
from sqlite3 import Connection

# Configuração do banco - onde fica o arquivo por padrão
ROOT_DIR = Path(__file__).parent
DEFAULT_DB_NAME = 'my_db.sqlite3'
DEFAULT_DB_FILE = ROOT_DIR / DEFAULT_DB_NAME

def get_connection(db_file: str | Path = DEFAULT_DB_FILE) -> Connection:
    """
    Cria uma conexão com o SQLite.
    
    Pode ser um arquivo real no disco ou ':memory:' pra usar só na RAM 
    (super útil quando você quer rodar testes sem bagunçar o banco real).
    """
    if isinstance(db_file, Path):
        db_file = str(db_file)
        
    return sqlite3.connect(db_file)