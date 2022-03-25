#The HANGMAN Game
#EDUCATION → word that the computer has thought of
#U, I, N → list of characters that the user has successfully guessed
#_ _ U _ _ _ I _ N → display visible to the user
def display (comp, guessed):
    displayString = ""
    for c in comp:
        if c in guessed:
            displayString = displayString + c + " "
        else:
            displayString = displayString + "_ "
    print (displayString)

#display ("EDUCATION", ["U", "I", "N"])
import random

dictionary = ["TRAMPOLINE", "AFTERSHOCK", "BINOCULARS", "FLAMINGOES", "BANKRUPTCY", "LUMBERJACK", "REPUBLICAN", "FARSIGHTED", "MOTHERLAND", "BLACKSMITH"]
compGuess = random.choice (dictionary)
#List of all distinct characters guessed correctly by the user
guessedList = []
#List of all distinct characters unguessed by the user
unguessedList = []

for c in compGuess:
    if c not in unguessedList:
        unguessedList.append (c)

tries = 7


while tries >= 1:
    userGuess = input ("Enter your guess (" + str(tries) + " tries left): ")
    if userGuess in unguessedList:
        print ("Congrats! The letter exists in my word.")
        guessedList.append (userGuess)
        unguessedList.remove (userGuess)
        display (compGuess, guessedList)
        print ("\n")
        if len (unguessedList) == 0:
            print ("Congrats! You win!")
            break
    else:
        print ("Alas! Your guess doesn't exist inn my word.")
        tries = tries - 1
        display (compGuess, guessedList)
        print ("\n")

if len (unguessedList) != 0:
    print ("You lose this round as you exhausted all of your tries.")
    print ("The word I had in mind was " + compGuess + ".")
