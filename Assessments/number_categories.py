def categorise(*numbers, divider = 5):

	multiples = []
	multipleCounter = 0

	for number in numbers:
		if isinstance(number, (int, float)):
			if number > 0 and number % divider == 0.0:
				multiples.append(int(number))
				multipleCounter += 1
		else: raise ValueError


	if  len(numbers) == 0: return "This array is empty"
	elif all(number == 0 for number in numbers): return "There are no multiples"
	elif  multipleCounter == 0: return "There are no multiples"
	else: return tuple(multiples)


"""
print(categorise(10, 15, 21, 30))		#no edge case
print(categorise())							#no input edge case
print(categorise(0, 15, 21, 30))			#0 edge case
print(categorise(0, 0, 0, 0))				#all zeros edge case
print(categorise(0, 0, 0, 4))				#no multiples with zeros edge case
print(categorise(11, 16, 21, 31))		#no multiple edge case
print(categorise(-10, 15, 21, 30))		#negative edge case
print(categorise(10.1, 15, 21, 30))		#float edge case
print(categorise(10.0, 15, 21, 30))		#float but still multiple edge case
print(categorise(10.1, "a", True, []))	#other datatypes edge case
"""







