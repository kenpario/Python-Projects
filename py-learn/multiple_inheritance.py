class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} the animal eats.")

    def sleep(self):
        print(f"{self.name} the animal sleeps.")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} the prey flees!")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} the predator hunts!")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
hawk.sleep()
fish.eat()
fish.sleep()
