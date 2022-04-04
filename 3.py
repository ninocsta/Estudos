'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
from time import sleep
print('~~' * 10)
count = 0
while True:
    while True:
        p = str(input('Par ou impar? [P/I] '))
        c = randint(1, 2)
        if p in 'Pp':
            print('Jogador: PAR!')
            print('Computador: IMPAR!')
            n = int(input('Digite um número: '))
            print('1')
            sleep(1)
            print('2')
            sleep(1)
            print('3')
            sleep(1)
            print('JÁ')
            print(f'Jogador: {n}')
            print(f'Computador: {c}')
            if (n + c) % 2 == 0:
                print(f'Boa, ganhou! {n + c} é par.')
                count += 1
            else:
                print(f'Poxa, não foi dessa vez. {n + c} é impar.')
                break
        elif p in 'Ii':
            print('Jogador: IMPAR!')
            print('Computador: PAR!')
            n = int(input('Digite um número: '))
            print('1')
            sleep(1)
            print('2')
            sleep(1)
            print('3')
            sleep(1)
            print('JÁ')
            print(f'Jogador: {n}')
            print(f'Computador: {c}')
            if (n + c) % 2 != 0:
                print(f'Boa, ganhou! {n + c} é ímpar.')
                count += 1
            else:
                print(f'Poxa, não foi dessa vez. {n + c} é par.')
                break
    print(f'Você conseguiu {count} vitórias consecutivas.')


