import numpy as np

'''
1. Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. 
Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados.

2. Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. 
Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média.

3. Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz.
matriz = np.array([[3, 4, 1], [3, 1, 5]])
'''

# Exercício 1
lista = []

for numeros in range(5):
    numeros = int(input())
    lista.append(numeros)

print(lista)

soma = 0
for numero in lista:
    soma += numero
    
print(f'A soma dos números da lista são: {soma}')


# Exercício 2
alunos = {'Maria': 10, 'João': 8, 'Pedro': 9.5}
print(alunos.keys())

for aluno in alunos.keys():
    print(f'Aluno: {aluno}, Nota = {alunos[aluno]}')
    
soma = 0
for nota in alunos.values():
    soma += nota
 
media = soma / 3
print(f'Media dos alunos: {media:.2f}')

# Exercício 3
matriz = np.array([[3, 4, 1], [3, 1, 5]])

for linhas in matriz:
    for coluna in linhas:
        print(coluna)
        
soma_array = np.sum(matriz)
print(f'A soma dos elementos da matriz é: {soma_array}')