numb1 = float(input("Enter a number : "))
numb2 = float(input("Enter another number : "))
numb3 = float(input("Enter one more number : "))


if numb1 <= numb2 and numb1 <= numb3:
	smallest_numb = numb1

	if numb2 <= numb3:
		second_smallest_numb = numb2
	if numb3 <= numb2:
		second_smallest_numb = numb3

	
if numb2 <= numb1 and numb2 <= numb3:
	smallest_numb = numb2

	if numb1 <= numb3:
		second_smallest_numb = numb1
	if numb3 <= numb1:
		second_smallest_numb = numb3


if numb3 <= numb1 and numb3 <= numb2:
	smallest_numb = numb3

	if numb2 <= numb1:
		second_smallest_numb = numb2
	if numb1 <= numb2:
		second_smallest_numb = numb1



if numb1 >= numb2 and numb1 >= numb3:
	largest_numb = numb1
	
if numb2 >= numb1 and numb2 >= numb3:
	largest_numb = numb2
	
if numb3 >= numb1 and numb3 >= numb2:
	largest_numb = numb3


print(f"{smallest_numb}, {second_smallest_numb}, {largest_numb}")