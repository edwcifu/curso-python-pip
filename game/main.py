import random


def choose_option():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera: ')
  if not user_option in options:
    print('Escoja una opcion valida')
    return None, None
  user_option = user_option.lower()
  computer_option = random.choice(options)
  return user_option, computer_option



def rules_game(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
    print(f'Resultado: User: {user_wins} - Computer: {computer_wins}')
  elif (user_option == 'piedra' and computer_option == 'tijera') or (
    user_option == 'papel' and computer_option == 'piedra') or (user_option == 'tijera' and computer_option == 'papel'):
    print(f'Computer dijo: {computer_option}')
    print('user gano!')
    user_wins += 1
    print(f'Resultado: User: {user_wins} - Computer: {computer_wins}')
  else:
    print(f'Computer dijo: {computer_option}')
    print('Computer ganó')
    computer_wins += 1
    print(f'Resultado: User: {user_wins} - Computer: {computer_wins}')
  return user_wins, computer_wins
def run_game():
  round = 1
  computer_wins = 0
  user_wins = 0
  
  while user_wins < 2 and computer_wins < 2:
  
    print('*' * 10)
    print('Round', round)
    print('*' * 10)
  
    user_option, computer_option = choose_option()
    if user_option is None and computer_option is None:
      continue
    user_wins, computer_wins = rules_game(user_option, computer_option, user_wins, computer_wins)

    round += 1

run_game()