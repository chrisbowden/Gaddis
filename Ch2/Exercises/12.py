# Program calculates stock costs based on fixed inputs and outputs

num_shares = 2000
cost = num_shares * 40
purchase_commission = cost * 0.03
income = num_shares * 42.75
sale_commission = income * 0.03

print("Initial stock cost is:", cost)
print("Purchase Commission:", purchase_commission)
print("Income from stock sale:", income)
print("Sale Commissions:", sale_commission)
print()
print("Total Profit:", income - cost - sale_commission - purchase_commission)
