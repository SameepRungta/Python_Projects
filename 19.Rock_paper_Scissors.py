import random

a = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:"))

b = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if a == 0:
    print(rock)
elif a == 1:
    print(paper)
elif a == 2:
    print(scissors)
else:
    print("Invalid Input")

if b == 0:
    print(rock)
elif b == 1:
    print(paper)
elif b == 2:
    print(scissors)
else:
    print("Invalid Input")

if a == b:
    print("It's a draw!")
elif (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
    print("You win!")
else:
    print("You lose!")
