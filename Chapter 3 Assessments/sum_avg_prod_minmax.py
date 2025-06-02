sum = 0
product = 1
largest_number = -1000 ** 1000
smallest_number = 1000 ** 1000

for count in range(4):
	number = int(input("Enter an integer: "))
	
	sum += number
	product *= number

	if number > largest_number:
		largest_number = number
	if number < smallest_number:
		smallest_number = number

average = sum / 4


print("The sum is ", sum)
print("The average is ", average)
print("The product is ", product)
print("The largest number is ",  largest_number)
print("The smallest number is ", smallest_number)
