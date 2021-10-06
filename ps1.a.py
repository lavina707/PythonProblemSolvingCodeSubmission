outstanding_balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))
minimum_monthly_payment_rate = float(input('Enter the minimum monthly payment rate as a decimal: '))
Total_amount_paid = 0 
for i in range(1,13):
    minimum_monthly_payment = round((minimum_monthly_payment_rate * outstanding_balance),2)
    Interest_paid = round((annual_interest_rate / 12.0  * outstanding_balance),2)
    Principal_paid = round((minimum_monthly_payment - Interest_paid),2)
    Remaining_balance = round((outstanding_balance - Principal_paid),2)
    
    print('Month' + ' ' + str(i))
    print('Minimum monthly payment: '+ 'Rs.' ,minimum_monthly_payment)
    print('Principal Paid: '+ 'Rs.',Principal_paid)
    print('Remaining balance: '+'Rs.' , Remaining_balance)
    Total_amount_paid = Total_amount_paid + minimum_monthly_payment
    outstanding_balance = Remaining_balance

print('RESULT')
print('Total amount paid: ' + 'Rs.',Total_amount_paid)
print('Remaining balance: '+'Rs.',Remaining_balance)
