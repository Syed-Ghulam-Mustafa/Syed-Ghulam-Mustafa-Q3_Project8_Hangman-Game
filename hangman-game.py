import random
words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'enum', 'collab', 'vscode', 'game']

word = random.choice(words)
guessed_letters = []
attempts = 8

print("Welcome to Hangman Game!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\n guess the letters:").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Write one alphabet only!")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter")
        continue
    guessed_letters.append(guess)
    
    if guess in word:
        print("You guessed it right!")
    else:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left")
        
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)
    
    if "_" not in displayed_word:
        print(f"Congratulations! the correct word is: {word}")
        break
else:
    print(f"Game over! The correct word is: {word}")