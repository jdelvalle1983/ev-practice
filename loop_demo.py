from ev_finder import pick_cars

prices = [15000, 20000, 35000, 59999, 60000]

for price in prices:
   print(price, pick_cars(price))
   print 
