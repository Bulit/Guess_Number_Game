import random

def guess_game():
    # pick random number between 1 & 100 (inclusive) and make it a string
    rn_number = str(random.randint(1, 100))

    chosen_num = input('OK, I already got number in my mind, so whats my number: ')
    # 10 tries
    guesses_left = 10

    while chosen_num != rn_number and guesses_left > 0:
        # if we are in loop a bad guess was made, and they have at least one guess left
        # so decrement and prompt again
        guesses_left -= 1
        print(f'Wrong number chose again, only {guesses_left} tries left')
        chosen_num = input('Whats my number: ')

    # Not in the loop, so they got it or they didn't
    # we want to report on their performance
    if chosen_num == rn_number:
        msg = f'Congratulation, {chosen_num} was my number!'
    else:
        msg = f'Sorry you lose :) I was thinking of {rn_number}'

    # prompt to play again
    play_again = input(f'{msg}\n Want to play again? Y/N\n')
    while play_again.lower() not in 'yn':
        print('I don\'t understand you!')
        play_again = input('Want to play AGAIN or NO? Chose Y or N only. Y/N\n')

    if play_again.lower() == 'y':
        guess_game()

    if play_again.lower() == 'n':
        print('OK, thank you for game and have a nice day')
        return

            
print('Hey do you wanna play a guess number game?\nI chose number between 1 - 100 and you try to quess it')
guess_game()

