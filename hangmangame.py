import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ['aardvark', 'bamboo', 'camel']
right_answer = random.choice(word_list)
print(right_answer)
word_length = len(right_answer)
placeholder = ''
lives = 6
game_over = False
correct_answer_list = []

for words in range(word_length):
    placeholder += '_'

print(placeholder)

while not game_over:
    print(f'You have {lives} left')
    guess = input('Guess a letter: ')

    display = ''

    for letters in right_answer:
        if letters == guess:

            if guess not in correct_answer_list:
                display += guess
                correct_answer_list.append(letters)
            else:
                print(f"You've already guessed this: {guess}")
        elif letters in correct_answer_list:
            display += letters
        else:
            display += '_'

    if '_' not in display:
        game_over = True
        print('You Win')
    elif guess not in right_answer:
        lives -= 1
        print(f"You guessed {guess}, that's not correct, you loose a life")
        print(stages[6 - lives])
        print(f'You have {lives} left')
        if lives == 0:
            game_over = True
            print('You lose')
    print(display)
