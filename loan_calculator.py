# function to calculate the loan amount to be paid
def loan_calculator(Amount, Rate, Time):
	Rate = float(Rate) / 100
	Time = float(Time / 12)

	if(Time < 0 or Time > 1):
		return "invalid time"
	else:
		new_amount = float((Amount * Rate * Time) + Amount)
		return new_amount

print loan_calculator(100000, 12, 12)

