total_spending = int(input("How much did you spend at the store: "))

if total_spending == 0:
	print("Why are you here?! Police! he wants to steal!")

elif total_spending > 0 and total_spending < 1000:
	print("Apologies mate, people below the poverty line cannot be offered discounts")

elif total_spending >= 1000 and total_spending <= 10000:
	print("You are entitled to a 5% discount")
	print(f"Your new price to pay is ${total_spending - (0.05 * total_spending):,.2f}")

elif total_spending > 10000 and total_spending <= 50000:
	print("You are entitled to a 10% discount")
	print(f"Your new price to pay is ${total_spending - (0.1 * total_spending):,.2f}")

elif total_spending > 50000:
	print("You are entitled to a 20% discount")
	print(f"Your new price to pay is ${total_spending - (0.2 * total_spending):,.2f}")

else:
	print("please use your brain")