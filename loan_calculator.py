# function to calculate the loan amount to be paid

def loan_calculator(Amount, Rate, Time):

	if(isinstance(Amount, (int, float)) == False or isinstance(Rate, (int, float))  == False or isinstance(Time, (int, float))  == False):
		return "invalid input"
	elif(Amount <= 0):
		return "invalid amount"
	elif (Rate <= 0 or Rate > 100):
		return "invalid rate"
	elif(Time <= 0 or Time > 12):
		return "invalid time"
	else:
		Rate = float(Rate) / 100
		Time = float(Time / 12)
		new_amount = float((Amount * Rate * Time) + Amount)
		return new_amount

print loan_calculator(100000, 12, 12)

