principal = 1000
annual_rate = 7

annual_rate_in_decimal = 7/100

for years in range(1, 31):

	deposit_amount_year = principal * ((1 + annual_rate_in_decimal) ** years)

	print(f"The deposit amount after year {years} is ${deposit_amount_year:,.2f}")
