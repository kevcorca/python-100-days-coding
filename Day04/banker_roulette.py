import random
# list of friends
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

number_of_friends = (len(friends) - 1)

who_pays = random.randint(0, number_of_friends)

print(f"{friends[who_pays]} must pay for everyone else dinner's bill!")