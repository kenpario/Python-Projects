age = int(input("Please enter your age: "))

if age < 18 and age >= 0:
    print("You can not make a credit card application.")
elif age < 0 or age > 120:
    print("Invalid age entered.")
else:
    print("You can make a credit card application.")