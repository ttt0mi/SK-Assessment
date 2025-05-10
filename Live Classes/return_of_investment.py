investment_amount = float(input("What amount do you want to invest? "))

interest_rate_in_decimal = int(input("What is the interest rate offered on your investment? ")) / 100

years =  int(input("How many years do you want this investment to last? "))


for year in range(1, years + 1):
	 
	investment_amount = (investment_amount * interest_rate_in_decimal) + investment_amount

	print(f"after year {year}. The return on your investment is {investment_amount:,.3f}")

