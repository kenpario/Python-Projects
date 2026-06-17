import datetime

date = datetime.date(2025, 5, 12)
today = datetime.date.today()

time = datetime.time(23, 30, 1)
now = datetime.datetime.now()

now = now.strftime("%d-%m-%Y" + "\n" + "%H:%M:%S")

target_datetime = datetime.datetime(2027, 5, 12, 23, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("The target datetime has already passed.")
else:
    print("The target datetime has not passed.")

# print(date)
# print(today)
# print(time)
# print(now)
# print(target_datetime)
# print(current_datetime)
