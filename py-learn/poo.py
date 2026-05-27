from car import Car

car1 = Car("Audi", 2007, "Black", True)
car2 = Car("Honda", 1998, "Red", False)

print(car2.model)
print(car2.year)

car1.drive()
car2.drive()
car1.stop()