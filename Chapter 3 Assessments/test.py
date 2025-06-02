for number in range(1):


	for row in range(10):
		for column in range(row):
			print("*", end = "")
		print()


	for row in range(10):
		print("		", end = "")
		for column in range(row, 10):
			print("*", end = "")
		print()


	for row in range(10):
		print("				", end = "")
		for column in range(row):
			print(" ", end = "")
		for column in range(row, 10):
			print("*", end = "")
		print()


	for row in range(10):
		print("						", end = "")
		for column in range(row, 10):
			print(" ", end = "")
		for column in range(row):
			print("*", end = "")
		print()

		