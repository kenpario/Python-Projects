class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print("WOOF!")

class Cat(Animal):
    def judge(self):
        print("JUDGES YOU!")

class Mouse(Animal):
    def run(self):
        print(f"RUNNING FROM {cat.name}")


dog = Dog("Qin")
cat = Cat("Captain Whiskers")
mouse = Mouse("Minnie")

print(dog.name)
print(dog.is_alive)
print(cat.name)
print(cat.is_alive)
print(mouse.name)
print(mouse.is_alive)
dog.eat()
cat.sleep()
mouse.eat()
dog.bark()
cat.judge()
mouse.run()
