# Cria uma lista vazia e adicionar todos os alunos da turma nela, quando terminar os alunos você imprime a lista.
lista = []
for nome in range(1,20):
    nome = input("Digite o nome do aluno: ou digite 'fim' para parar:")
    if nome == 'fim':
        break
    lista.append (nome)

print("Nome dos alunos:",lista)
