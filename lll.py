"""
Develop a simple game that teaches kindergarteners 
how to add single-digit numbers
Your function game() 
will take an integer n as input
Ask n single-digit addition questions
Numbers to be added should be chosen randomly from the range [0, 9]
The user will enter the answer when prompted
Print ‘Correct’ and ‘Incorrect’ by checking the answer

"""

# Sagar Chhadia (checked)

import random


def game(n):
    countCorrect = 0
    for i in range(n):

        firstNum = random.randint(0, 9)
        secondNum = random.randint(0, 9)

        print ('{} + {} = '.format(firstNum, secondNum))

        try:
            userInput = int(raw_input('Enter your ansewer: '))

            if (firstNum + secondNum) == userInput:
                print ('Correct!')
                countCorrect += 1
            else:
                print ('Incorrect!')
        except:
            print ('Enter your input in 0 to 9 format')
    print countCorrect


game(3)
