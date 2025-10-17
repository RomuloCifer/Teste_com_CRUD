# aluno_service.py

from typing import List, Any, Optional
from aluno_repositorio import AlunoRepository, AlunoData

class AlunoService:
    """
    Camada de Serviço: Responsável por implementar as regras de negócio
    e garantir a validade dos dados antes de chamar o Repositório.
    """
    def __init__(self):
        # Injeção da Dependência
        self.repository = AlunoRepository()
        self.repository.create_table() # Garante que a tabela existe

    def adicionar_aluno(self, nome: str, serie: int, nota: float) -> int:
        """
        Adiciona um aluno após validar a nota e o nome.
        Qualquer regra deve ser implementada aqui.
        """
        # --- Regra (Validação) ---
        if not (0.0 <= nota <= 10.0):
            # Lançar exceções claras é uma prática sênior.
            raise ValueError("Erro: A nota deve estar entre 0.0 e 10.0.")
            
        if not nome or len(nome.strip()) < 3:
            raise ValueError("Erro: O nome deve ter pelo menos 3 caracteres.")
            
        return self.repository.insert_aluno(nome, serie, nota)

    def obter_aluno_por_id(self, aluno_id: int) -> Optional[AlunoData]:
        """Busca um aluno."""
        return self.repository.select_one(aluno_id)

    def deletar_aluno(self, aluno_id: int) -> None:
        """Remove um aluno."""
        self.repository.delete_aluno(aluno_id)
        
    def obter_todos_alunos(self) -> List[AlunoData]:
        """Retorna todos os alunos do repositório."""
        return self.repository.select_all()