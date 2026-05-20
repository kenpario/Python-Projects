menu = {
    "popcorn": 4.00,
    "pizza": 5.00,
    "fries": 3.00,
    "drink": 2.00,
    "candy": 1.00,
    "pretzel": 3.50,
    "hot dog": 4.50,
}

cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select an item you would like to purchase (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu[food]
        print(f"{food} added to cart. Total: ${total:.2f}")

print("---------- TOTAL ----------")
print(f"Final total: ${total:.2f}")