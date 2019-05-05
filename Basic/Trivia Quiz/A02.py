#
# Name: Yuta Kihara

# Description of program: we will create a simple question and answer game using
# if statements, Boolean expressions, Python I/O for interaction and looping control flow structures.

print('*************************************************')
print('Welcome to Japan Trivia Quiz.')
print('Win by answering all three questions correctly.')
print('*************************************************')
print()

continuing = True

while continuing:
    numOfWin = 0
    print('Q1. What is the name of the highest mountain in Japan ?\n',
          '1. FUJI\n',
          '2. FIJI\n',
          '3. HOJI\n',
          '4. MAJI')
    answer1 = input('Enter your answer (1,2,3, or 4): ')
    if answer1 == '1':
        print("You're correct!!\n")
        numOfWin = numOfWin + 1
    else:
        print('Incorrect, there are two more!!\n')

    print('Q2. What is the name of the currency in Japan ?\n',
          '1. BON\n',
          '2. REN\n',
          '3. YEN\n',
          '4. VEN')
    answer2 = input('Enter your answer (1,2,3, or 4): ')
    if answer2 == '3' and numOfWin == 1:
        print("You're correct again!!\n")
        numOfWin = numOfWin + 1
    elif answer2 == '3' and numOfWin == 0:
        print("Nice! You got it!!\n")
        numOfWin = numOfWin + 1
    else:
        print('Oh no... only one question left!!\n')

    print('Q3. What is the name of the capital in Japan ?\n',
          '1. KYOTO\n',
          '2. OSAKA\n',
          '3. TOKYO\n',
          '4. OKINAWA')
    answer3 = input('Enter your answer (1,2,3, or 4): ')
    if answer3 == '3' and numOfWin == 2:
        print("You're perfect!! Congrats!!")
        print("Thank you for playing. Goodbye")
        numOfWin = numOfWin + 1
        break
    elif answer3 == '3' and numOfWin == 1:
        print('Great!! Your score is 2 out of 3.\n')
        numOfWin = numOfWin + 1
    elif answer3 == '3' and numOfWin == 0:
        print('Finally, you got it!\n')
        numOfWin = numOfWin + 1
    elif answer3 != '3' and numOfWin == 2:
        print('Ohhhhhh no, almost you got a perfect score!!\n')
    elif answer3 != '3' and numOfWin == 1:
        print('Incorrect!! Your final score is 1\n')
    else:
        print('Terrible score, you are failed.\n')

    if numOfWin != 3:
        result = input('Do you want to try again? (y)es or (n)o? ')
        if result == 'y':
            continue
        else:
            print("Thank you for playing. Goodbye")
            break
