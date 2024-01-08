import random

sorteio = random.randint(1, 10)

chute = 0

while chute != sorteio:
    chute = int(input('Escolha um número entre [1] e [10]: '))
    if chute < sorteio:
        print(f'O número {chute} é menor...')
    elif chute > sorteio:
        print(f'O número {chute} é maior...')
    else:
        print('Você acertou!')
