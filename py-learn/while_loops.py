# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
food = input("Enter your favorite food or press q to quit: ")

# while name == "":
#     print("You didn't enter a name.")
#     name = input("Enter your name: ")
# print(f"Hello, {name}!")

# while age <= 0:
#     print("You didn't enter a valid age.")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old.")

while not food.lower() == "q":
    print(f"{food.capitalize()} is a great choice!")
    food = input("Enter another food you like or press q to quit: ")
print(f"Goodbye!")
    
