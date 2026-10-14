import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("EV_API_KEY")
print("Key loaded:", api_key is not None)

price = int(input("Max price? "))

if price < 20000:
    print("Look at: Chevy Bolt, Nissan Leaf")
elif price < 35000:
    print("Look at: Tesla Model 3, Kia EV6")
else:
    print("Look at: Rivian R1T, Tesla Model S")
