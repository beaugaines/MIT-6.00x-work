
# initialize variables

balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 10
goal = 0
epsilon = 20
oldBalance = balance


while True:
  for month in range(1,13):
    balance -= monthlyPayment
    interest = balance * monthlyInterestRate
    balance += interest

  print "Balance after month " + str(month) + ": "  + str(balance)

  if balance > 0:
    monthlyPayment += 10
    print("Month pay now: " + str(monthlyPayment) )
    balance = oldBalance
  else:
    break


print("Lowest Payment: " + str(monthlyPayment))


