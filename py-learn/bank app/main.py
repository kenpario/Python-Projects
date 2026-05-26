def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))

    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount


def main():

    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice(1-4): "))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                print("Exiting the program. Goodbye!")
                is_running = False
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")

    print("Thank you for using the banking program!")

if __name__ == "__main__":
    main()