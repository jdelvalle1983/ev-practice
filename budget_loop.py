from ev_finder import pick_cars

while True:
    try:
        price = int(input("Max price (0 to quit)? "))
    except ValueError:
        print("Please type a number.")
        continue
    if price == -5:
        print("Price must be positive.")
        continue
    if price == 0:
        break
    print("Look at: " + pick_cars(price))

print("Done")
