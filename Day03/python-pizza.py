print("Welcome to Python Pizza Deliveries!")
bill = 0
order = True
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
# else:
#     order = False

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
# else:
    # order = False
# if order:
#     print(f"Your due bill is ${bill}")
# else:
#     print("Sorry! You have chosen an invalid option through your order!")