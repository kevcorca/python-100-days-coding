def life_in_weeks(age):
    # print(f"Your actual age is: {age}")
    ninety = 90 * 52
    age = age * 52
    age = ninety - age
    print(f"You have {age} weeks left.")

age = 0
# age = int(input("How many years do you have?"))
life_in_weeks(age)