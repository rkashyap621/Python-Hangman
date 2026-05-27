import random
from Hangman_Word_Repo import word_list
from Hangman_ASCII_Arts import logo, stages

print(logo)

max_guess = 6
current_guess = max_guess
correct_guesses = []
all_guesses = []
game_over = False

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

display = list(placeholder)

while current_guess > 0 and not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in all_guesses:
        print("You already guessed the letter", guess + "! " + "Guess a different letter!")
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = chosen_word[i]
        display_str = "".join(display)

        if guess not in chosen_word:
            all_guesses.append(guess)
        else:
            correct_guesses.append(guess)
            all_guesses.append(guess)
            print("Great! Your guess,", guess, "is in the word! No lives were Lost!")

        if guess not in correct_guesses and all_guesses:
            current_guess -= 1
            print("Oh! No. Your guess,", guess, "is not in the word! You lost a life!")

    if "_" not in display:
        print(display_str)
        print("\n***********************YOU WIN!****************************************************************")
        print("The word was indeed " + "\"" + chosen_word + "!" + "\"")
        game_over = True
    else:
        print(display_str)
        print(
            f"\n*************************{current_guess}/{max_guess} LIVES LEFT********************************************************")
        print(stages[current_guess])

if not game_over:
    print(display_str)
    print("\n***********************GAME OVER! YOU LOSE!****************************************************")
    print("Alas! The word was " + "\"" + chosen_word + "!" + "\"")
