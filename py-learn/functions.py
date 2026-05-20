def alert():
    print("Alert!")


for x in range(3):
    alert()


def happy_birthday(name, age):
    print(f"Happy birthday, {name}! You are now {age}.")


happy_birthday("Unc", 25)


def invoice(username, amount, due_date):
    print(f"Invoice for {username}: Amount due is ${amount:.2f}, due by {due_date}.")


invoice("Alice", 155, "2024-07-01")


def add(x, y):
    z = x + y
    return z


result = add(5, 7)
print(result)
