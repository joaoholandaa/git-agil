import random
from .messages import display_messages

while True:
  resposta = input('Deseja receber um conselho? S/N: ')
  if (resposta == 'S' or resposta == 's'):
    messagem = random.choice(display_messages)
    print(messagem)
    print()