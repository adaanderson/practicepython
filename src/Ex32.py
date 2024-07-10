from random import sample

with open('sowpods.txt', 'r') as open_file:
    names = set()
       
    while True:
        line = open_file.readline()
        if not line:
            break
        x = line.replace('\n', '')
        names.add(x)
        
draft_word = sample(names,1)

guesses = set()
word = ''.join(draft_word)
word_set = set(word)
anim = []
anim.append("___\n" + "|  |\n" + "|   \n" + "|  \n" + "|   \n" + "|   \n")
anim.append("___\n" + "|  |\n" + "|  o \n" + "|  \n" + "|   \n" + "|   \n")
anim.append("___\n" + "|  |\n" + "|  o \n" + "|  | \n" + "|   \n" + "|   \n")
anim.append("___\n" + "|  |\n" + "|  o \n" + "| /| \n" + "|   \n" + "|   \n")
anim.append("___\n" + "|  |\n" + "|  o \n" + "| /|\\ \n" + "|   \n" + "|   \n")
anim.append("___\n" + "|  |\n" + "|  o \n" + "| /|\\ \n" + "| /  \n" + "|   \n")
anim.append("___\n" + "|  |\n" + "|  o \n" + "| /|\\ \n" + "| / \\ \n" + "|   \n")

print("\nWelcome to Hangman:\n" + len(word) * '_ ' + "\n\n" + anim[0] + "\n")

while word_set.intersection(guesses) != word_set:
    user_draft = input("Guess your letter: ")
    user = user_draft.upper()

    guesses.add(user)
    mistakes = guesses.difference(word_set)
    num_mistakes = len(mistakes)
    num_guesses = 6 - num_mistakes

    print()
    print(anim[num_mistakes])
    print("\nYou have " + str(num_guesses) + " guesses left.\n")

    for letter in word:
        if letter in guesses:
            print(letter, end = ' ')
        else:
            print("_", end=' ')

    str_mistakes = ', '.join(mistakes)
    print("\nMistakes: " + str_mistakes)
    print()         
    if word_set.intersection(guesses) == word_set:
        print("You win... (ノಠ益ಠ)ノ彡┻━━┻ ")
    if num_mistakes >= 6:
        print("You lose! The word is " + word + " 〵⎝` ‿ ´⎠ 〳")
        break