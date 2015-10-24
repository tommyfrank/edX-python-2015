balance = int(raw_input('Enter a balance: '))
annualInterestRate = float(raw_input('Enter an annual interest rate: '))
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12)**12) / 12.0
guess = 0
remainingBalance = balance

while abs(remainingBalance) > 0.01:
    remainingBalance = balance
    guess = (lowerBound + upperBound)/2
    for month in range(1, 13):
        remainingBalance -= guess
        remainingBalance += remainingBalance * annualInterestRate / 12
    if (remainingBalance > 0):
        lowerBound = guess
    else:
        upperBound = guess
guess = (round(guess * 100)) / 100
print('Lowest payment: ' + str(guess))