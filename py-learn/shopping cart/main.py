foods = []
prices = []
total = 0

while True:
    food = input("What food do you want to buy? (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"How much does {food.capitalize()} cost? $"))
        foods.append(food)
        prices.append(price)
for food in foods:
    print(food.capitalize(), end=" ")
print()
for price in prices:
    total += price
print(f"Your total is ${total:.2f}")
