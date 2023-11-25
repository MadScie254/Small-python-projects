import random
import nltk

# Download the words dataset from NLTK (you need to do this once)
nltk.download('words')
from nltk.corpus import words

def generate_words(random_letters):
    possible_words = []

    for word in words.words():
        if all(letter in random_letters for letter in word):
            possible_words.append(word)

    return possible_words

def main():
    # Get random letters from the user
    random_letters = input("Enter random letters: ").lower()

    # Generate and display words
    generated_words = generate_words(random_letters)
    
    if generated_words:
        print("Generated words:")
        for word in generated_words:
            print(word)
    else:
        print("No words found with the given letters.")

if __name__ == "__main__":
    main()
