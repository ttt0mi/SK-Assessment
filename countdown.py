n = int(input("Enter a positive integer to begin: "))

while n < 1:
	print("invalid mate, Try again")
	n = int(input("Enter a positive integer to begin: "))

for countdown in range(n, 0, -1):

	print(countdown)

	if countdown == 1:
		print("Blast Off!")