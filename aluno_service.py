# aluno_service.py

from typing import List, Any, Optional
from pathlib import Path
from aluno_repositorio import AlunoRepository, AlunoData

class AlunoService:
    """
    Aqui ficam as regras de negócio do sistema. 
    O bacana dessa abordagem é que podemos injetar diferentes repositórios,
    tipo um de teste que usa memória em vez do banco real.
    """
    def __init__(self, db_file: str | Path = None):
        # Cria o repositório e já deixa a tabela pronta pra usar
        self.repository = AlunoRepository(db_file=db_file) 
        self.repository.create_table()

    def adicionar_aluno(self, nome: str, serie: int, nota: float) -> int:
        """Adiciona um aluno novo, mas antes verifica se tá tudo certo."""
        
        # Validações básicas - nada de nota impossível ou nome muito curto
        if not (0.0 <= nota <= 10.0):
            raise ValueError("Opa! A nota precisa estar entre 0 e 10.")
            
        if not nome or len(nome.strip()) < 3:
            raise ValueError("Nome muito curto! Precisa de pelo menos 3 caracteres.")
            
        return self.repository.insert_aluno(nome, serie, nota)

    def obter_aluno_por_id(self, aluno_id: int) -> Optional[AlunoData]:
        """Busca um aluno pelo ID."""
        return self.repository.select_one(aluno_id)

    def deletar_aluno(self, aluno_id: int) -> None:
        """Remove um aluno pelo ID."""
        self.repository.delete_aluno(aluno_id)
        
    def obter_todos_alunos(self) -> List[AlunoData]:
        """Retorna todos os alunos."""
        return self.repository.select_all()

    def atualizar_nota(self, aluno_id: int, nova_nota: float) -> None:
        """Muda a nota do aluno, mas só se ela for válida."""
        if not (0.0 <= nova_nota <= 10.0):
            raise ValueError("Eita! Essa nota não existe, tem que ser entre 0 e 10.")
        self.repository.update_aluno_nota(aluno_id, nova_nota)