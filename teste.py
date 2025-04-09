alunos = []
while True:
    aluno = input('digite nome do aluno: ')
    alunos.append(aluno)

    resposta = input('deseja continuar? (s/n)')
    if resposta.lower() != 's':
        break

print("\nLista de alunos: ")
for aluno in alunos:
    print(aluno)
