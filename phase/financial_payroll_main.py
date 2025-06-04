import financial_payroll
from financial_payroll import *



payroll = {}
proceed = True

while True:

	print("""

	Financial Payroll for Terrorist

	1 >>> Add Payroll

	2 >>> View All Payrolls

	3 >>> Update Payroll

	0 >>> Exit

	""")

	choice = str(input("Choose a number: "))

	if userinput_check(choice) != True:
		print(userinput_check(choice))
		continue

	match(choice):
		
		case '1':
			while proceed:
				details = employee_details(payroll)

				if not isinstance(details, tuple):
					print(details)

					while proceed:
						choice = str(input("Enter yes to continue, no to go back to menu"))
						choice = choice.upper()

						match choice:
							case "YES":
								break

							case "NO":
								proceed = False
								break

							case _:
								print("invalid choice, try again")
								continue

				print(add(payroll, details))
				break

		case '2':
			view(payroll)
		

		case '3':
			while True:
				update_name = str(input("Enter employee's name to update details: "))

				if not update(payroll, update_name):
					print("payroll does not exist, try again")
					continue

				details = employee_details(payroll)

				if not isinstance(details, tuple):
					print(details)

					while proceed:
						choice = str(input("Enter yes to continue, no to go back to menu"))
						choice = choice.upper()

						match choice:
							case "YES":
								break

							case "NO":
								proceed = False
								break

							case _:
								print("invalid choice, try again")
								continue

				print(add(payroll, details))
				break


		case '0':
			print("okay, fuck off then")
			break;

		case _:
			print("that's invalid mate c'mon, try again")
			continue

