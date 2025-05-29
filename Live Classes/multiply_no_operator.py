def multiply(numb1, numb2):
	
	sum = 0

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


number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

print(multiply(number1, number2))