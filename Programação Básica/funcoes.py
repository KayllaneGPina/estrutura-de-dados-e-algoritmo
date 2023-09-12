# Funções sem parametros
def mensagem() :
   print('Texto da função')
    
mensagem()

# Funções sem retorno
def mensagem2(texto) :
   print(texto)

mensagem2('Olá, mundo!')

# Função com passagem e retorno
def soma(a, b):
    return a + b

print(soma(2, 3))
help(soma)

# def monta_computador(memoria=64, armazenamento=4, cpu='Intel Core i9') # Chama de função  nomeada
def monta_computador(cpu='', armazenamento=0, memoria=0) :
   print(f'A configuração é: \n\t- CPU: {cpu}\n\t- Armazenameno: {armazenamento}Tb\n\t- Memória: {memoria}Gb')
    
monta_computador('Intel Core i9', 4, 64) # Chamada de função posicional

def maior_30(*args) :
   print(args)
   print(type(args))
   
   for num in args:
       if num > 30:
           print(num)
            
maior_30(10, 20, 30, 40, 50, 60)

def dados_pessoa(**kwargs):
    print(type(kwargs))
    
    for chave, valor in kwargs.items() :
        print(f'{chave}: {valor}')
        
dados_pessoa(nome='Kayllane', idade= 21, carreira='Desenvolvedora de software')

# Função com retorno
def soma_dois_numeros(num1, num2):
    soma = num1 + num2
    return soma

print(soma_dois_numeros(10, 20))

# Funções de uma linha
def soma(valor1, valor2): return valor1 + valor2
print(soma(1, 4))