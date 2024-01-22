from messages import display_messages
import random

print('Starting project again')

while True:
  resposta = input('Deseja receber um conselho? S/N: ')
  if (resposta == 'S' or resposta == 's'):
    messagem = random.choice(display_messages)
    print(messagem)
    print()