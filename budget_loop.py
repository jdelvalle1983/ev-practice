from ev_finder import pick_cars

price = int(input("Max price (0 to quit)? "))

while price != 0:
    print("Look at: " + pick_cars(price))
    

print("Done")
