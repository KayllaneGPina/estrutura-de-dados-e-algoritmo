''' 

1. Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão.
2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
   Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
   Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
   O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
   
''' 

# Exercício 1
a = 40
b = 10

soma = a + b 
subtracao = a - b 
multiplicacao = a * b 
divisao = a / b 
print(f'Adição: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}')

# Exercício 2
# 12 km -> 1 L
velocidade = int(input('Digite a velocidade média da viagem: ')) # Em Km/H
tempo = int(input('Digite o tempo da viagem: ')) # Em Hrs
distancia = velocidade * tempo # Em km
litros_usados = distancia / 12

print(f'A velocidade média foi {velocidade} km/h.')
print(f'O tempo gasto na viagem foi de {tempo} hrs.')
print(f'A distânica percorrida foi de {distancia} km.')
print(f'A quantidade de listros usados na viagem foi de {round(litros_usados, 1)} L')

