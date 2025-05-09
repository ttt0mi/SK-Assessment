gallons_used = float(input("How many gallons of fuel did you use?(enter -1 to get results) "))

total_gallons_used = 0
total_miles_driven = 0

while gallons_used != -1:

	miles_driven = float(input("How many miles did you drive? "))


	miles_driven_per_gallon = miles_driven / gallons_used
	print(f"The miles used per gallon for this tank was {miles_driven_per_gallon:.6f}")
	

	total_gallons_used += gallons_used	
	total_miles_driven += miles_driven

	gallons_used = float(input("How many gallons of fuel did you use?(enter -1 to get results) "))


average = total_miles_driven / total_gallons_used

print(f"Your overall average miles per gallon was {average:.6f}")
	
	