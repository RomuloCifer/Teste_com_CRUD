# CRUD de Alunos com SQLite3

Este projeto é um CRUD (Create, Read, Update, Delete) simples em Python utilizando SQLite3 para gerenciar uma tabela de alunos.

## Funcionalidades
- Criação automática da tabela de alunos
- Inserção de um ou vários alunos
- Seleção de todos os alunos ou de um aluno específico
- Atualização de dados de um aluno
- Remoção de alunos

## Estrutura da Tabela
- `id` (INTEGER, chave primária, autoincremento)
- `nome` (TEXT)
- `serie` (INTEGER)
- `nota` (REAL)

## Como usar
1. Instale o Python 3.10+ e o SQLite3 (já incluso na maioria das instalações Python).
2. Clone este repositório.
3. Execute o arquivo principal para criar a tabela e testar as funções:

```bash
python alunos_crud.py
```

## Exemplo de uso
Veja o bloco `if __name__ == '__main__':` no arquivo principal para exemplos de inserção, atualização, seleção e remoção de alunos.

## Requisitos
- Python 3.10 ou superior

## Observações
- O banco de dados será criado no mesmo diretório do script.
- O código pode ser facilmente adaptado para outros tipos de dados ou tabelas.

---

Desenvolvido por Cifer.
