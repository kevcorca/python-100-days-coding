# import random
#
# num1 = 0
# guess = int(input("Please choose a number between 0 and 10"))
#
# if guess >= 0 and guess <= 10:
#     num1 = random.randint(0, 10)
#     if num1 == guess:
#         print("You have chosen the correct number")
#     else:
#         print(f"You have chosen the wrong number, the correct one was {num1}")
# else:
#     print("It was from 1 to 10...")

import random
# import my_module

# print(my_module.my_favorite_number)

# heads or tails
result = 0
user_selection = input("heads or tails")

if user_selection == "heads":
    user_selection = 0
elif user_selection == "tails":
    user_selection = 1
else:
    print("Didn't choose heads or tails...")

result = random.randint(0, 1)
print(result)
if result == "0":
    print("The result is heads")
    if user_selection == 0:
        print("You win!")
    else:
        print("You lose...")
else:
    print("The result is tails")
    if user_selection == 1:
        print("You win!")
    else:
        print("You lose...")