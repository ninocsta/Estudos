'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
 um de cada vez,
 para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.
'''

n = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor ? '))
    if num < 0:
        break
    for n in range(1, 11):
        m = n * num
        print(f'{n} * {num} = {m}')
print('Encerrado!')
