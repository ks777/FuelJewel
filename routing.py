#note to self: it works, so we just need to recreate the conditions and apply it once one
#note to self 2: dont utilize the api yet. work with an initial base value and once that works, work on the website and then apply the api from there.
#how to set up the page:
#1. Intro page to set up user preference (so car make/model/year)
#2. Page to display result

from flask import Flask, url_for, request, render_template
from app import app
import math
import untangle

response = untangle.parse("http://www.fueleconomy.gov/ws/rest/fuelprices")
x = float(response.fuelPrices.regular.cdata)

#Credit card gives 3% cashback for gas purchases.
def cashback(x):
   z = x * .03
   x = x - z
   print(x)

#first page/where we collect data from the user
@app.route('/')
def itstime():
    return render_template('SENDINTHEFINISHER.html')


#second page where we display outputs to the user
@app.route('/Had this idea for a while, but wanted to give it a shot today!', methods = ['GET','POST'])
def itsover():
    if request.method == 'POST':
       cgas = input("Enter the price, in decimal form, of purchasing gas via credit card: ")
       cgas = float(cgas)
       pgas = input("Enter the percentage of gas you need to fill your tank: ")
       pgas_final = float(pgas)/100
       
       #do i need to calculate the highest credit cost
       #remember, i`m attempting to determine the best deals, so i need to assume the cheapest value
       #which appears to be a .06 credit increase
       
       cash = x * 16 * pgas_final
       cash = round(cash,2)
       print("This is the amount you would pay for a full tank, in cash: $",cash)
       credit_low = cgas * 16 * pgas_final
       print("This is the amount you would pay for a full tank, in the lowest price in credit card:$",credit_low)
       saving_low = cashback(credit_low)
       print("This is the end result of the lowest credit spending, assuming cashback: $",saving_low)       #total i spend on a full tank of gas using credit minus the $3 cashback
       if cash > saving_low:
          savings = cash - saving_low
          savings = round(savings,2)
          print("You save more with your credit card! How much more? Well you save: $",savings)
          elif saving_low > cash:
             savings = saving_low - cash
             savings = round(savings,2)
             print("You save more by using your cash at this price. You save: $", savings)
             else:
                print("DO WHATEVER, ITS THE SAME PRICE REALLY!")




