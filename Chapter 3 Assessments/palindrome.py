number = int(input("Enter a number: "))

main_number = number

while number != 0:
		
	digit = number % 10
	reverse_number = reverse_number * 10 + digit
	number /= 10

if main_number == reverse_number:
	print(main_number, "is a palindrome")
else:
	print(main_number, "is not a palindrome")