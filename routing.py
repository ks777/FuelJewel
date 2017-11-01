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
    #space reserved for calling the database. Most of the work comes here
    #vehicle will be the mock variable called to reference the database output
    #assuming you can even get the value. for now, put a placement value
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
        
        #would need to add car model when database is finished
        #if credit_high > cash:
          #  int returned = credit_high - cash
         #   return render_template('Ialwaysgottasendinthefinisher1.html', credit_high = credit_high, cash = cash )
        #elif credit_high < cash:
         #   int returned = cash - credit_high
          #  return render_template('Ialwaysgottasendinthefinisher1.html', credit_high = credit_high, cash = cash )
        #elif credit_low > cash:
         #   int returned = credit_low - cash
          #  return render_template('Ialwaysgottasendinthefinisher2.html', credit_low = credit_low, cash = cash )
        #elif credit_low < cash:
         #   int returned = cash - credit_low
          #  return render_template('Ialwaysgottasendinthefinisher2.html', credit_low = credit_low, cash = cash )
        #else:
        #    return render_template('Ialwaysgottasendinthefinisher3.html')  
    #API_response = requests.get("https://www.quandl.com/api/v3/datasets/FRED/GASALLCOVW")
    #gas_price = response.data[0]
    #else:
     #   shutdown_server()
     #   return('Thank you for using our product!')
