cars = {
    "Chevy Bolt": 27000,
    "Tesla Model 3": 39000,
    "Ford F-150 Lightning": 55000,
}

cars["Chevy Bolt"] = 25000

print(cars["Tesla Model 3"])
print(len(cars))

cars["Kia EV6"] = 43000

for name, price in cars.items():
    if price < 40000:
        print(name, price)	


