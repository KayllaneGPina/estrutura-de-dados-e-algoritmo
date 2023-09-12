'''
1 - Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
    *ValueError*: se o usuário digitar um caracter
    *ZeroDivisionError*: se o usuário digitar zero e ocorrer erro na divisão
    *IndexError*: caso a divisão seja feita levando em consideração posições que não existem na lista
    *KeyboardInterrupt*: caso o usuário interrompa a execução

2 - Mostre uma mensagem personalizada na ocorrência de cada um desses erros
'''
while True:
    try:
        empty_list = []
        valor1 = float(input())
        valor2 = float(input())
        
        empty_list.append(valor1)
        empty_list.append(valor2)
        
        divisao = empty_list[0] / empty_list[1]
    except ValueError:
        print('Valor inválido')
    except ZeroDivisionError:
        if empty_list[1] == 0:
            print('Impossível dividir por 0')
    except IndexError:
        print('Erro! Índice inválido')
    except KeyboardInterrupt:
        print('Ação interrompida pelo usuário do usuário')
        break
    else:
        print(f'O resultado da divisão é: {divisao}')
        break