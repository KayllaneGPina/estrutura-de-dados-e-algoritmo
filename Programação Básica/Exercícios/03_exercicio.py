'''
1. Ler 5 notas e informar a média

2. Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
'''

#Exercício 1
while True:
    nota_1 = int(input('Digite sua nota: '))
    nota_2 = int(input('Digite sua nota: '))
    nota_3 = int(input('Digite sua nota: '))
    nota_4 = int(input('Digite sua nota: '))
    nota_5 = int(input('Digite sua nota: '))
    
    media = int((nota_1 + nota_2 + nota_3 + nota_4 + nota_5)) / 5
    
    print(f'Sua média foi: {media:.1f}')
    break
     
# Exercício 2
for i in range(11):
    tabuada = 3 * i
    print(f'3 X {i} = {tabuada}')