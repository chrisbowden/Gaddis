total = float(input('What is the total cost? '))
down_payment = float(input('How much is your deposit? '))
due = total-down_payment

print('The total due is $', due, sep='')
print('The total due is $', format(due, '.2f') , sep='')


