cars = {}

with open("cars.txt") as file:
    for line in file:
        name, price = line.strip().split(",")
        cars[name] = int(price)

print(cars)
print(cars["Kia EV6"])
