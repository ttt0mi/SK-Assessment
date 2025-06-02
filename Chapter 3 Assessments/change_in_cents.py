"""

query = (input("This item costs 26 cents. enter 'OK' to purchase "))
print()

if query == 'OK':
	print("You paid with a dollar bill")

if query != 'OK':
	print("Ode, You still paid with a dollar bill")

"""

query = float(input("How much are you owed? "))

change_in_cents = query * 100

if change_in_cents == 0:
	print("You have no change, leave mate")

elif change_in_cents < 0 or change_in_cents > 99:
	print("impossible, Fuck off pisspot")

else:
	quarters = change_in_cents // 25		#1 quarter = 25 cents
	change_in_cents %= 25		#remaining_change_after_removing_quarters
	
	dimes = change_in_cents // 10		#1 dime = 10 cents
	change_in_cents %= 10		#remaining_change_after_removing_dimes

	nickels = change_in_cents // 5		#1 nickel = 5 cents
	change_in_cents %= 5			#remaining_change_after_removing_nickels

	pennies = change_in_cents			#1 penny = 1 cent


	print("Your change is:")
	print(quarters, "quarters")
	print(dimes, "dimes")
	print(nickels, "nickels")
	print(pennies, "pennies")