
# initialize variables

balance = 321513
annualInterestRate = 0.21
monthlyInterestRate = annualInterestRate / 12.0

low = balance / 12
high = (balance * (monthlyInterestRate + 1)**12)/12.0
epsilon = .01
minMonthlyPayment = (high + low)/2.0
oldBalance = balance



while True:

  for n in range(1,13):
    print "Balance on" + str(n) + "month: " + str(balance)
    balance -= minMonthlyPayment
    balance += (balance * (monthlyInterestRate))

  print "Balance: " + str(balance)
  print "Low: " + str(low)
  print "High: " + str(high)
  print "minpayment: " + str(minMonthlyPayment)

  if round(balance, 3) > epsilon:
    print 'Balance positive'
    low = minMonthlyPayment
    minMonthlyPayment = (high + low)/2.0
    print "new min monthly: " + str(minMonthlyPayment)
    balance = oldBalance
  elif round(balance, 3) < epsilon:
    print 'balance negative'
    high = minMonthlyPayment
    minMonthlyPayment = (high + low)/2.0
    print "new min monthly: " + str(minMonthlyPayment)
    balance = oldBalance
  else:
    print "minimum pay: " + str(minMonthlyPayment)
    break

  





