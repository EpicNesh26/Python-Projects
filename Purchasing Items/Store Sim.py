print("Idea : To create a python program thhat allows the user to choose item from the given options just like in a mart and than give them the total accordingly")
print()
options=["Milk","Chocolate","Can","Chips","Biscuits"]
price=[5,15,12,16,20]

TotalPrice=0

while(True):
    userinput=input("Type the item you want to buy from the given options or press Q to quit: ").lower()
    if userinput != "q":
        continue
    if userinput == "Milk":
       TotalPrice +=5
       print(TotalPrice)
