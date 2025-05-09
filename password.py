password = str(input("Enter your password "))

password_length = len(password)


if password_length > 0 and password_length < 8:
	print("Very Weak")

elif password_length == 8:
	print("Weak")

elif password_length > 8 and password_length <= 16:
	print("Strong")

elif password_length > 16:
	print("Very Strong")

else: print("Password cannot be empty")