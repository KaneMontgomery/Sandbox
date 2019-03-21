###Kane Montgomery
MIN_LEN = 5

password = input("Please enter your password: ")
if len(password) < MIN_LEN:
    password = input("Please enter your password: ")

print(len(password) * '*')
