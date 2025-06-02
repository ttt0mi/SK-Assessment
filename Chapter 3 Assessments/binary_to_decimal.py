decimal_number = 0

binary_number = int(input("Enter a binary Number: "))

#binary_number_string = str(binary_number)

binary_number_length = len(str(binary_number))

for exponent in range(binary_number_length):

	digit = binary_number % 10
	binary_number //= 10

	decimal_of_digit = digit * 2 ** exponent

	decimal_number += decimal_of_digit
	

print(decimal_number)

