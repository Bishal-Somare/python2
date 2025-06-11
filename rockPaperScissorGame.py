#rock paper sissors
#rule = paper>rock rock>scissors scissor>paper
print("Rock paper sissors game")
print("Rule: paper>rock rock>scissors scissor>paper")

import random
computer=random.choice(["rock","paper","scissor"])

user = input("Enter your choice: ")
print(user)
print(computer)

if(user=='rock' and computer=='scissor') or (user=='paper' and computer =='rock') or (user=='scissor' and computer=='paper'):
    print("user has won")
elif user==computer:
    print("game has been drawn")
elif user not in ['rock','paper','scissor']:
    print("invalid word")
else:
    print("computer has won")