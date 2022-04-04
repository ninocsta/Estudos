'''
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e
 qual foi a soma entre elas (desconsiderando o flag).

numerops inteiros
999 break
soma dos numeros
quantos numeros
'''
count = 0
print('^^' * 10)
print('Soma de números inteiros')
print('[999] para cancelar.')
print('^^' * 10)
soma = 0
while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'Foram somados {count} números')
print(f'A soma total dos números é {soma}.')
