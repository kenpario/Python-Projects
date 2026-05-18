fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "tomato"]
meats = ["chicken", "beef", "pork"]

grocery_list = [fruits, vegetables, meats]

print(grocery_list)
print(grocery_list[0][1])

for collection in grocery_list:
    for item in collection:
        print(item)
    print()
