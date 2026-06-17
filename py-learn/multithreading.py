import threading
import time


def walk_dog(name, place):
    time.sleep(8)
    print(f"You finished walking {name} at {place}")


def take_out_trash():
    time.sleep(5)
    print("You finished taking out the trash")


def do_dishes():
    time.sleep(3)
    print("You finished doing the dishes")


chore1 = threading.Thread(target=walk_dog, args=("Scooby", "the park"))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=do_dishes)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print(f"All chores are complete")
