rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the last number: "))

for x in range(rows):
    for y in range(1, columns + 1):
        print(y, end=" ")
    print()
