import random
import os
import time

def get_user_points(username):
    try:
        f = open("scores.txt", 'r')
        for line in f:
            user, userscore = line.split()
            user = user.rstrip(',')
            if user == username:
                return userscore   
        f.close()
        return '-1'
    except IOError:
        print ('File scores.txt not found, A new file will be Created.')
        f = open('scores.txt', 'w')
        f.close()
        return '-1'


def update_user_points(newuser, username, score):
    if newuser:
        f = open("scores.txt", 'a')
        f.write(username + ', ' + str(score) + '\n')
        f.close()
    else:
        f = open("scores.txt" , 'r')
        g = open("scores.tmp", 'w')
        for line in f:
            user, userscore = line.split(',')
            if user == username:
                g.write(user + ', ' + str(score))
            else:
                g.write(line)
        f.close()
        g.close()
        os.remove('scores.txt') 
        os.rename('scores.tmp', 'scores.txt') 
    

def generatequestion(username):
    operandlist = [0, 0]
    operatorlist = ['','']
    operatordict = {1: '+', 2: '-'}
    
    #generate random numbers
    for num in range(0,2):
        operandlist[num] = random.randint(1,9)

   
    #generate random operators
    for op in range(0,2):
        operator = operatordict[random.randint(1, 2)]
        operatorlist[op] = operator
    

    #generate the questions
    questionstring = str(operandlist[0])

    if operandlist[0] < operandlist[1]:
        operatorlist[0] = '+'

    questionstring = questionstring + str(operatorlist[num-1]) + str(operandlist[1])

    result = eval(questionstring)
    #remove ** from questionstring and replace with ^ for ease of reading
    questionstring = questionstring.replace('**', '^')

    print (f'\nLet\'s see how good your maths is {username}?\n')
    print (questionstring)
    useranswer = input("\nAnswer: ")

    while True:
        try:
            if useranswer.isdigit() or useranswer.startswith('-'):
                if int(useranswer) == int(result):
                    print ('Congratulations, you are correct')
                    return 1
                else:
                    print('\nSorry incorrect\n')
                    time.sleep(1)
                    print (f'Correct answer is {result}')
                    time.sleep(1.5)   
                    return 0
            else:
                print ('\nYou have not typed a numeber, try again\n')
                useranswer = input ('\nAnswer: ')
        except ValueError:
            print ('\nYou have not typed a numeber, try again\n')
            useranswer = input ('\nAnswer: ')

