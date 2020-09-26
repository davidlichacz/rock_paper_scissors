import random

random.seed()

choices = {'rock': {'win': 'scissors', 'lose': 'paper'}, 'paper': {'win': 'rock', 'lose': 'scissors'},
           'scissors': {'win': 'paper', 'lose': 'rock'}}

player_name = input('Enter your name: ')
print('Hello,', player_name)
options = input('').split(',')
if options == [''] or options == ['rock', 'paper', 'scissors']:
    options = ['rock', 'scissors', 'paper']
print("Okay, let's start")

with open('rating.txt', 'r') as ratings:
    current_score = 0
    for line in ratings.readlines():
        rating = line.split()
        if rating[0] == player_name:
            current_score = int(rating[1])
            break

while True:
    player_choice = input('Enter your choice: ')

    if player_choice == '!exit':
        print('Bye!')
        break
    elif player_choice == '!rating':
        print('Your rating:', current_score)
        continue
    elif player_choice not in options:
        print('Invalid input')
        continue
    else:
        idx = options.index(player_choice)
        new = options[idx + 1:] + options[:idx]
        midpoint = int(len(new) / 2)
        win = new[:midpoint]
        lose = new[midpoint:]

    computer_choice = random.choice(options)

    if computer_choice in win:
        print(f'Well done. The computer chose {computer_choice} and failed')
        current_score += 100
    elif computer_choice in lose:
        print(f'Sorry, but the computer chose {computer_choice}')
    elif computer_choice == player_choice:
        print(f'There is a draw {computer_choice}')
        current_score += 50