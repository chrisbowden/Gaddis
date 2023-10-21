# This program determines whether a bank customer
# qualifies for a loan

min_salary = 30000.0
min_years = 2

# Get customers salary
salary = float(input("Enter your annual salary: "))

# Get number of years in the current job
years_on_job = int(input("Enter number of years employed: "))

# Determine if customer qualifies
if salary >= min_salary:
    if years_on_job >= min_years:
        print("You qualify for the loan.")
    else:
        print("You must have been employed for at least", min_years,"years in order to qualify.")
else:
    print("You must earn at least", format(min_salary,',.2f'), "per year to qualify.")
