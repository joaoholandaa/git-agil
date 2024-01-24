from messages import display_messages
import random
import time

print('Iniciando o Projeto 3..2..1..')
time.sleep(3)

login_username = [
    'Maria',
    'Joao',
    'Pedro',
    'Lucas',
    'Marcos',
    'Paulo'
]

username = input('usuario para login: ')

while True:
    while(username not in login_username):
        print()
        print('Usario Invalido! Tente novamente!')
        username = input('usuario para login: ')

    resposta = input('Deseja receber um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        print()
        messagem = random.choice(display_messages)
        print(messagem)
        print()