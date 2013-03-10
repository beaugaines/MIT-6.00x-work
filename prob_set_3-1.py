
# initialize variables

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0

low = balance / 12
high = round((balance * (monthlyInterestRate + 1)**12)/12.0, 2)
epsilon = .10
minMonthlyPayment = round((high + low)/2.0, 2)
oldBalance = balance
difference = 0



while True:

  for n in range(1,13):
    print "Balance on" + str(n) + "month: " + str(balance)
    balance -= minMonthlyPayment
    balance += (balance * (monthlyInterestRate))

  # print "Balance: " + str(balance)
  print "Low: " + str(low)
  print "High: " + str(high)
  print "minpayment: " + str(minMonthlyPayment)

  if balance - minMonthlyPayment > 0:
    print 'Balance positive'
    low = minMonthlyPayment
    minMonthlyPayment = (high + low)/2.0
    print "new min monthly: " + str(minMonthlyPayment)
    balance = oldBalance
  elif balance - minMonthlyPayment < 0:
    print 'balance negative'
    high = minMonthlyPayment
    minMonthlyPayment = (high + low)/2.0
    print "new min monthly: " + str(minMonthlyPayment)
    balance = oldBalance
  else:
    print "minimum pay: " + str(minMonthlyPayment)
    break

  





