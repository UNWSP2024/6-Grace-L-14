'''Tax Rate Program
By Grace LeVoir
2 - 26 - 26'''

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

'''Pseudocode:'''
#Collect total sales
#Calculate state sales tax
#   Multiply total sales by state tax rate
#Calculate county sales tax
#   Multiply total sales by county tax rate
#Calculate total sales tax
#   Add state sales tax and county sales tax
#Display state tax, county tax, and total

total_sales = float(input('Enter total sales: $'))

def state_tax():
    tax = total_sales * 0.05
    return tax

def county_tax():
    tax = total_sales * 0.025
    return tax

def total_tax():
    tax = state_tax() + county_tax()
    return tax

print(f'The state sales tax is ${state_tax():.2f}')
print(f'The county sales tax is ${county_tax():.2f}')
print(f'The total sales tax is ${total_tax():.2f}')