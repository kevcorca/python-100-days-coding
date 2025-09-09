# while loop
# used to execute a block of code repeatedly (while conditions are met)
count = 0

# while count isn't 5 do this:
while count < 5:
    print(f"current count is {count}")

    # a variable is needed to exit the loop and prevent an infinite
    count = count + 1

print("The loop has finished")

# while not is used when we need to reach an specific event or goal
# syntax -> while not condition > something: