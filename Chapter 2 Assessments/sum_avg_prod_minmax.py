numb1 = int(input("Enter a number : "))
numb2 = int(input("Enter another number : "))
numb3 = int(input("Enter one more number : "))

sum = numb1 + numb2 + numb3
average = sum / 3
product = numb1 * numb2 * numb3

print("The sum is", sum)
print("The average is", average)
print("The product is", product)


if numb1 >= numb2 and numb1 >= numb3:
	print("The largest number is", numb1)
	
if numb2 >= numb1 and numb2 >= numb3:
	print("The largest number is", numb2)

if numb3 >= numb1 and numb3 >= numb2:
	print("The largest number is", numb3)


if numb1 <= numb2 and numb1 <= numb3:
	print("The smallest number is", numb1)
	
if numb2 <= numb1 and numb2 <= numb3:
	print("The smallest number is", numb2)

if numb3 <= numb1 and numb3 <= numb2:
	print("The smallest number is", numb3)