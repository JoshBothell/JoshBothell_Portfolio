#JoshBothell 11/18
#importing data.py and initializing variables.
import data
correct = False
guess_num = 0
#main loop and scoring system.
def main():
    score = 0
    print(data.main_menu)
    input("...")
    print("The scoring will be based upon how many attempts you take\nthe best possible score is 20")
    score = score + q1()
    score = score + p1()
    print("Your score is:",score,"remember, lower is better")
    score = score + q2()
    score = score + p2()
    print("Your score is:",score,"remember, lower is better")
    score = score + q3()
    score = score + p3()
    print("Your score is:",score,"remember, lower is better")
    score = score + q4()
    score = score + p4()
    print("Your score is:",score,"remember, lower is better")
    score = score + q5()
    score = score + p5()
    print("Your score is:",score,"remember, lower is better")
    score = score + q6()
    score = score + p6()
    print("Your score is:",score,"remember, lower is better")
    score = score + q7()
    score = score + p7()
    print("Your score is:",score,"remember, lower is better")
    score = score + q8()
    score = score + p8()
    print("Your score is:",score,"remember, lower is better")
    score = score + q9()
    score = score + p9()
    print("Your score is:",score,"remember, lower is better")
    score = score + q10()
    score = score + p10()
    print("Your FINAL score is:",score,"remember, lower is better")
#ALL THE FUNCTIONS FOR EACH QUESTION AND PUZZLE  
def q1():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        print("ENTER THE MATCHING WORD TO THE DEFINITION")
        guess = input(data.trivia_1)
        if guess.lower() == data.answer_1:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p1():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_1)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_1:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q2():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_2)
        if guess.lower() == data.answer_2:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p2():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_2)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_2:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q3():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_3)
        if guess.lower() == data.answer_3:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p3():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_3)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_3:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q4():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_4)
        if guess.lower() == data.answer_4:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p4():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_4)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_4:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q5():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_5)
        if guess.lower() == data.answer_5:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p5():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_5)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_5:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q6():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_6)
        if guess.lower() == data.answer_6:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p6():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_6)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_6:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q7():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_7)
        if guess.lower() == data.answer_7:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p7():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_7)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_7:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q8():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_8)
        if guess.lower() == data.answer_8:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p8():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_8)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_8:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q9():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_9)
        if guess.lower() == data.answer_9:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p9():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_9)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_9:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num
def q10():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_10)
        if guess.lower() == data.answer_10:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p10():
    guess_num = 0
    print(data.puzzle_pretty)
    while correct == False and guess_num < 10:
        print(data.enter_pos, data.answer_10)
        guess = input("")
        guess_num += 1
        word = ""
        pos = "0"
        for i in guess:
            if i == ",":
                x = int(pos)
                word = word + data.puzzle[x]
                pos = "0"
            else:
                pos = pos + i
        print(word)
        if word == data.answer_10:
            print(data.correct)
            return guess_num
        else:
            print(data.incorrect)
            continue
    print(data.fail)
    return guess_num


main()
input("press enter to exit")

