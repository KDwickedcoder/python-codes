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

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]

user_choice = int(input("what do you want to chose 0 for rock, 1 for paper and 2 for scissors:\n"))

if (user_choice >= 3) or(user_choice<0):
  print("you entered an invalid number, you lose")
  
else:
  print("your choice is:\n")
  print(game_images[user_choice])

  print("\n")

  print("computer choice is:\n")
  computer_choice = random.randint(0,2)
  print(game_images[computer_choice])


if (user_choice == 0) and (computer_choice == 2):
  print("you win")
elif (user_choice == 2) and (computer_choice == 0):
  print("you lose")
elif (user_choice > computer_choice):
  print("you win")
elif (user_choice < computer_choice):
  print("you lose")
else:
  print("it is a draw")
  
  