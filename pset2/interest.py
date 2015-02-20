"""
This code is done for calculating the interest rates and the installment values for credit card debt.
"""


balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

rbalance=balance
minpayment=0.00
ipayable=0.00
interest=0.00
total=0.00
for i in range(1,13):
    print "Month:  "+str(i)
    minpayment=float(rbalance*monthlyPaymentRate)
    print "Minimum Monthly Payment :"+str(round(minpayment,2))
    ipayable=float (rbalance-minpayment)
    interest=float(ipayable*annualInterestRate/12)
    total+=minpayment
    rbalance=float(ipayable+interest)
    print "Remaining balance: "+str(round(rbalance,2))
print "Total paid: "+str(round(total,2))
print "Remaining balance: "+str(round(rbalance,2))
