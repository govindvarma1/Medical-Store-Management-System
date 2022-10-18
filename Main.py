from Shop_Managment_system import database

while True:
    
    print("1.Display Available items\n2.Want to buy new product\n3.Sales Report\n4.Credit\n5.repayment of Dues\n6.Payment dues from customers")
    user_input=input("Choose any Option from above: ")
    
    while user_input not in ['1','2','3','4','5','6']:
        print("1.Display Available items\n2.Want to buy new product\n3.Sales Report\n4.Credit\n5.repayment of Dues\n6.Payment dues from customers")
        user_input = input("Choose a valid Option from above: ")
    
    user_input=int(user_input)
    
    if user_input == 1:
        database.stock_available()
    elif user_input == 2:
        item_name = input("Enter the Item: ")
        quantity = int(input("Enter the quantity You want to purchase: "))
        database.Buy(item_name, quantity)
    elif user_input == 3:
        database.sales()
    elif user_input == 4:
        cst_name = input("Enter the name: ")
        item_name = input("Enter The item name: ")
        quantity = int(input("Enter the quantity: "))
        database.lend(cst_name, item_name, quantity)
    elif user_input == 5:
        cst_name = input("Enter the name: ")
        database.repay(cst_name)
    elif user_input == 6:
        database.lendlist()
    choice = input("Enter q to Exit and c to continue: ").lower()
    
    if choice == "q":
        exit()
    else:
        continue
