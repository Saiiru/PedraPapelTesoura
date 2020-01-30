print("-----------------------------------")
print("Rock, Paper, Scissors Account Setup")
print("-----------------------------------")
while True:
    username = input("Pick a username:  ")
    password = input("Pick a password:  ")
    password_confirm = input("Please confirm your password:  ")

    if password != password_confirm:
        print("Your passwords don't match. Please try again.")

    if password == password_confirm:
        print("Your Account has been setup.")
        text_file = open("accounts.txt","a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break
