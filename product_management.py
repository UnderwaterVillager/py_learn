import os
from product_operations import product_view, products

while True:
    while True:
        choice = input("Good Morning, what kind of operation would you like to perform?\n1- View products\n2- Add products\n3- Remove products\n4- Calculate storage value\n5- Apply discount\n")
        try:
            choice = int(choice)
            break
        except ValueError:
            os.system("cls")
            print("Incorrect type, try again!")
    if choice == 1:
        os.system("cls")
        product_view.see_product(products)
    elif choice == 2:
        print(2)
    elif choice == 3:
        print(3)
    elif choice == 4:
        print(4)
    elif choice == 5:
        print(5)
    else:
        os.system("cls")
        print("Option not available, try again!")