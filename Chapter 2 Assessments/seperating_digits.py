numb = int(input("Enter a number : "))

if numb < 10000 or numb > 99999:
	print("invalid")

if numb >= 10000 and numb <= 99999:

	digit1 = numb % 10
	numb = numb // 10

	digit2 = numb % 10
	numb = numb // 10

	digit3 = numb % 10
	numb = numb // 10

	digit4 = numb % 10
	numb = numb // 10

	digit5 = numb % 10
	numb = numb // 10


print(digit5, "   ", digit4, "   ", digit3, "   ", digit2, "   ", digit1)