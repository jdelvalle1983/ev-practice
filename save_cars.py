cars = {
    "Chevy Bolt": 25000,
    "Tesla Model 3": 39000,
    "Kia EV6": 43000,
}

with open("cars.txt", "w") as file:
    for name, price in cars.items():
        file.write(f"{name},{price}\n")

print("Saved")
