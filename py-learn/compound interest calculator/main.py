principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Please enter a positive number for the principle.")
while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Please enter a positive number for the rate of interest.")
while time <= 0:
    time = int(input("Enter the time period in years: "))
    if time <= 0:
        print("Please enter a positive number for the time period in years.")

total = principle * (1 + rate / 100) ** time

print(f"The balance after {time} years is: ${total:.2f}")
