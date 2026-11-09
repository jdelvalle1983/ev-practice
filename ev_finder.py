import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("EV_API_KEY")
print("Key loaded:", api_key is not None)

def pick_cars(price):
    if price < 20000:
        return "Chevy Bolt, Nissan Leaf"
    elif price < 35000:
        return "Tesla Model 3, Kia EV6"
    elif price < 60000:
        return "Ford F-150 Lightning, Rivian R1T"
    else:
        return "Tesla Model S, Rivian R1S"

if __name__== "__main__":
    price = int(input("Max price? "))
    print("Look at: " + pick_cars(price)) 
    