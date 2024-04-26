print("Idea : To write a python program which will keep adding a stream of numbers until the user presses enter and it will give the final amount as the result ")
# It is just a price calculator but the items will not be specified

Total = 0
while(True):
    userinput=input("Enter the item price or press q to quit: \n")
    if (userinput!='q'):
        Total = Total + int(userinput)
        print(f"Order Total so far : {Total}")

    else:
        print(f"Your Bill total is {Total}.Thanks for shopping !")
        break