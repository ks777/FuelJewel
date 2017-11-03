#yes its the price of gas currently
#IGNORE HTML PROCESS ATM, AND FOCUS ON BASE CODEWORK

import math
import untangle

response = untangle.parse("http://www.fueleconomy.gov/ws/rest/fuelprices")
x = float(response.fuelPrices.regular.cdata)

def cashback(x):
   z = x * .03
   x = x - z
   return(round(x,2))

#do i need to calculate the highest credit cost
#remember, i`m attempting to determine the best deals, so i need to assume the cheapest value
#which appears to be a .06 credit increase

cgas = input("Enter the price, in decimal form, of purchasing gas via credit card: ")
pgas = input("Enter the percentage of gas you need to fill your tank: ")

#gas2 = x + .06   #low point credit card
#print("Cost of gas using credit card, at its lowest price: $",gas2)
#gas3 = x + .10  #high point credit card/normal cost
#print("Cost of gas using credit card, at its highest price: $",gas3)

cash = x * 16 #16 is the combined mpg of the 2002 trailblazer 4WD
print("This is the amount you would pay for a full tank, in cash: $",cash)
credit_low = gas2 * 16
print("This is the amount you would pay for a full tank, in the lowest price in credit card:$",credit_low)
credit_high = gas3 * 16
print("This is the amount you would pay for a full tank, in the highest price in credit card:$",credit_high)
saving_low = cashback(credit_low)
saving_high = cashback(credit_high)
print("This is the end result of the lowest credit spending, assuming cashback: $",saving_low)       #total i spend on a full tank of gas using credit minus the $3 cashback
print("This is the end result of the highest credit spending, assuming cashback: $",saving_high)
if cash > saving_low:
   savings = cash - saving_low
   savings = round(savings,2)
   print("You save more with cash! How much more? Well you save: $",savings)
elif cash > saving_high:
   savings = cash - saving_high
   savings = round(savings,2)
   print("You save more by using cash at this price. You save: $", savings)
elif saving_high > cash:
   savings = saving_high - cash
   savings = round(savings,2)
   print("You save more by using your credit card at this price. You save: $", savings)
elif saving_low > cash:
   savings = saving_low - cash
   savings = round(savings,2)
   print("You save more by using your credit card at this price. You save: $", savings)
else:
   print("DO WHATEVER, ITS THE SAME PRICE REALLY!")


#MAIN QUESTION: DOES MY CAULCATION CHANGE IF I DON`T SPEND A FULL TANK?
#LIKE 75%/50%/25%
#it does not. reducing it all equals the same answer.
#the only thing that can change would be the credit value
#so if you do % change and credit increase change, then the values would matter a lot.
   #so: variable to initial credit value  and percentage change
   #so then you only need 2 values.


