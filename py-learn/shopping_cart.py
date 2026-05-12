item = input("What item would you like to buy?: ")
price = float(input(f"What is the price of {item}?: "))
quantity = int(input(f"How many {item}s would you like to buy?: "))
cost = price * quantity
print(f"The total cost of {quantity} {item}(s) is: ${cost}")