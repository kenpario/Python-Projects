import random


def spin_row():
    symbols = ["🍒", "🍓", "🍎", "🍋", "⭐"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍓":
            return bet * 3
        elif row[0] == "🍎":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 7
        elif row[0] == "⭐":
            return bet * 10
    return 0


def main():
    balance = 100

    print("***********************************")
    print("Welcome to the python slot machine!")
    print("    Symbols: 🍒 🍓 🍎 🍋 ⭐")
    print("***********************************")

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input. Please enter a numeric value.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance. Please enter a smaller bet.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero. Please enter a valid bet.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout:.2f}!")
            balance += payout
        else:
            print("Sorry, you lost. Better luck next time!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break
    print("***********************************")
    print(f"Your final balance is: ${balance:.2f}")


if __name__ == "__main__":
    main()
