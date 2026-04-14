# Snake, Water and Gun Game  🐍
'''
1 for Snake
-1 for Water
0 for Gun
'''
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice:")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youstr]

# by now we have 2 numbers (varibales), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("Its a Draw!")
else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("Oh!, Your Lose!")

    elif(computer == 1 and you == -1):
        print("Oh!, You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("Oh!, You Lose!")

    '''The below logic is written on the basis of the value of computer - you
    you can also do it like this'''

    '''if((computer - you) == -1 or (computer - you) == 2):
       print("Oh!, You Lose!")
    else:
        print("You Win!") '''