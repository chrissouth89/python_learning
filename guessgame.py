secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess.capitalize() != secret_word.capitalize() and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Take a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You guessed it!")
