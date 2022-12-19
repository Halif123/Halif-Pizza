credit = 0
print(credit)


def addcredit():
    print("Input yes or no")
    request = input("Do you want to purchase credit:")
    if request == "yes":
        global credit
        credit = int(input("How much credit would you like to add:"))
        balance: int = 0
        credit = balance + credit
        print("your new balance is", credit, "credits")
    if request == "no":
        print("you may proceed")
    str(input("would you like to add more credit:"))
    if request == "yes":
        balance = int(input("How much credit would you like to add:"))
        credit += balance
        print("your new balance is", balance)

    if request == "no":
        print("you may proceed")


def orderpizza():
    global credit
    t = credit
    statement = "ORDER PIZZA - SELECT SIZE [current baLance = {} credits]"
    print(statement.format(t))
    while True:
        print("Please choose from the following options:")
        print("1. 7 inch [3.0 Credits]")
        print("2. 9 inch [5.50 Credits]")
        print("3. 14 inch [7.25 Credits]")
        print("0. Return to the main menu")
        C = int(input("Enter a number:"))
        if C == 1:
            inch = 7
            credit -= 3.0
            print("you have selected", inch, "inch pizza your current balance",credit)
        elif C == 2:
            inch = 9
            credit -= 5.50
            print("you have selected", inch, "inch pizza your current balance",credit)
        elif C == 3:
            inch = 14
            credit -= 7.25
            print("you have selected", inch, "inch pizza your current balance",credit)
        elif C == 0:
            break
        else:
            print("wrong input")

        while True:
            print("select toppings from this option")
            print("1. Ham [0.80 Credits]\n", "2. Mushroom [0.50 Credits]\n", "3. Pepperoni [1.00 Credits]\n"
                                                                             "4. Olives [0.30 Credits]\n",
                  "5. Pineapple [0.60 Credits]\n", "6. Extra cheese [1.20 Credits]\n",
                  "0. Return to the main menu\n")
            toppings = int(input("enter a number:"))
            if toppings == 1:
                credit -= 0.80
                print("you have added ham to your pizza. your current credit is:", credit)
                break
            elif toppings == 2:
                credit -= 0.50
                print("you have added mushroom to your pizza. your current credit is:", credit)
            elif toppings == 3:
                credit -= 1.00
                print("you have added mushroom to your pizza. your current credit is:", credit)
            elif toppings == 4:
                credit -= 0.30
                print("you have added mushroom to your pizza. your current credit is:", credit)
            elif toppings == 5:
                credit -= 0.60
                print("you have added mushroom to your pizza. your current credit is:", credit)
            elif toppings == 6:
                credit -= 1.20
                print("you have added mushroom to your pizza. your current credit is:", credit)
            elif toppings == 0:
                print("Return to main menu")
                break
            else:
                print("you have entered the wrong input")
            print("would you like to add additional topping")
            choice = input("please y for yes and n for no")
            if choice.lower() =="n":
                break
            else:
                continue
while True:
    print("credit",credit)
    print("------------------")
    print("\t\tUCLAN PIZZA ")
    print("------------------")
    print("MAIN MENU")
    print("\t 1. Add Credits (current credits =",credit,"Credits")
    print("\t 2.Order Pizza")
    print("\t 0.Exit")
    m = int(input("enter a number:"))
    if m == 1:
        addcredit()
    elif m == 2:
        orderpizza()
    elif m == 0:
        break
    else:
        print("wrong input")





