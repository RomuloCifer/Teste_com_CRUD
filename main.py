from aluno_service import AlunoService
from sqlite3 import IntegrityError

def run_application_demo():
    service = AlunoService() 
    
    # --- Teste de Inserção e Validação ---
    try:
        # Insert válido
        id_jorgin = service.adicionar_aluno('Jorgin do Pneu', 5, 8.5)
        print(f"✅ Aluno 'Jorgin do Pneu' inserido com ID: {id_jorgin}")
        # Teste de validação: nota inválida
        service.adicionar_aluno('Aluno Falho', 10, 11.0) 
        
    except ValueError as e:
        print(f"🛑 Erro esperado: {e}")
        
    except IntegrityError:
        print("⚠️ Dados já existem no banco. Continuando...")


    
    # --- Teste de Leitura ---
    service.repository.update_aluno_nota(id_jorgin, 9.9)
    print(f"✏️ Nota do aluno {id_jorgin} atualizada para 9.9.")
    
    aluno = service.obter_aluno_por_id(id_jorgin)
    print(f"🔍 Aluno após update: {aluno}")
    
    # --- Teste de Remoção ---
    service.deletar_aluno(id_jorgin)
    print(f"🗑️ Aluno com ID {id_jorgin} deletado.")
    
    # --- Teste de Leitura Geral ---
    print("\nLista de todos os alunos restantes:")
    for aluno in service.obter_todos_alunos():
        print(aluno)


if __name__ == '__main__':
    run_application_demo()