try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("That's not a valid number!")
except Exception:
    print("An unexpected error occurred.")
finally:
    print("Do some cleanup.")
