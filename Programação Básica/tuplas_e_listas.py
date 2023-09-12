# Tuplas
print('--------------------TUPLAS--------------------')
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
lanche1, lanche2, lanche3, lanche4 = lanche
print(f"Primeiro lanche: {lanche1}")
print(f"Segundo lanche: {lanche2}")
print(f"Terceiro lanche: {lanche3}")
print(f"Quartoro lanche: {lanche4}")

print(lanche)

print(type(lanche))
 


print(len(lanche))
print('---')


print(lanche[0:2])
print('---')

print(lanche[::-1])
print('---')



for lanches in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[lanches]}')
    
print('---')

carros = (
    "gol",
    "celta",
    "palio",
)

#for carro in carros:
#    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

tuplas_nomes = ('Maria','Paulo', 'Maria', 'João', 'Sérgio')
print(tuplas_nomes[2:])
print(tuplas_nomes[::-1])
print(len(tuplas_nomes))
print(tuplas_nomes.index('João'))

for nomes in tuplas_nomes:
    print(nomes)

print('--------------------LISTAS--------------------')

lista = ['Nome', 1, 'Oi', 646341, 'mundo']
print(lista)
#del lista
#lista.clear()
#print(lista)
lista.append('tequinha')
print(lista[2:6])

lista2 = ['maca', 'pera', 'uva', 'melancia', 'banana']
for indice, elementos in enumerate(lista2):
    print(f'{indice} = {elementos}')
    
lista2.reverse()
print(lista2)

lista2.sort()
print(lista2)


lista3 = [2, 4, 8, 1]
print(min(lista3)) # Retorna o menor valor da lista
print(max(lista3)) # Retorna o maior valor da lista
