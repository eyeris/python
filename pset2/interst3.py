"""
    annual payment shedule finding for credit card sheme.
    Exhaustive enumeration and bisection search were added so that the
    ]number of steps and approximation for more realistic value is achieved.
"""

balance = 320000
annualInterestRate = 0.2

l_bound=balance/12
h_bound=(balance*(1+annualInterestRate/12)**12)/12.0
monthlyPayment = (l_bound+h_bound)/2.0
endBalance = balance
while abs(h_bound-l_bound) > 0.01:
    monthlyPayment = (l_bound+h_bound)/2.0
    endBalance = balance
    for i in range(12):
        endBalance -= monthlyPayment
        endBalance *= 1 + annualInterestRate/12
    if endBalance<0:
        h_bound=monthlyPayment
    else:
        l_bound=monthlyPayment
    
print "Lowest payment: " + str(round(monthlyPayment,2))
