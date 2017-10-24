import quandl
vehicle = quandl.get('FRED/GASALLCOVW',api_key = '-eEfb_xe_aq_RMPLStzK', data_only = "true", column_index = 1, rows = 1, sort_order = "desc", returns = "numpy" )
#for e in len(vehicle):
#    if e
print(vehicle)

