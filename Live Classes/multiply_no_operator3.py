def multiply(numb1, numb2):
	
	sum = 0

	if isinstance(numb2, float):

		string = str(numb2)
		number = string.split('.', 1)
		integer2 = int(number[0])
		decimal2 = int(number[1])

		exponential = 10 ** len(number[1])

		if numb2 < 0:
			for count in range(abs(integer2)):
				sum += numb1
			for count in range(decimal2):
				sum += (numb1/exponential)

			return -sum

		elif numb1 < 0:
			for count in range(integer2):
				sum += abs(numb1)
			for count in range(decimal2):
				sum += (abs(numb1)/exponential)

			return -sum

		else:
			for count in range(integer2):
				sum += numb1
			for count in range(decimal2):
				sum += numb1/exponential

			return sum

	
	if isinstance(numb2, int):

		if numb2 < 0:
			for count in range(abs(numb2)):
				sum += numb1
			return -sum

		elif numb1 < 0:
			for count in range(numb2):
				sum += abs(numb1)
			return -sum

		else:
			for count in range(numb2):
				sum += numb1
			return sum


number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

print(multiply(number1, number2))