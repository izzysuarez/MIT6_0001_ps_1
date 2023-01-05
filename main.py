# import statments:
import math

# declare variables and initialize

down_payment_perc = 0.25
current_savings = 0.0
months_saving = 0
apr = 0.04


# define a function that takes in the current savings and adds the apr/12 to the current amount
def monthly_return(current_savings):
  current_savings = current_savings + ((current_savings * apr) / 12)
  return current_savings


# get input from the user to define the annual salary and monthly savings.
annual_salary = float(input("What is your annual salary?: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved

# define the cost of the dream home
total_cost = float(input("Enter the cost of our dream home: "))
portion_down_payment = total_cost * down_payment_perc
# print()
# print("Down Payment Due: ")
# print(portion_down_payment)

# define the semi-annual raise amount as a percentage
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

while (current_savings <= portion_down_payment):
  
  # add interest on current savings to the current savings variable
  current_savings = monthly_return(current_savings)

  # add a portion of the monthy salary to the current savings
  current_savings += monthly_savings

  # increment month counter by one
  months_saving += 1

  # add if stament that redefines the annual salary every 6 months.
  if ((months_saving % 6) == 0):
    # print(months_saving)
    annual_salary = annual_salary * (1 + semi_annual_raise)
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * portion_saved

# print final savings amount and months saved
# print("Final Savings Amt: ")
# print(round(current_savings, 2))
# print()
# print("Total Months Saved: ")
print("Number of months:", months_saving)
