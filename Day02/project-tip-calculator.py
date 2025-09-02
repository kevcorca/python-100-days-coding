print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = float(input("How many people to split the bill?\n"))

tip_perc = (tip * 0.01) + 1
tip_calc = round(((bill / people) * tip_perc), 2)

print(f"Each person should pay: {tip_calc}")