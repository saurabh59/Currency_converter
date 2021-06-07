import requests


currency_in = input("Enter your currency (inr for indian national currency):")
currency_out = input("Enter the other currency(usd for american dollars):")
cache = {}
url = f"http://www.floatrates.com/daily/{currency_in}.json"
r = requests.get(url).json()
if currency_in != "usd":
    cache["usd"] = r["usd"]["rate"]
if currency_in != "eur":
    cache["eur"] = r['eur']["rate"]
amount = float(input("Enter the amount of money you have:"))
while True:
    print("Checking the cache...")
    if currency_out in cache:
        print("Oh! It is in the cache!")
        print(f"You received {cache[currency_out] * amount:.2f} {currency_out.upper()}.")
        print("Just press enter if you don't want to continue")
        currency_out = input("Enter the other currency")
        if currency_out == "" or currency_in == "":
            break
        amount = float(input())
    else:
        print("Sorry, but it is not in the cache!")
        j = "rate"
        print(f"You received {r[currency_out.lower()][j] * amount:.2f} {currency_out.upper()}.")
        cache[currency_out] = r[currency_out.lower()][j]
        currency_out = input()
        if currency_out == "":
            break
        amount = float(input())