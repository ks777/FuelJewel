#yes its the price of gas currently
#IGNORE HTML PROCESS ATM, AND FOCUS ON BASE CODEWORK

import math
import untangle

response = untangle.parse("http://www.fueleconomy.gov/ws/rest/fuelprices")
x = float(response.fuelPrices.regular.cdata)

def cashback(x):
   z = x * .03
   x = x - z
   return(x)


gas2 = x + .05   #low point credit card
print(gas2)
gas3 = x + .10  #high point credit card
print(gas3)
cash = x * 16 #16 is the combined mpg of the 2002 trailblazer 4WD
print(cash)
credit_low = gas2 * 16
print(credit_low)
#credit_high = gas3 * 16
#print(credit_high)
saving_low = cashback(credit_low)
#saving_high = cashback(credit_high)
print(saving_low)
#print(saving_high)

