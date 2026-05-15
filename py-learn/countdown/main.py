import time

my_time = int(input("Enter the number of seconds for the countdown: "))
counter = int(input("Enter the ending number for the countdown: "))

for x in reversed(range(1, counter + 1)):
    print(x)
    time.sleep(my_time)
print("Countdown complete!")
