
# initialize variables

totalPaid = 0
balance = 4213
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentRate = 0.04

for month in range(1,13):
    print("Month: " + str(month))
    
    minPayment = balance * monthlyPaymentRate
    balance -= minPayment
    monthlyInterest = balance * monthlyInterestRate
    totalPaid += minPayment
    balance += monthlyInterest
    print("Minimum monthly payment: %.2f" % minPayment)
    print("Remaining balance: %.2f\n" % balance)

print("Total paid: %.2f" % totalPaid)
print("Remaining balance: %.2f" % balance)