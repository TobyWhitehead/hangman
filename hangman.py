import sys
import hangman_images
import enchant


def main():
    print("\n" * 10)
    word_in = input("Enter a word for your opponent to guess: ").lower()
    if word_in == "exit_program":
        sys.exit(0)
    else:
        pass
    print("\n" * 50)
    letters = list(word_in)
    if word_in.isalpha() is False:
        print("\ninvalid character used")
        del word_in
        main()
    elif len(word_in) <= 2:
        print("\nplease enter a longer word")
        del word_in
        main()
    elif enchant.Dict("en_GB").check(word_in) is False:
        print("\nword not found in dictionary")
        print("\nsuggestions: {}".format(enchant.Dict("en_GB").suggest(word_in)))
        del word_in
        main()
    else:
        underscores = []
        incorrect_guesses = []
        correct_guesses = []
        out_of_guesses = False
        while len(underscores) < len(letters):
            underscores.append("_")
        current_underscores = " ".join(underscores)
        current_answer = "".join(underscores)
        print(current_underscores)
        while current_answer != word_in and out_of_guesses is False:
            guess = input("Guess a letter: ")
            print("\n" * 50)
            if guess == "exit_program":  # debug purposes
                sys.exit(0)
            elif len(guess) != 1:
                print("\ninvalid guess")
                if len(incorrect_guesses) == 0:
                    pass
                else:
                    hangman_images.image(len(incorrect_guesses))
                    print("\nincorrect guesses: {}"
                          .format(" ".join(incorrect_guesses)))
                print("\n" + current_underscores)
            elif correct_guesses.count(guess) == 1 or \
                    incorrect_guesses.count(guess) == 1:
                print("\nyou have already guessed this")
                hangman_images.image(len(incorrect_guesses))
                print("\n" + current_underscores)
                print("\nincorrect guesses: {}"
                      .format(" ".join(incorrect_guesses)))
            else:
                correct_letter = False
                for i in range(len(letters)):
                    if letters[i] == guess:
                        underscores[i] = letters[i]
                        if correct_guesses.count(guess) < 1:
                            correct_guesses.append(guess)
#                            print("correct guess detected: {}"
#                                  .format(correct_guesses))
#                            print("count: {}"
#                                  .format(correct_guesses.count(guess)))
                            correct_letter = True
                        else:
                            pass
                    else:
                        pass
                if correct_letter is False:
                    incorrect_guesses.append(guess)
#                    print("incorrect guess detected: {}"
#                          .format(incorrect_guesses))
#                    print("count: {}"
#                          .format(incorrect_guesses.count(guess)))
                else:
                    pass
                current_underscores = " ".join(underscores)
                current_answer = "".join(underscores)
                if len(incorrect_guesses) == 0:
                    pass
                else:
                    hangman_images.image(len(incorrect_guesses))
                    print("\nincorrect guesses: {}"
                          .format(" ".join(incorrect_guesses)))
                print("\n" + current_underscores)
                if len(incorrect_guesses) == 10:
                    out_of_guesses = True
        if out_of_guesses is True:
            print("\nOut of guesses. The word was {}".format(word_in))
        else:
            print("\nThe word was {}".format(word_in))
        del word_in
        play_again = input("Play Again? (y/n): ")
        if play_again == "y":
            main()
        elif play_again == "n":
            print("\nEnding Program")
        else:
            print("\nYou're not good at following instructions, "
                  "ending the program anyway")


main()
