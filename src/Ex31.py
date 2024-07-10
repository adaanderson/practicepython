print("Welcome to Hangman:\n_ _ _ _ _ _ _ _ _\n")
guesses = set()
word = "EVAPORATE"
word_set = set(word)

while word_set.intersection(guesses) != word_set:
    user = input("Guess your letter: ")
    guesses.add(user)
    mistakes = guesses.difference(word_set)
    print()
    for letter in word:
        if letter in guesses:
            print(letter, end = ' ')
        else:
            print("_", end=' ')
    str_mistakes = ', '.join(mistakes)
    print("\nMistakes: " + str_mistakes)
    print()         
    if word_set.intersection(guesses) == word_set:
        print("You win.")