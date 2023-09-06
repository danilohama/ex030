"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR"""
num = int(input('Me diga um numero qualquer: '))
resultado = num % 2
# print('O resultado foi {}'.format(resultado))
if resultado == 0:
    print('O número {} é \033[0:31mPAR'.format(num))
else:
    print('O número {} é \033[0:31mIMPAR'.format(num))
