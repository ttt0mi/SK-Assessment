import math

PI = 0
sign = 1
term = 1
decimal_place = 2


for number in range(1, 1000000, 2):
	
	PI += sign * (4 / number)

	print(f"{PI} after term {term}")

	term += 1
	sign *= -1

	rounded_PI = round(PI, decimal_place)


	if  rounded_PI == 3.14 and decimal_place == 2:
		answer1 = term
		decimal_place += 1

	if rounded_PI == 3.141 and decimal_place == 3:
		answer2 = term
		decimal_place += 1

	if rounded_PI == 3.1415 and decimal_place == 4:
		answer3 = term
		decimal_place += 1

	if rounded_PI == 3.14159 and decimal_place == 5:
		answer4 = term
		decimal_place += 1

	if decimal_place == 6:
		break


		


print(f"Using the leibniz formula, PI equates to 3.14 after {answer1} terms")
print(f"Using the leibniz formula, PI equates to 3.141 after {answer2} terms")
print(f"Using the leibniz formula, PI equates to 3.1415 after {answer3} terms")
print(f"Using the leibniz formula, PI equates to 3.14159 after {answer4} terms")





