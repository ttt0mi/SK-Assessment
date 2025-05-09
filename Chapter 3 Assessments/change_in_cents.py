query = (input("This item costs 26 cents. enter 'OK' to purchase "))
print()

if query == 'OK':
	print("You paid with a dollar bill")

if query != 'OK':
	print("Ode, You still paid with a dollar bill")


change_in_cents = 100 - 26

if change_in_cents == 0:
	print("Ypu have no change, leave mate")

elif change_in_cents < 0 or change_in_cents > 99:
	print("impossible, Fuck off pisspot")

else:
	quaters = change_in_cents // 25		#1 quater = 25 cents
	change_in_cents %= 25			#remaining_change_after_removing_quaters
	
	dimes = change_in_cents // 10		#1 dime = 10 cents
	change_in_cents %= 10			#remaining_change_after_removing_dimes

	pennies = change_in_cents			#1 penny = 1 cent


	print("Your change is:")
	print(quaters, "quaters")
	print(dimes, "dimes")
	print(pennies, "pennies")