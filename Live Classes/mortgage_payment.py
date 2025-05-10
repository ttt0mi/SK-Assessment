principal = float(input("How Much Do You Wish To Borrow? "))

annualinterestrate = float(input("What Annual Interest Rate Was Offered on the Mortgage? "))

durationinyears = float(input("What is the Duration of Your Mortgage Loan? "))


monthlyinterestrate = (annualinterestrate / 100) / 12

durationinmonths = durationinyears * 12


numerator = monthlyinterestrate * ((1 + monthlyinterestrate) ** durationinmonths)

denominator = ((1 + monthlyinterestrate) ** durationinmonths) - 1

mortgagepayment = principal * ( numerator / denominator )


print(f"The Value of Your Monthly Mortgage Payment amounts to {mortgagepayment : ,.2f}")











"""
other ways to format are:

print("The Value of Your Monthly Mortgage Payment amounts to {: .2f}".format(mortgagepayment) )

format() function

			or

rounded_mortgagepayment = round(mortgagepayment, 2)
print("The Value of Your Monthly Mortgage Payment amounts to ", rounded_mortgagepayment)


{} = encases the formatting process
: = introduces the format 
, = adds a comma for every thousand
.2 = formats float to 2 decimal places

f = float, d = integer, s = string

"""