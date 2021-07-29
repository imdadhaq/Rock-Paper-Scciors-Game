
from random import randint



def game():
    # create a list of play options
    opt = ["Rock", "Paper", "scissors"]

    # assign a random play to the computer
    comp = opt[randint(0,2)]

    # set player to false
    palyer = False
    while palyer == False:
        palyer = input("Rock, Paper,Scissors")
        if palyer == comp :
            print("It's a tie")
        elif palyer == "Rock":
            if comp=="Paper":
                print("You lose",comp,"covers",palyer)
            else:
                print("You win",palyer,"smashes",comp)
        elif palyer=="Paper":
            if comp=="Scirssors":
                print("you lose",comp,"cuts",palyer)
            else:
                print("you win",palyer,"Covers",comp)
        elif palyer == "Scirssors":
            if comp=="Rock":
                print("You Lose",comp,"Breaks",palyer)
            else:
                print("You Win",palyer,"cut",comp)
        else:
            print("that's not avalid play please check your spelling")
        palyer=False
        comp=opt[randint(0,2)]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()


