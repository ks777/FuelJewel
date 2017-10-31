#yes its the price of gas currently
#IGNORE HTML PROCESS ATM, AND FOCUS ON BASE CODEWORK

import untangle

response = untangle.parse("http://www.fueleconomy.gov/ws/rest/fuelprices")
print(response.fuelPrices.regular.cdata)

