username = input("Enter your username: ")
username_len = len(username)
username_spaces = username.count(" ")
username_isdigit = username.isdigit()

print("Valid username" if username_len <= 12 and username_spaces == 0 and not username_isdigit else "Invalid username")