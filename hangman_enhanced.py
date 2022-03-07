from ntpath import join
from operator import truediv
import random
import re

# Choose game difficulty: - DONE
# Easy - Duplicate letters are populated, duplicted guesses do not impact you.
# Hard - Duplicate letters are not-populated, duplicate letter guesses will count against you.
# Identify if you have already guessed a letter
# Handle uppercase letters
# Provide option to add a word (Masked) or pull the word from a list

## To display outputs not needed in the functioning of the program, but necessary to debug set the debugging value to True.
debugging = False

# This function is called to collect the input from the user. 
def getLetter():
    print("\n")
    msg = "Guess a letter: "
    char = input(msg)

    # .isalpha() check to make sure this is actually a character and not a number or symbol.
    if char.isalpha():
        return(char)
    else:
        print("You did not enter a letter, try again.")
        getLetter()

def Hard_hangman(word):
    wrong = 0
    stages = ["",
        "-------",
        "|  |  ",
        "|  O  ",
        "|  |  ",
        "| /|  ",
        "| /|\ ",
        "| /   ",
        "| / \ ",
        "|     "
        ]

    if debugging:
        f = 9
        print("\n"
        .join(stages[0:5]))
        print("\n"
        .join(stages[6:8]))


    rletters = list(word)
    board = ["__"] * len(word)
    win = False

    if debugging:
        print("################")
        print("##DEBUG OUTPUT##")
        print("----------------")
        print("The value of rletters is:", rletters)
        print("The value of board is:", board)
        print("The value of win is: ", win)
    
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        char = getLetter()

        if char in rletters:
            cind = rletters \
                .index(char)
            board[cind] = char
            rletters[cind] = '$'
            if debugging:
                print("The value of cind is:", cind)
                print("The value of char is:", char)
                print("The value of rletter is", rletters[cind])

        else:
            wrong += 1
        
        print((" ".join(board)))
        
        # e is incrimented to be one more than wrong so that we can join up to the number but 
        # not include the number when printing the stages.
        
        e = wrong + 1
        
        if debugging:
            print("The value of wrong is:", wrong)
            print("The value of e is:", e)

        if e < 5:
            print("\n"
                .join(stages[0:e]))
        elif e >= 5 and e < 8:
            print("\n"
                .join(stages[0:4]))
            print(stages[e - 1])
        elif e >= 8 and e < 10:
            print("\n"
                .join(stages[0:4]))
            print(stages[6])
            print(stages[e - 1])
        
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break 

    if debugging:
        print("About to move into loser code")

    if not win:
        print("\n"
            .join(stages[0:4]))
        print(stages[6])
        print(stages[8])

        print("You lose! It was {}."
            .format(word))

def easy_hangman(word):
    wrong = 0
    stages = ["",
        "-------",
        "|  |  ",
        "|  O  ",
        "|  |  ",
        "| /|  ",
        "| /|\ ",
        "| /   ",
        "| / \ ",
        "|     "
        ]

    if debugging:
        f = 9
        print("\n"
        .join(stages[0:5]))
        print("\n"
        .join(stages[6:8]))

    rletters = word
    board = ["__"] * len(word)
    win = False

    if debugging:
        print("################")
        print("##DEBUG OUTPUT##")
        print("----------------")
        print("The value of rletters is:", rletters)
        print("The value of board is:", board)
        print("The value of win is: ", win)
    
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        char = getLetter()

        if char in rletters:
            indices = [i.start() for i in re.finditer(char, rletters)]
        
            if debugging:
                print(indices)

            while indices:
                cind = indices.pop()
                board[cind] = char
        else:
            wrong += 1
        
        print((" ".join(board)))
        
        # e is incrimented to be one more than wrong so that we can join up to the number but 
        # not include the number when printing the stages.
        
        e = wrong + 1
        
        if debugging:
            print("The value of wrong is:", wrong)
            print("The value of e is:", e)

        if e < 5:
            print("\n"
                .join(stages[0:e]))
        elif e >= 5 and e < 8:
            print("\n"
                .join(stages[0:4]))
            print(stages[e - 1])
        elif e >= 8 and e < 10:
            print("\n"
                .join(stages[0:4]))
            print(stages[6])
            print(stages[e - 1])
        
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break 

    if debugging:
        print("About to move into loser code")

    if not win:
        print("\n"
            .join(stages[0:4]))
        print(stages[6])
        print(stages[8])

        print("You lose! It was {}."
            .format(word))

## the following lines open the words.txt file, the words are read into the word_list and seperated by commas.
words_file = open("words.txt", "r")
content = words_file.read()
word_list = content.split(",")
words_file.close()


if debugging:
    print(word_list)
    print(len(word_list))

"""
Randomint holds the integer that will be used to select the word from the word_list. The random intenger is 
generated by calling the random.randint python function. We pass the variables 0 and the length of the 
word_list to it to create teh range from which the random.randit will chose.
"""

randomint = random.randint(0,len(word_list))




# randomint is used to choose the word from a word list. 
# word_list is a list containing all the words that can be randomly used in this game. 

game = input("\n\nYou are about to play the game Hangman. There are two game options. Hard and Easy. To play Hard enter H otherwise press enter for easy.\n >>>> ")

if game == "H":
    Hard_hangman(word_list[randomint])
else:
    easy_hangman(word_list[randomint])