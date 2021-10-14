# Tip Calculator


# Welcome to Currie's five star steak house message
print("Welcome to Currie's Steak House")

# Users input number of party
people_of_party = float(input("how many people are in your party: "))

# Users input cost of meal
cost_of_meal = float(input('cost of meal '))

# added 10% tax
tax = .10

# Users tip percent input
tip_percent = float(input('tip percent: '))

# Calculating tax
total_bill = cost_of_meal * tax 

# Calculating total bill plus tip
tip_amount = total_bill + tip_percent

# Calculating tip per person
dividing_the_bill = total_bill / people_of_party


# printing amount of tip
print(f'your tip is ${total_bill}')

# printing tip by person
print(f'split the tip each person needs to pay $ {(round(dividing_the_bill, 2))}:')