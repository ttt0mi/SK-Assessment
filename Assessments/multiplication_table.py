print("\t", end = " ")

for header in range(1, 10):

	print(f"{header}\t", end = " ")

print()

print("---------------------------------------------------------------------------")

for row in range(1, 10):

	print(f"{row:<2}|\t", end = "")

	for column in range(1, 10):

		print(f"{row * column:>2}\t", end = "")

	print()