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

game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?"))
prog_choice = game.index(random.choice(game))
# print(user_choice)
# print(prog_choice)

if user_choice == prog_choice:
    print("User choice")
    print(game[user_choice])
    print("Computer choice")
    print(game[prog_choice])
    print("It's a draw ...")
elif user_choice != prog_choice:
    if (user_choice == 0) and (prog_choice == 1):
        print("User choice")
        print(game[user_choice])
        print("Computer choice")
        print(game[prog_choice])
        print("Computer wins ...")
    elif (user_choice == 0) and (prog_choice == 2):
        print("User choice")
        print(game[user_choice])
        print("Computer choice")
        print(game[prog_choice])
        print("User wins ...")
    elif (user_choice == 1) and (prog_choice == 0):
        print("User choice")
        print(game[user_choice])
        print("Computer choice")
        print(game[prog_choice])
        print("User wins ...")
    elif (user_choice == 1) and (prog_choice == 2):
        print("User choice")
        print(game[user_choice])
        print("Computer choice")
        print(game[prog_choice])
        print("Computer wins ...")
    elif (user_choice == 2) and (prog_choice == 0):
        print("User choice")
        print(game[user_choice])
        print("Computer choice")
        print(game[prog_choice])
        print("Computer wins ...")
    elif (user_choice == 2) and (prog_choice == 1):
        print("User choice")
        print(game[user_choice])
        print("Computer choice")
        print(game[prog_choice])
        print("User wins ...")