number_of_months= 0
bal= 0
mini_monthly_payment= 0
outstanding_balance= float(input('Enter the outstanding balance on your credit card: '))
annual_interest_rate= float(input('Enter the annual credit card interest rate as a decimal: '))
monthly_interest_rate= (annual_interest_rate/12.0)

bal = outstanding_balance
while bal>0:
    number_of_months= 0
    bal= outstanding_balance
    mini_monthly_payment = mini_monthly_payment+ 500
    while bal> 0 and number_of_months < 12:   
        bal = (bal * (1+ monthly_interest_rate))- mini_monthly_payment
        number_of_months = number_of_months+1

print('RESULT')
print('Monthly payment to pay off debt in 1 year: '+ 'Rs.', round(mini_monthly_payment,2))
print('Number of months needed: ',number_of_months)
print('Balance:'+ 'Rs.', round(bal,2))
