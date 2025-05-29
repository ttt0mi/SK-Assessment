number = int(input("Choose a number between 1 - 10,000? "))

sum = 0


while True:
	if number < 1 or number > 10000:
		print("Invalid Input mate, Try again..")
		number = int(input("Choose a number between 1 - 10,000? "))

	else:
		while number != 0:
			digit = number % 10
			number //= 10

			sum += digit

		print(sum)
		break