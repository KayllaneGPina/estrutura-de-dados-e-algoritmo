import random 
import time

print(random.random())
print(random.randint(1, 6))

random.seed(8)
print(random.random())

random.seed(8)
numeros = random.getstate()
print(random.sample(range(10), k=3))

random.setstate(numeros)
print(random.sample(range(10), k=3))

print(random.getrandbits(8))


print(random.randrange(10, 100, 5))

print(random.randint(10, 350))

# lista_nome = ['Pedro', 'Maria', 'João', 'Marcos']
# print(random.choice(lista_nome))
lista_nomes=['Maria', 'João', 'Pedro', 'Cláudia']
print(random.choices(lista_nomes,weights=[2, 5, 1, 8], k=3))

lista_nomes2=['Maria', 'João', 'Pedro', 'Cláudia', 'Angélica', 'Tiago']
random.shuffle(lista_nomes2)
print(lista_nomes2)

pro_time = time.ctime()
print("Current processor time (in seconds):", pro_time) 