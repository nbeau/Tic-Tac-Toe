from turtle import *
import time
import random
import os

def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def drawBoard():
    lt(90)
    up()
    goto(-150, 50)
    down()
    goto(150, 50)
    up()
    goto(-150, -50)
    down()
    goto(150, -50)
    up()
    goto(-50, 150)
    down()
    goto(-50, -150)
    up()
    goto(50, 150)
    down()
    goto(50, -150)
    up()
    goto(0, 0)
    time.sleep(1)

def drawX():
    lt(40)
    fd(50)
    down()
    back(100)
    fd(50)
    rt(80)
    fd(50)
    back(100)
    fd(50)
    lt(40)
    up()

def drawX2(position):
    if position == 1:
        goto(-100, 100)
        drawX()
        goto(0, 0)
    elif position == 2:
        goto(0, 100)
        drawX()
        goto(0, 0)
    elif position == 3:
        goto(100, 100)
        drawX()
        goto(0, 0)
    elif position == 4:
        goto(-100, 0)
        drawX()
        goto(0, 0)
    elif position == 5:
        drawX()
    elif position == 6:
        goto(100, 0)
        drawX()
        goto(0, 0)
    elif position == 7:
        goto(-100, -100)
        drawX()
        goto(0, 0)
    elif position == 8:
        goto(0, -100)
        drawX()
        goto(0, 0)
    elif position == 9:
        goto(100, -100)
        drawX()
        goto(0, 0)

def drawO():
    fd(40)
    rt(90)
    down()
    fd(15)
    rt(45)
    fd(30)
    rt(45)
    fd(40)
    rt(45)
    fd(30)
    rt(45)
    fd(30)
    rt(45)
    fd(30)
    rt(45)
    fd(40)
    rt(45)
    fd(30)
    rt(45)
    fd(15)
    up()
    rt(90)
    fd(40)
    rt(180)

def drawO2(position):
    if position == 1:
        goto(-100, 100)
        drawO()
        goto(0, 0)
    elif position == 2:
        goto(0, 100)
        drawO()
        goto(0, 0)
    elif position == 3:
        goto(100, 100)
        drawO()
        goto(0, 0)
    elif position == 4:
        goto(-100, 0)
        drawO()
        goto(0, 0)
    elif position == 5:
        drawO()
    elif position == 6:
        goto(100, 0)
        drawO()
        goto(0, 0)
    elif position == 7:
        goto(-100, -100)
        drawO()
        goto(0, 0)
    elif position == 8:
        goto(0, -100)
        drawO()
        goto(0, 0)
    elif position == 9:
        goto(100, -100)
        drawO()
        goto(0, 0)

def checkWinX():
    if game[0] == "X" and game[1] == "X" and game[2] == "X":
        up()
        goto(-150, 100)
        down()
        goto(150, 100)
        up()
        goto(0, 0)
        down()
    elif game[3] == "X" and game[4] == "X" and game[5] == "X":
        up()
        goto(-150, 0)
        down()
        goto(150, 0)
        up()
        goto(0, 0)
        down()
    elif game[6] == "X" and game[7] == "X" and game[8] == "X":
        up()
        goto(-150, -100)
        down()
        goto(150, -100)
        up()
        rt(180)
        goto(0, 0)
        down()
    elif game[0] == "X" and game[3] == "X" and game[6] == "X":
        up()
        goto(-100, 150)
        down()
        goto(-100, -150)
        up()
        goto(0, 0)
        down()
    elif game[1] == "X" and game[4] == "X" and game[7] == "X":
        up()
        goto(0, 150)
        down()
        goto(0, -150)
        up()
        goto(0, 0)
        down()
    elif game[2] == "X" and game[5] == "X" and game[8] == "X":
        up()
        goto(100, 150)
        down()
        goto(100, -150)
        up()
        goto(0, 0)
        down()
    elif game[0] == "X" and game[4] == "X" and game[8] == "X":
        up()
        goto(-150, 150)
        down()
        goto(150, -150)
        up()
        goto(0, 0)
        down()
    elif game[2] == "X" and game[4] == "X" and game[6] == "X":
        up()
        goto(150, 150)
        down()
        goto(-150, -150)
        up()
        goto(0, 0)
        down()
    else: return False

def checkWinO():
    if game[0] == "O" and game[1] == "O" and game[2] == "O":
        up()
        goto(-150, 100)
        down()
        goto(150, 100)
        up()
        goto(0, 0)
        down()
    elif game[3] == "O" and game[4] == "O" and game[5] == "O":
        up()
        goto(-150, 0)
        down()
        goto(150, 0)
        up()
        goto(0, 0)
        down()
    elif game[6] == "O" and game[7] == "O" and game[8] == "O":
        up()
        goto(-150, -100)
        down()
        goto(150, -100)
        up()
        rt(180)
        goto(0, 0)
        down()
    elif game[0] == "O" and game[3] == "O" and game[6] == "O":
        up()
        goto(-100, 150)
        down()
        goto(-100, -150)
        up()
        goto(0, 0)
        down()
    elif game[1] == "O" and game[4] == "O" and game[7] == "O":
        up()
        goto(0, 150)
        down()
        goto(0, -150)
        up()
        goto(0, 0)
        down()
    elif game[2] == "O" and game[5] == "O" and game[8] == "O":
        up()
        goto(100, 150)
        down()
        goto(100, -150)
        up()
        goto(0, 0)
        down()
    elif game[0] == "O" and game[4] == "O" and game[8] == "O":
        up()
        goto(-150, 150)
        down()
        goto(150, -150)
        up()
        goto(0, 0)
        down()
    elif game[2] == "O" and game[4] == "O" and game[6] == "O":
        up()
        goto(150, 150)
        down()
        goto(-150, -150)
        up()
        goto(0, 0)
        down()
    else: return False  

def play():
    if game[0:3] == [0, "O", "O"]: return 1
    elif game[0:3] == ["O", 0, "O"]: return 2
    elif game[0:3] == ["O", "O", 0]: return 3
    elif game[3:6] == [0, "O", "O"]: return 4
    elif game[3:6] == ["O", 0, "O"]: return 5
    elif game[3:6] == ["O", "O", 0]: return 6
    elif game[6:9] == [0, "O", "O"]: return 7
    elif game[6:9] == ["O", 0, "O"]: return 8
    elif game[6:9] == ["O", "O", 0]: return 9
    
    elif game[0] == 0 and game[3] == "O" and game[6] == "O": return 1
    elif game[0] == "O" and game[3] == 0 and game[6] == "O": return 4
    elif game[0] == "O" and game[3] == "O" and game[6] == 0: return 7
    elif game[1] == 0 and game[4] == "O" and game[7] == "O": return 2
    elif game[1] == "O" and game[4] == 0 and game[7] == "O": return 5
    elif game[1] == "O" and game[4] == "O" and game[7] == 0: return 8
    elif game[2] == 0 and game[5] == "O" and game[8] == "O": return 3
    elif game[2] == "O" and game[5] == 0 and game[8] == "O": return 6
    elif game[2] == "O" and game[5] == "O" and game[8] == 0: return 9

    elif game[0] == 0 and game[4] == "O" and game[8] == "O": return 1
    elif game[0] == "O" and game[4] == 0 and game[8] == "O": return 5
    elif game[0] == "O" and game[4] == "O" and game[8] == 0: return 9
    elif game[2] == 0 and game[4] == "O" and game[6] == "O": return 3
    elif game[2] == "O" and game[4] == 0 and game[6] == "O": return 5
    elif game[2] == "O" and game[4] == "O" and game[6] == 0: return 7

    elif game[0:3] == [0, "X", "X"]: return 1
    elif game[0:3] == ["X", 0, "X"]: return 2
    elif game[0:3] == ["X", "X", 0]: return 3
    elif game[3:6] == [0, "X", "X"]: return 4
    elif game[3:6] == ["X", 0, "X"]: return 5
    elif game[3:6] == ["X", "X", 0]: return 6
    elif game[6:9] == [0, "X", "X"]: return 7
    elif game[6:9] == ["X", 0, "X"]: return 8
    elif game[6:9] == ["X", "X", 0]: return 9
    
    elif game[0] == 0 and game[3] == "X" and game[6] == "X": return 1
    elif game[0] == "X" and game[3] == 0 and game[6] == "X": return 4
    elif game[0] == "X" and game[3] == "X" and game[6] == 0: return 7
    elif game[1] == 0 and game[4] == "X" and game[7] == "X": return 2
    elif game[1] == "X" and game[4] == 0 and game[7] == "X": return 5
    elif game[1] == "X" and game[4] == "X" and game[7] == 0: return 8
    elif game[2] == 0 and game[5] == "X" and game[8] == "X": return 3
    elif game[2] == "X" and game[5] == 0 and game[8] == "X": return 6
    elif game[2] == "X" and game[5] == "X" and game[8] == 0: return 9

    elif game[0] == 0 and game[4] == "X" and game[8] == "X": return 1
    elif game[0] == "X" and game[4] == 0 and game[8] == "X": return 5
    elif game[0] == "X" and game[4] == "X" and game[8] == 0: return 9
    elif game[2] == 0 and game[4] == "X" and game[6] == "X": return 3
    elif game[2] == "X" and game[4] == 0 and game[6] == "X": return 5
    elif game[2] == "X" and game[4] == "X" and game[6] == 0: return 7

    return 0

def easy():
    position = random.choice(grid)
    return position

def medium():
    move = play()
    if move > 0 and move < 10:
        return move
    else: 
        return random.choice(grid)

def hard():
    move = play()
    if move > 0 and move < 10:
        return move
    elif i == 0: return 1
    elif i == 1:
        if scenario == 1.1: return 5
        elif scenario == 1.2: return 5
        elif scenario == 2: return 9
        elif scenario == 3: return 5
        elif scenario == 4: return 3
        elif scenario == 5: return 9
    elif i == 2:
        if scenario == 1.1: return 4
        elif scenario == 1.2: return 2
        elif scenario == 2:
            if position == 3: return 7
            elif position == 7: return 3
        elif scenario == 3:
            if position == 6: return 3
            elif position == 8: return 7
        elif scenario == 4:
            return 7   

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#XXXXX  Game intro
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

clearConsole()

again = "yes"
while again == "yes":
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game = [0] * 9
    win = False
    speed(0)
    
    print("This game of tic tac toe will be between you and I")
    print("")
    time.sleep(1)

    difficulty = input("""pick a dificulty (a, b or c)

    a: easy
    b: medium
    c: hard

""").strip().lower()
    print("")
    time.sleep(1)

    while not (difficulty == "a" or difficulty == "b" or difficulty == "c"):
        difficulty = input("It literally couldn't be simpler. pick a, b or c: ").strip().lower()

    print("Here is where we will play")
    print("")
    drawBoard()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#XX Game begins
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    for i in range(0, 5):

        # Computer's turn
        if win == False:
            if difficulty == "a":
                position = easy()
                grid.remove(position)
            elif difficulty == "b":
                position = medium()
                grid.remove(position)
            elif difficulty == "c":
                position = hard()

            game[position - 1] = "O"

            drawO2(position)
            time.sleep(1)
            
            if checkWinO() != False:
                clearConsole()
                print("I WIN")
                print("")
                time.sleep(1)
                win = True

            if game.count(0) == 0:
                win = "Tie"

        # Player's turn
        valid = False
        while valid == False and win == False:
            clearConsole()

            position = print("""Pick a number between 1 and 9 to pick a spot

    1 2 3
    4 5 6
    7 8 9
""")

            position_is_digit = False
            try:
                position = int(input())
                position_is_digit = True
            except:
                print("You didn't even enter a number, you were supposed to write a number")
                time.sleep(2)
               
            
            if position_is_digit == True and 0 < position < 10:
                if game[position - 1] == "X":
                    print("You've already picked that spot")
                    time.sleep(2)
                elif game[position - 1] == "O":
                    print("Can't you tell I already took that spot?")
                    time.sleep(2)
                else:
                    game[position - 1] = "X"
                    grid.remove(position)
                    valid = True
            elif position_is_digit == True:
                print("Did you never learn to count? You have to enter a number between 1 and 9")
                time.sleep(2)

            if valid == True:
                if i == 0:
                    if position == 2: scenario = 1.1
                    elif position == 4: scenario = 1.2
                    elif position == 3 or position == 7: scenario = 2
                    elif position == 6 or position == 8: scenario = 3
                    elif position == 9: scenario = 4
                    elif position == 5: scenario = 5
                
                drawX2(position)
                time.sleep(1)

        if checkWinX() != False:
            clearConsole()
            print("You won the match, good game!")
            print("")
            time.sleep(1)
            if difficulty == "a":
                print("Now try to beat me on the medium difficulty")
            elif difficulty == "b":
                print("Now try to beat me on the hard difficulty")
            elif difficulty == "c":
                print("I dont know how you managed to beat me, please tell the person who wrote this code how you did it, he will fix me")
            win = True
            break
            
    if win == "Tie":
        clearConsole()
        print("There was no winner this game")
        print("")
        time.sleep(1)

    again = input("You wanna play again? (Answer with yes or no) ").strip().lower()
    while not (again ==  "yes" or again == "no"):
        again = input("Is this a joke to you?\nDo you want to play again\n(ANSWER WITH YES OR NO)\n").strip().lower()

    if again == "yes":
        print("")
        time.sleep(1)
        print("Ok, let me erase this board first")
        time.sleep(1)
        clear()
        rt(90)
    elif again == "no":
        print("")
        time.sleep(1)
        print("oh, okay   :( ")
        print("")
        time.sleep(2)
        print("goodbye, friend")