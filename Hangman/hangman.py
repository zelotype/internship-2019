"""Hangman - The Internship 2019"""

import random

def main():
    """Main process"""
    category = {'1':'BNK48', '2':'Twice', '3':'Animal'}

    print("Select Category: \nBNK48 \nTwice \nAnimal \n ")

    selected = category[input("> ")]

    target, hint = random_word(selected)

    print("\nHint: \""+hint+"\"")

    score = 0
    g_num = 10

    guessed_wrong = ""
    guessed_true = ""

    check = False

    cal_sc = calculate_score(target)

    while True:

        check = True

        for guess in target:
            if not guess.isalpha():
                print(guess, end="")
            elif guess in guessed_true or guess in guessed_true.swapcase():
                print(guess+" ", end="")
            else:
                print("_ ", end="")
                check = False

        print("   score %d, remaining wrong guess %d" %(score, g_num), end="")

        if(g_num != 10 and len(guessed_wrong)!=0):
            print(", wrong guessed: ", end="")
            for i in guessed_wrong:
                print(i, end=" ")

        if g_num == 0 or check:
            break
        
        ans = input("\n>")

        g_num -= 1

        if ans in guessed_true or ans in guessed_true.swapcase() :
            pass
        elif ans in target or ans in target.swapcase():

            ans_for_cal = ans

            if ans in target.swapcase():
                ans_for_cal = ans.swapcase()
            score += cal_sc * (target.count(ans_for_cal))

            guessed_true += ans
        else:
            guessed_wrong += ans

        print(len(guessed_wrong))


def random_word(category):
    """Random word from category that player choose"""
    filename = category + ".txt"
    file = open(filename, "r")

    words = list()
    hint = list()

    for aline in file:
        word = aline.split(',')
        words.append(word[0])
        hint.append(word[1].strip())

    num = random.randint(0, 4)

    target = [words[num], hint[num]]

    file.close()

    return target

def calculate_score(word):
    """calculate score for guess word"""

    word_no_sign = 0

    for alpha in word:
        if alpha.isalpha():
            word_no_sign += 1

    cal = 100 / word_no_sign

    return cal

main()
    

