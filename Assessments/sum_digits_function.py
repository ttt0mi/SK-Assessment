def sum_digits(number):
	if number < 1 or number > 10000:
		return "Invalid Input mate"
	else:
		sum = 0
		while number != 0:
			digit = number % 10
			number //= 10

			sum += digit

		return sum



user_number = int(input("Choose a number between 1 - 10,000? "))

print(sum_digits(user_number))
	