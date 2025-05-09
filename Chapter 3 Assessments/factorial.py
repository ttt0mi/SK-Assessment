number = int(input("Enter a number: "))

counter = 0
factorial = 1

while(counter < number):

	factorial *= (number - counter)
	counter += 1


print(factorial)