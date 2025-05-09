max_number = -1000 ** 1000
second_max_number = -1000 ** 1000

for count in range(10):
	
	number = int(input("Enter your number: "))

	if number > max_number:
		second_max_number = max_number
		max_number = number
			
	elif number > second_max_number:
		second_max_number = number


print(f"{max_number} is the largest number")
print(f"{second_max_number} is the 2nd largest number")
