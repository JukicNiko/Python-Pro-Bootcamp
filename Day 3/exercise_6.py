print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

side = input("You are on the island, would you like to go to the left or right side of it? ")
l_side = side.lower()


if l_side == "right":
  print("You fell into a hole! Game over!")
elif l_side == "left":
  print("Great, you avoided the trap! You can head over to the next step.")
  decision = input("Next boat is coming in 13 hours, would you like to wait for it or swim accross? ")
  l_decision = decision.lower()
  if l_decision == "wait":
    print("That sea was full of sharks, you are lucky! You got onto a next step.")
    door = input("There are 3 doors, if you choose the correct one you will find a treasure! Which one do you want to open? Red, blue or yellow? ")
    l_door = door.lower()
    if l_door == "blue":
      print("Monster ate you! Game over!")
    elif l_door == "red":
      print("Monster ate you! Game over!")
    elif l_door == "yellow":
      print("Congratulations! You found the treasure!")
    else:
      print("Game over!")
  elif l_decision == "swim":
    print("Well, that is unfortunate. Sharks ate your body. Game over!")