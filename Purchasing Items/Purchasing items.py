print("Idea:To allow the user to select specific items and give them their final price at the end , if user buy more than 1 product of the same item than the total will according to the number of items and the bill will be given at last")

apple = 40.00
chocolate = 20.00
sprite = 40.00
pizza = 150.00
chips = 30.00

print("Apple Price : 40.00 ")
print("Chocolate Price: 20.00 ")
print("Sprite Price : 40.00 ")
print("Pizza Price : 150.00 ")
print("Chips Price : 30.00 ")
print()
print("Maximum Number of Same Items you can purchase is 5 \n")

print("Welcome to Our Store \n")
x=[1,2,3,4,5]

Price = 0

while(True):
    choice = input('Choose An Item Or Press Q to Quit:  ').lower()
    if choice == 'apple':
        Num = input("How many Apples wWould you like to buy ? :")
        if Num == '1':
            Price += apple
            print("Total :",Price)
            print()
        if Num == '2':
            Price += apple*2
            print("Total :",Price)
            print()
        if Num == '3':
            Price += apple*3
            print("Total :",Price)
            print()
        if Num == '4':
            Price += apple*4
            print("Total :",Price)
            print()
        if Num == '5':
            Price += apple*5
            print("Total :",Price)
            print()
    elif choice == 'chocolate':
        Num = input("How many chocolate wWould you like to buy ? :")
        if Num == '1':
            Price += chocolate
            print("Total :",Price)
            print()
        if Num == '2':
            Price += chocolate*2
            print("Total :",Price)
            print()
        if Num == '3':
            Price += chocolate*3
            print("Total :",Price)
            print()
        if Num == '4':
            Price += chocolate*4
            print("Total :",Price)
            print()
        if Num == '5':
            Price += chocolate*5
            print("Total :",Price)
            print()
    elif choice == 'sprite':
        Num = input("How many sprite wWould you like to buy ? :")
        if Num == '1':
            Price += sprite
            print("Total :",Price)
            print()
        if Num == '2':
            Price += sprite*2
            print("Total :",Price)
            print()
        if Num == '3':
            Price += sprite*3
            print("Total :",Price)
            print()
        if Num == '4':
            Price += sprite*4
            print("Total :",Price)
            print()
        if Num == '5':
            Price += sprite*5
            print("Total :",pizza)
            print()
    elif choice == 'pizza':
        Num = input("How many pizzas wWould you like to buy ? :")
        if Num == '1':
            Price += pizza
            print("Total :",Price)
            print()
        if Num == '2':
            Price += pizza*2
            print("Total :",Price)
            print()
        if Num == '3':
            Price += pizza*3
            print("Total :",Price)
            print()
        if Num == '4':
            Price += pizza*4
            print("Total :",Price)
            print()
        if Num == '5':
            Price += pizza*5
            print("Total :",Price)
            print()
    elif choice == 'chips':
        Num = input("How many chips wWould you like to buy ? :")
        if Num == '1':
            Price += chips
            print("Total :",Price)
            print()
        if Num == '2':
            Price += chips*2
            print("Total :",Price)
            print()
        if Num == '3':
            Price += chips*3
            print("Total :",Price)
            print()
        if Num == '4':
            Price += chips*4
            print("Total :",Price)
            print()
        if Num == '5':
            Price += chips*5
            print("Total :",Price)
            print()
    elif choice == 'q':
        print("Your Final Total is :",Price)
        print()
        break
userinfo=input("Please Enter your name : ")
userinfo1=input("Please provide your mobile no! :")
print()

print("Thank You For Shoping At Our Store")
print("Name: ",userinfo)
print("Mobile No: ",userinfo1)
print()
print("Apples :",apple*float(Num))
print("Chocolate :",chocolate*float(Num))
print("Sprite :",sprite*float(Num))
print("Pizza :",pizza*float(Num))
print("Chips :",chips*float(Num))
print()
print("Total      :",Price)