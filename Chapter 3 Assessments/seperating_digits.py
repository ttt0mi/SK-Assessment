number = int(input("Enter a number: "))

result = str(" ")

if number < 10000 or number > 99999:
	print("invalid")

if number >= 10000 and number <= 99999:

	while number != 0:

		digit = str(number % 10)
		number //= 10

		result = "   " + digit + result


print(result)