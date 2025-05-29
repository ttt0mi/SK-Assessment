number_of_students = int(input("Enter the number of students: "))

max_score = -1000 ** 1000
max_score_name = str("")


if number_of_students < 0:
	print("Invalid Input")

elif number_of_students == 0:
	print("There are no students")

else:
	for students in range(number_of_students):

		student_name = str(input("What is this students' name? "))
		score = int(input("and what was their score? "))
		print()

		if score > max_score:
			max_score = score
			max_score_name = student_name

		elif score == max_score:
			max_score = score
			max_score_name = max_score_name + " & " + student_name

	
	print(f"The highest in class is {max_score_name} with a score of {max_score}")


