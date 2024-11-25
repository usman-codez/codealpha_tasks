import random

with open('word.txt','r') as words:
    w = words.readline()

word1 = w.split(',')
word = random.choice(word1)
word = word.upper()
choices = 6

g_word = '-'*len(word)

while choices!=0:
    print(g_word)
    letter = input('Guess letter for word: ').upper()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                g_word = g_word[:i]+letter+g_word[i+1:]

        if g_word == word:
            print('Congratulations! You guessed the word')
            break

    else:
        choices -= 1
        print('The letter is not in the word')
        print('Choices left:', choices)


else:
    print('You lose!')
    print('The right word was', word)


