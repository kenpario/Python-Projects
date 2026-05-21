def add(*args):
    return sum(args)


print(add(2, 3))
print(add(2, 3, 4))
print(add(2, 3, 4, 5))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("John", "Doe")
display_name("Dr", "Doom")

def print_address(**kwargs):
    for value in kwargs.values():
        print(value)
    for key in kwargs.keys():
        print(key)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Main St", 
              city="Anytown", 
              state="CA", 
              zip_code="12345")