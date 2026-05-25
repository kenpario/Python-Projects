doubles = []

for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

doubles = [x * 2 for x in range(1, 11)]
print(doubles)
triples = [y * 3 for y in range(1, 11)]
print(triples)
squares = [z**2 for z in range(1, 11)]
print(squares)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits = [fruit.capitalize() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)
