import random

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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
choice_CPU = random.randint(0,2)
images = [rock, paper, scissors]

if choice > 2 or choice < 0:
  print("You typed an invalid number, you lost!")
else:
  print(images[choice])

  print("Computer chose:")

  print(images[choice_CPU])

  if choice == 0 and choice_CPU == 1:
    print("You lost!")
  elif choice == 1 and choice_CPU == 2:
    print("You lost!")
  elif choice == 2 and choice_CPU == 0:
    print("You lost!")
  elif choice == 1 and choice_CPU == 0:
    print("You won!")
  elif choice == 2 and choice_CPU == 1:
    print("You won!")
  elif choice == 0 and choice_CPU == 2:
    print("You won!")
  else:
    print("Draw!")