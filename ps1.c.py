outstanding_balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))
low = outstanding_balance/12.0
monthly_interest_rate = annual_interest_rate/12.0
high = (outstanding_balance*(1+monthly_interest_rate)*12.0)/12.0
balance = outstanding_balance
number_of_months=0
epsilon = 0.01   

while abs(balance)>=epsilon:
    ans = (high+low)/2.0
    balance = outstanding_balance  
    number_of_months=0 
    while number_of_months<12:        
        balance = (balance * ( 1 + monthly_interest_rate)) - ans#calculating balnce after adding interest per month and subtracting monthly payment.
        number_of_months = number_of_months + 1
    if balance>=epsilon:
        low = ans
    else:
        high = ans       
print('RESULT')
print('Monthly payment to pay off debt in 1 year: '+ 'Rs.',round(ans,2) )
print('Number of months needed: ', number_of_months)
print('Balance: ' + 'Rs.',round(balance))
