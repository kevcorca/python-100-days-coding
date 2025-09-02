print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What's your age?"))
    if age < 12:
        bill = 5
        print("Children tickets are 5$")
    elif age < 18:
        bill = 7
        print("Adolescent tickets are 7$")
    else:
        bill = 12
        print("Adult tickets are 12$")

    want_photo = input("Want a photo to be taken? Type 'y' for yes or 'no' for no")
    if want_photo == "y":
        bill += 3

    print(f"Your total due ${bill}")
else:
    print("Sorry, you need to be taller to ride the rollercoaster...")