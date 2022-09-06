import functions as g
import sys

def main():
    try:
        username = input("What is your name? ").title()
        userscore = g.get_user_points(username)
        userscore = int(userscore)
        if userscore == -1:
            newuser = True
            userscore = 0
        else:
            newuser = False
        userchoice = 'y'
        while userchoice != 'n':
            session_score = g.generatequestion(username)
            userscore = userscore + int(session_score)
            g.update_user_points(newuser, username, userscore)
            try:
                userchoice = input ('\nWould you like to play again? Y/N ').lower()
            except:
                userchoice = input ('\nPlease use Y or N').lower()
    
    except:
        sys.exit('Unexpected error')


if __name__ == "__main__":
    main()
