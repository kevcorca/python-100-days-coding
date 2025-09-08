#define a function
def greet():
    print("Hello!")

# call a function
greet()

# parameters as input
def greet_name(name):
    print("Hello" + " " + name)

your_name = input("What's your name?")
greet_name(your_name)

# return statement
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)
