


passes = 0
failures = 0
valid_user_input = 0

while valid_user_input < 10:

	result = int(input("Enter Result(1 for passed, 2 for failures): "))

	if result == 1:
		passes += 1
		valid_user_input += 1

	elif result == 2:
		failure += 1
		valid_user_input += 1

	else:
		print("Invalid input, Try again..")
print(f" Number of passes: {passes}")
print(failures)

if passes > 8:
	print("Kudos to the instructor")


