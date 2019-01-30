""" Hangman - The Internship 2019 """
import sys
import random
import keyboard

def random_word(category):
    """ 
        Random word from file of category that player choose.
        Use 'Random' for help to random word
    """
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
    """
        Calculate score from the answer for 100 score.
        solution: Number of the answer(count alphabet only) divided by 100
    """

    word_no_sign = 0

    for alpha in word:
        if alpha.isalpha():
            word_no_sign += 1

    cal = 100 / word_no_sign

    return cal

def display_on_screen(target, guessed_true, check):
    """ 
        generate display part before player guess by
        - if player can guess the correct character in last round : show that correct answer
        - but if player can't guess correct charecter : show the blank space('_') according to number of answer.
        The value 'check' - for check that player have complete the answer or not.
        - if True : player can guess the complete answer.
        - if False : player have not yet guess complete answer
    """
    for guess in target:
        if not guess.isalpha():
            print(guess, end="")
        elif guess in guessed_true or guess in guessed_true.swapcase():
            print(guess+" ", end="")
        else:
            print("_ ", end="")
            check = False
    return check

def check_answer(guessed_true, guessed_wrong, target, score, cal_sc):
    """ 
        First check : Player can input character only if player have wrong input, 
        tell them and give them a chance for input the new one
        Next, check the answer that True or False
        if True : increase score and show in next display part
        if False : store wrong answer
    """ 
    while True:
        res = input("\nYour answer >")
        print("\n", end="")
        if len(res) > 1:
            print("You can guess in character only! Try again")
        else:
            break

    if res in guessed_true or res in guessed_true.swapcase() :
            pass
    elif res in target or res in target.swapcase():
        target_for_cal = target.lower()
        res_for_cal = res
        if res in target.swapcase():
            res_for_cal = res.lower()
        score += cal_sc * (target_for_cal.count(res_for_cal))

        guessed_true += res
    else:
        if res in guessed_wrong:
            pass
        else: 
            guessed_wrong += res
    return guessed_true, guessed_wrong, score

def show_guess_wrong_case(num_of_guess, guessed_wrong):
    """
        display wrong case that player guess in last round
    """
    if(num_of_guess != 10 and len(guessed_wrong)!=0):
            print("wrong guessed: ", end="")
            for i in guessed_wrong:
                print(i, end=" ")
            print("\n", end="")

if __name__ == '__main__':
    category = {1:'BNK48', 2:'Twice', 3:'Animal'}

    print("---------------Hangman Game---------------")
    print("     Rules:\n\
        1. You can guess in character only.\n\
        2. You have chance to guess 10 times.\n\
        3. Total score : 100 points.\n\
    Type Number for select category that you want to guess!\n\
    \tChoose 1 - BNK48 \n\tChoose 2 - Twice \n\tChoose 3 - Animal")

    try: 
        selected = category[int(input("Select Category > "))]
    except ValueError:
        print("Incorrect Category. Please select it again")
        sys.exit()

    target, hint = random_word(selected)

    print("Hint: \""+hint+"\"")

    score = 0 
    num_of_guess = 10

    guessed_wrong = ""
    guessed_true = ""

    check = False

    cal_sc = calculate_score(target)

    while True:

        check = True

        check = display_on_screen(target, guessed_true, check)

        print("\nscore: %d \nremaining wrong guess %d" %(score, num_of_guess))

        show_guess_wrong_case(num_of_guess, guessed_wrong)

        if num_of_guess == 0 or check:
            if check:
                print("Congratuation! The answer is \"%s\"" %target)
            else:
                print("Game Over! Try it again!")
            break

        guessed_true, guessed_wrong, score = check_answer(guessed_true, guessed_wrong, target, score, cal_sc)

        num_of_guess -= 1
