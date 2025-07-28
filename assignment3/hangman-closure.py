def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)
        
        # Create display word with underscores for unguessed letters
        display_word = "".join(
            char if char in guesses else "_" 
            for char in secret_word
        )
        
        print(f"Current word: {display_word}")
        return all(char in guesses for char in secret_word)
    
    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter secret word: ").lower()
    game = make_hangman(secret)
    
    while True:
        guess = input("Guess a letter: ").lower()
        if game(guess):
            print("Congratulations! You guessed the word!")
            break