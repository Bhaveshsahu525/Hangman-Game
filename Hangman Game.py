def hangman():
    words = ["dog", "frog", "hog", "slob", "bacon", "avacado"]
    word = random.choice(words)
    lives = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')


    while len(word)>0 and lives>0:
        main_word = ""

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_"

        if main_word == word:
            print(main_word)
            print("you won")
            break

        print("guess the words", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade+guess
        else:
            print("enter valid character")
            continue

        if guess not in word:
            lives = lives - 1
            print("Wrong guess. You have", lives, "lives left.")

        if lives == 0:
            print('You lose the word was:', word)


name = input("Enter your name -->")
print("Welcome", name)
print("-----------------")
print("Guess the word in less then 10 attempts")
hangman()