import math

# garlic_bread = 10

# # garlic_bread += 1
# # garlic_bread -= 1
# # garlic_bread *= 2
# # garlic_bread /= 2
# # garlic_bread %= 2
# garlic_bread **= 2

# print(garlic_bread)

# x = 3.14
# y = -8
# z = 2
# # result = round(x)
# # result = abs(y)
# # result = pow(z,5)
# # result = max(x,y,z)
# # result = min(x,y,z)

# # print(result)
# print(math.pi)
# print(math.e)
# print(math.sqrt(9))
# print(math.ceil(9.1))
# print(math.floor(9.9))

r = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * r
print(f"The circumference of the circle is: {round(circumference,2)}")
area = math.pi * r ** 2
print(f"The area of the circle is: {round(area,2)}")