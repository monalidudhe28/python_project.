import random

words = ["python", "java", "keyboard", "monitor", "programming", "developer"]

word = random.choice(words)
jumbled = ''.join(random.sample(word, len(word)))

print("Unscramble the word:", jumbled)

guess = input("Your guess: ")

if guess.lower() == word:
    print("Correct!")
else:
    print("Wrong! The correct word is:", word)