from flask import Flask, url_for, request, render_template
from app import app
import quandl
import math

#def cashback(x):
  #  z = x * .03
  #  x = x - z
  #  print(x)


#first page/where we collect data from the user
@app.route('/')
def itstime():
    return render_template('SENDINTHEFINISHER.html')

#second page where we display outputs to the user
#@app.route('/Had this idea for a while, but wanted to give it a shot today!', methods = ['GET','POST'])
#def itsover():
  #  if request.method == 'POST':
    #space reserved for calling the database. Most of the work comes here
    #vehicle will be the mock variable called to reference the database output
    #assuming you can even get the value. for now, put a placement value
    #    gas = 2.50
     #   gas2 = data + .05   #low point credit card
      #  gas3 = data + .10  #high point credit card
       # cash = data * vehicle
        #credit_low = gas2 * vehicle
       # credit_high = gas3 * vehicle
       # saving = cashback(credit_low)
       # saving = cashback(credit_high)
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
