# main.py

from aluno_service import AlunoService
from sqlite3 import IntegrityError

def run_application_demo():
    """
    Aqui é só pra mostrar como usar o sistema.
    Vai criar um service que usa o banco real (não de teste).
    """
    service = AlunoService() 
    
    print("--- TESTANDO O SISTEMA DE ALUNOS ---")

    # Vamos tentar adicionar um aluno normal
    try:
        id_jorgin = service.adicionar_aluno('Jorgin do Pneu', 5, 8.5)
        print(f"✅ Adicionou o 'Jorgin do Pneu' com ID: {id_jorgin}")
        
        # Agora vamos tentar algo que vai dar erro de propósito
        service.adicionar_aluno('Aluno Falho', 10, 11.0) 
        
    except ValueError as e:
        print(f"🛑 Deu erro como esperado: {e}")
        
    except IntegrityError:
        print("⚠️ Esse dado já existe no banco, mas vamos continuar...")

    # Vamos mudar a nota dele
    try:
        service.atualizar_nota(id_jorgin, 9.9)
        print(f"✏️ Mudou a nota do aluno {id_jorgin} pra 9.9")
    except Exception as e:
        print(f"Deu ruim na atualização: {e}")

    # Confere como ficou
    aluno = service.obter_aluno_por_id(id_jorgin)
    print(f"🔍 Dados do aluno depois da mudança: {aluno}")
    
    # Agora vamos remover ele
    service.deletar_aluno(id_jorgin)
    print(f"🗑️ Removeu o aluno {id_jorgin}")
    
    # Vê quem sobrou no banco
    print("\nQuem ainda tá cadastrado:")
    for aluno in service.obter_todos_alunos():
        print(aluno)


if __name__ == '__main__':
    run_application_demo()