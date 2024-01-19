import random

display_messages = [
  'Seja Feliz :)',
  'Fique tranquilo, tudo vai acabar bem!',
  'Olá Mundo! Estou aqui!'
]

while True:
  resposta = input('Deseja receber um conselho? S/N: ')
  if (resposta == 'S' or resposta == 's'):
    messagem = random.choice(display_messages)
    print(messagem)
    print()