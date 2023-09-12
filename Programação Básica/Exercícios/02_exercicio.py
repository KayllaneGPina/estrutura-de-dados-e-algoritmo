'''
1. Leia a idade do usuário e classifique-o em:
- Criança – 0 a 12 anos
- Adolescente – 13 a 17 anos
- Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

2. Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
'''

# Exercício 1
usuario = int(input("Digite sua idade: "))

if usuario >= 0 and usuario <= 12:
    print("Criança")
elif usuario >= 13 and usuario <= 17:
    print("Adolescente")
elif usuario > 18:
    print("Adulto")
else:
    print("Idade inválida")
    
# Exercício 2
m1 = float(input('Digite sua nota: '))
m2 = float(input('Digite sua nota: '))
m3 = float(input('Digite sua nota: '))

media = (m1 + m2 + m3) / 3.0

if media >= 0.0 and media <= 4.0:
    print(f'Sua nota foi {media:.1f}. Reprovado!')
elif media >= 4.1 and media <= 6.0:
    print(f'Sua nota foi {media:.1f}. Pegou exame!')
    exame = float(input('Digite a nota do seu exame: '))
    if exame >= 6.0:
        print('Aprovado no exame!')
    else:
        print('Reprovado no exame!')
else:
    print(f'Sua nota foi {media:.1f}. Aprovado!')
    