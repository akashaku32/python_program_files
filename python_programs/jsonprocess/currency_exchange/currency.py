# rates={  "USD": 1,
#     "AED": 3.6725,
#     "AFN": 86.0330,
#     "ALL": 97.5499,
#     "AMD": 386.9256,
#     "ANG": 1.7900,
#     "AOA": 824.0658,
#     "ARS": 254.7465,
#     "AUD": 1.5099,
#     "AWG": 1.7900,
#     "AZN": 1.6979,
#     "BAM": 1.7974,
#     "INR":80.0914}
from json import load
with open("C:\\Users\\idk18\OneDrive\\Desktop\python_programs\\jsonprocess\currency_exchange\\currency.json","r",encoding="UTF-8") as fread:
    data=load(fread)




amount=int(input("enter the amount:"))
fromcurrencycode=input("enter the from currency code:")
tocurrencycode=input("enter the to currency code:")
equation=(amount/(data.get("conversion_rates")).get(fromcurrencycode))*(data.get("conversion_rates")).get(tocurrencycode)
print(equation)