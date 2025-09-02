print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

question1 = input("You came across an intersection, you must choose: left or right?")
if question1 != "left":
    print("You fell into a hole! Game over...")
    exit()

question2 = input("You found a lake, you must choose: swim or wait")
if question2 != "wait":
    print("You got attacked by a trout! Game over...")
    exit()
    
question3 = input("You found a house with three unlocked doors, you must choose one: red, yellow or blue")
if question3 == "red":
    print("You got burned by fire! Game over...")
elif question3 == "blue":
    print("You got attacked by wild beasts! Game over...")
elif question3 == "yellow":
    print("You found the lost treasure! Congratulations you win!")
else:
    print("You got lost in the wonders of the mysterious house. Game over...")
# print("wololo")