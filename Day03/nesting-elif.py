print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What's your age?"))
    if age <= 12:
        print("You need to pay $5")
    elif age <= 18:
        print("You need to pay $7")
    elif age <= 22:
        print("You need to pay $10")
    elif age >= 60:
        print("You need to pay $7")
    else:
        print("You need to pay $12")

else:
    print("Sorry, you need to be taller to ride the rollercoaster...")