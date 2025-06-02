import random
import datetime

def random_numbers():
	numb1 = random.randint(0, 100)
	numb2 = random.randrange(numb1)
	return (numb1, numb2)

def question(numbers):
	numb1, numb2 = numbers
	print(f"what is {numb1} minus {numb2}? ")

def subtraction(numbers, answer):
	numb1, numb2 = numbers
	if (numb1 - numb2) == answer:
		return True
	else: return False
	

score_counter = 0
question_counter = 0

time = datetime.datetime.now()
while question_counter <= 10:

	numbers = random_numbers()
	attempts_per_quest_Counter = 0

	while attempts_per_quest_Counter < 2:

		question(numbers)
		answer = int(input())

		if subtraction(numbers, answer):
			print("Well done mate!")
			score_counter += 1
			break
		else:
			print("Incorrect.")
			attempts_per_quest_Counter += 1

	question_counter += 1


print(f"Your score is {score_counter}")
print(f"this took you {datetime.datetime.now() - time}")
