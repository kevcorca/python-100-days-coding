import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("YOU WIN!")
