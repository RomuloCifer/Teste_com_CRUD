from pathlib import Path
import sqlite3
from typing import Any, List, Optional, Tuple

# Configurações de Banco de Dados (variáveis globais aqui são aceitáveis para a demo)
ROOT_DIR = Path(__file__).parent
DB_NAME = 'my_db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

def get_connection() -> sqlite3.Connection:
    """Função de fábrica para obter uma nova conexão de banco de dados."""
    return sqlite3.connect(DB_FILE)