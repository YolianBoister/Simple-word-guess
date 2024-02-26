word = "fazbear"
first_letter = word[0]
last_letter = word[-1]
guess_count = 0

print("Welcome to the guessing game!")

def user_guess(guess_count):
    remaining_guesses = 5 - guess_count
    print("You have " + str(remaining_guesses) + " guesses remaining")
    current_guess = input("Next guess")
    if current_guess == word:
        print("You guessed the word!")
    else:
        print("Incorrect answer")
        guess_count = guess_count + 1
        if guess_count == 1:
            print("First letter is: ", str(first_letter))
            user_guess(guess_count)
        elif guess_count == 3:
            print("Last letter is: ", str(last_letter))
            user_guess(guess_count)
        elif guess_count == 5:
            print("You have run out of guesses")
            print("Gameover")
        else:
            user_guess(guess_count)
                
    
user_guess(guess_count)
