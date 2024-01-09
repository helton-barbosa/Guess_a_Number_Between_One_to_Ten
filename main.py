import random

sorteio = random.randint(1, 10)
tentativas = 3
chute = 0

while chute != sorteio and tentativas > 0:
    print(f'Você tem {tentativas} tentativas [{sorteio}]')

    chute = int(input('Escolha um número entre [1] e [10]: '))
    tentativas -= 1

    if chute < sorteio:
        print(f'O número {chute} é menor...\n')
    elif chute > sorteio:
        print(f'O número {chute} é maior...\n')
    else:
        print('Você acertou!\n')
        tentativas = 0
