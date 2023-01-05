# import statments:
import math
import numpy as np

# **************************
#  ----- GLOBAL VARIABLES
# **************************

# Global variables for the annual salary and portion to save in decimal. BASED ON USER INPUT..
annual_salary = float(input("What is your annual salary?: "))
apr = 0.04
semi_annual_raise_rate = 0.07

# define a function that takes in the current savings and adds the apr/12 to the current amount
def monthly_return(current_savings):
  current_savings = current_savings + ((current_savings * apr) / 12)
  return current_savings


def number_of_months(perc_rate, ann_Sal, apr_rate, sa_rr):
  # declare variables and initialize
  down_payment_perc = 0.25
  current_savings = 0.0
  months_saving = 0
  apr = apr_rate
  
  # # define the cost of the dream home
  total_cost = float(1000000)
  portion_down_payment = total_cost * down_payment_perc
  
  # define the semi-annual raise amount as a percentage
  semi_annual_raise = float(sa_rr)
  
  
  monthly_salary = ann_Sal / 12
  portion_saved = float(perc_rate)
  monthly_savings = monthly_salary * portion_saved

  if(monthly_salary > (portion_down_payment/36)):
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
        ann_Sal = ann_Sal * (1 + semi_annual_raise)
        monthly_salary = ann_Sal / 12
        monthly_savings = monthly_salary * portion_saved
    
    # print("Rate:", months_saving)
    return months_saving
  else:
    print("It is not possible to pay the down payment in three years.")
    return None

for x in np.arange(0,1,0.0001):
  ms = number_of_months(float(x), annual_salary, apr, semi_annual_raise_rate)
  if(ms is None):
    break
  elif (ms <= 36):
    print("Rate:",round(x, 4))
    print("Number of months: __",ms)
    break


    