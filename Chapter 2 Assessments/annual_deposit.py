principal = 1000
annual_rate = 7
annual_rate_in_decimal = 7/100
years = 10

deposit_amount_year1 = principal * ((1 + annual_rate_in_decimal) ** years)
deposit_amount_year2 = principal * ((1 + annual_rate_in_decimal) ** (years * 2))
deposit_amount_year3 = principal * ((1 + annual_rate_in_decimal) ** (years * 3))

print("The deposit amount afrter 10 years is $", deposit_amount_year1)
print("The deposit amount afrter 20 years is $", deposit_amount_year2)
print("The deposit amount afrter 30 years is $", deposit_amount_year3)