'''
Tratamento de erros e exceções
    NameError: variável nao foi definida
    TypeError: tipos de dados incompatíveis
    RuntimeError: erro de execução
    SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
    ZeroDivisionError: divisão por zero
    IndexError: índice está fora da coleção
'''

# 1 -SyntaxError
# 3 = 4

# NameError
# print('Meu nome é', nome)

# ZeroDivisionError
# print(3 / 0)

# TypeError
# 2.3 / 'cachorro'

# IndexError
c = [1,2,3,4,5,6]
# print(c[9])

# Tratamento de erros
while True:
    try:
        n = int(input('Digite um número inteiro: '))
    except: 
        print("Valor inválido")
    else:
        print(f'Valor digitado é {n}')
        break
    
while True:
    try:
        p = int(input('Digite um número: '))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'O valor digitado foi {p}')
        break