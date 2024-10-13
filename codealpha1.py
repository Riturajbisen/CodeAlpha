import random

def select_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'openai', 'artificial', 'intelligence']
    return random.choice(words)

def display_word_state(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # limit of incorrect guesses
    
    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word_state(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            incorrect_guesses += 1
            guessed_letters.append(guess)
        
        if set(word) <= set(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

if _name_ == "_main_":
    hangman_game()