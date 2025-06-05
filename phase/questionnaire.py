import random


def user_input_check(user_input):

	if not user_input or user_input.isspace():
		return False

	elif user_input.isdecimal():
		user_input = int(user_input)

		if user_input in range(1, 11): return True
		else: return False

	else:
		return False



def question1(proceed = False):
	
	if proceed:

		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is 5 + 5?
			option A ->  25
			option B ->  10
			option C ->  5

			""")

			choice = str(input("make a choice(A, B or C): "))
		
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("correct")
					return True

				case "C":
					print("incorrect")
					attempts_counter += 1
					continue

				case _:
					print("invalid choice")
					continue

		return "Q: What is 5 + 5?. A: 10"
	pass



def question2(proceed = False):

	if proceed: 
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is 45 6 * 1854?
			option A ->  lool dawg i dont know
			option B ->  100000
			option C ->  5e7

			""")

			choice = str(input("make a choice(A, B or C): "))
		
			choice = choice.upper()

			match choice:
				case "A":
					print("correct")
					return True

				case "B":
					print("incorrect")
					attempts_counter += 1
					continue

				case "C":
					print("incorrect")
					attempts_counter += 1
					continue

				case _:
					print("invalid choice")
					continue


		return "Q: What is 45 6 * 1854?. A: lool dawg i dont know"
	pass

	
def question3(proceed = False):
	
	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is your net worth?
			option A ->  £something
			option B ->  blah blah blah
			option C ->  you're worthless

			""")

			choice = str(input("make a choice(A, B or C): "))
			
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("incorrect")
					attempts_counter += 1
					continue

				case "C":
					print("correct")
					return True

				case _:
					print("invalid choice")
					continue


		return "Q: What is your net worth?. A: you're worthless"
	pass

	
def question4(proceed = False):
	
	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is 5 + 6?
			option A ->  26
			option B ->  11
			option C ->  1

			""")

			choice = str(input("make a choice(A, B or C): "))
		
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("correct")
					return True

				case "C":
					print("incorrect")
					attempts_counter += 1
					continue

				case _:
					print("invalid choice")
					continue


		return "Q: What is 5 + 6? . A: 11"
	pass
	
def question5(proceed = False):
	
	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			How many punic wars occurred?
			option A ->  5
			option B ->  2
			option C ->  3

			""")

			choice = str(input("make a choice(A, B or C): "))
			
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("incorrect")
					attempts_counter += 1
					continue
	
				case "C":
					print("correct")
					return True

				case _:
					print("invalid choice")
					continue


		return "Q: How many punic wars occurred? .A: 3"
	pass
	
def question6(proceed = False):
	
	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is your name?
			option A ->  you think i know?
			option B ->  i really care
			option C ->  fuck off

			""")

			choice = str(input("make a choice(A, B or C): "))
		
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("incorrect")
					attempts_counter += 1
					continue

				case "C":
					print("correct")
					return True

				case _:
					print("invalid choice")
					continue

		return "Q: What is your name? .A: fuck off"
	pass

	
def question7(proceed = False):

	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is 200 / 4?
			option A ->  100
			option B ->  50
			option C ->  75

			""")

			choice = str(input("make a choice(A, B or C): "))
		
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("correct")
					return True

				case "C":
					print("incorrect")
					attempts_counter += 1
					continue

				case _:
					print("invalid choice")
					continue


		return "Q: What is 200 / 4? .A: 50"
	pass

	
def question8(proceed = False):

	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			When did WW2 start?
			option A ->  1939
			option B ->  1915
			option C ->  1962

			""")

			choice = str(input("make a choice(A, B or C): "))
		
			choice = choice.upper()

			match choice:
				case "A":
					print("correct")
					return True

				case "B":
					print("incorrect")
					attempts_counter += 1
					continue
	
				case "C":
					print("incorrect")
					attempts_counter += 1
					continue

				case _:
					print("invalid choice")
					continue


		return "Q: When did WW2 start? .A: 1939"
	pass

	
def question9(proceed = False):

	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is 5 / 5?
			option A ->  5
			option B ->  55
			option C ->  1

			""")

			choice = str(input("make a choice(A, B or C): "))
			
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("incorrect")
					attempts_counter += 1
					continue

				case "C":
					print("correct")
					return True

				case _:
					print("invalid choice")
					continue


		return "Q: What is 5/5? .A: 1"
	pass
	
def question10(proceed = False):
	
	if proceed:
		attempts_counter = 0

		while attempts_counter < 2:

			print("""
			What is 1 + 10?
			option A ->  10
			option B ->  11
			option C ->  5

			""")

			choice = str(input("make a choice(A, B or C): "))
		
			choice = choice.upper()

			match choice:
				case "A":
					print("incorrect")
					attempts_counter += 1
					continue

				case "B":
					print("correct")
					return True

				case "C":
					print("incorrect")
					attempts_counter += 1
					continue

				case _:
					print("invalid choice")
					continue


		return "Q: What is 1 + 10? .A: 11"
	pass
	

proceed = True

while proceed:

	questions = {0 : question1, 1 : question2, 2 : question3, 3 : question4, 4 : 	question5, 5 : question6, 6 : question7, 7 : question8, 8 : question9, 9 : question10}

	random.shuffle(questions)

	missed_questions = []

	question_counter = 0
	correct_counter = 0
	missed_counter = 0


	while question_counter < 10:

		user_input = str(input("choose a number between 1 - 10: "))

		if not user_input_check(user_input):
			print("invalid input, try again")
			continue

		user_input = int(user_input)
		user_input = user_input - 1

		if user_input in questions.keys():

			q = questions.get(user_input)
			q(True)
		
			if q:
				question_counter += 1
				correct_counter += 1
			else:
				question_counter += 1
				missed_counter += 1
				missed_questions.append(q)

			questions.pop(user_input)

		else:
			print("Question already answered")
			continue


	print(f"correct: {correct_counter}")
	print(f"missed: {missed_counter}")
	for item in missed_questions:
		print(f"{item}\n")

	while True:
		user_continue = str(input("Enter yes to continue, no to quit: "))
		user_continue = user_continue.upper()

		match user_continue:
			case "YES":
				break

			case "NO":
				proceed = False
				break

			case _:
				print("invalid choice, try again")
				continue














