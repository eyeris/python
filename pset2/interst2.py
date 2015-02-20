"""
    This program is done for calculating the minimum monthly payment
    for certain debt amount.The succesive approximations were done
    adding the 10s to each installment.
"""

balance = 3329
annualInterestRate = 0.2

monthlyPayment = 0
endBalance = balance
while endBalance > 0:
    monthlyPayment += 10
    endBalance = balance
    for i in range(12):
        endBalance -= monthlyPayment
        endBalance *= 1 + annualInterestRate/12

print "Lowest payment: " + str(monthlyPayment)
