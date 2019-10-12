#Van Nguyen
#4/20/2018
#guessing game with improvements
import random
def main():
    guesses = 0
    randNum = random.randint(1,20)

    while guesses < 6:
        myGuess = int(input("Please input a number between 1 and 20: "))

        if myGuess > 20 or myGuess < 1:
            print("Please enter a valid number between 1 and 20: ") #The improvement is that now the user cannot input an invalid guess.
        elif myGuess < randNum:
            print("Number is higher.")
            guesses += 1
        elif myGuess > randNum:
            print("Number is lower")
            guesses += 1
        else:
            guesses += 1
            break

    if myGuess == randNum:
        print("Perfect, you got it in %s guesses" % guesses)

    else:
        print("Try again!")


main()


