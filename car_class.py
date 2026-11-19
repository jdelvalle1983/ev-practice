class Car:
    def __init__(self, name, price, range_miles):
        self.name = name
        self.price = price
        self.range_miles = range_miles

    def is_affordable(self, budget):
        return self.price <= budget

    def describe(self):
        return f"{self.name}: ${self.price}, {self.range_miles} mi"

bolt = Car("Chevy Bolt", 25000, 259)
tesla = Car("Tesla Model 3", 39000, 272)

print(bolt.describe())
print(tesla.price)
print(bolt.is_affordable(30000))
print(tesla.is_affordable(30000))

cars= [bolt, tesla, Car("Kia EV6", 43000, 310)]
for car in cars:
    if car.is_affordable(40000):
        print(car.describe())


