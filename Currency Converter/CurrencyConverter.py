with open('Currency.txt') as f:
    lines = f.readlines()

currencydict={}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]]=parsed[1]

amount = int(input("Enter amount : \n"))
print("Enter the name of the currency you want to convert this amount to ?? \n Available Options : \n ")
[print(item) for item in currencydict.keys()]
Currency = (input("Please enter one of the values:  "))
Chosencur = {float(currencydict[Currency])}
print(f"{amount} INR is equal to {amount *float(currencydict[Currency])} {Currency}")
